from com_cheese_api.cop.rec.recommend.model.recommend_dfo import RecommendDfo
import pandas as pd
import numpy as np
import os

import joblib
from com_cheese_api.cmm.utl.file import FileReader


class RecommendAi(object):
    def __init__(self):
        self.data = None
        # self.cheese_model = joblib.load("com_cheese_api/cop/machine/cheese_knn_model.pkl")
        self.cheese_model = joblib.load("com_cheese_api/cop/machine/cheese_model.h5")
        
    @staticmethod
    def read_survey(input_user_id):
        query = """SELECT * FROM recommends WHERE user_id = input_user_id"""
        survey_result = RecommendDfo().dump_to_csv(query)
        # cheese_data = FileReader.csv_load(file_path, 'utf-8-sig')
        return survey_result
    

    def preprocessing_data(self, input_user_id):
        survey_result = RecommendAi.read_survey(input_user_id) 
        # dummy_result = pd.get_dummies(survey_result)
        # print(dummy_result)

        features = ['user_id',  '간식', '감자', '견과류', '과일', '그라탕',
       '김가루', '꿀', '딥소스', '라자냐', '리소토', '마르게리타 피자', '막걸리', '맥앤치즈', '맥주',
       '멤브리요', '무화과', '바질', '발사믹 식초', '발사믹식초', '배', '베이컨', '볶음밥', '비스킷', '빵',
       '사케', '사퀘테리', '샌드위치', '샐러드', '샐러리', '샤퀴테리', '소금', '스테이크', '스프', '스프레드',
       '올리브오일', '올리브유', '와인', '위스키', '잼', '채소', '치즈케이크', '카나페', '카프레제',
       '카프레제 샐러드', '크래커', '크로스티니', '키쉬', '타르트', '타파스', '테이블치즈', '토마토', '토스트',
       '파스타', '팬케이크', '퐁듀', '피자', '핑거 푸드', '핑거푸드', '화이트와인']
        survey_df = pd.DataFrame(survey_result, columns=features)
        # print(dummy_df)
        # print(dummy_df.columns)
        # print(dummy_df.isnull().sum())
        food_value = survey_result.values
        # print(food_value)
        # print(type(food_value))

        # for food_item in food_value:
        #     for column_item in survey_df.columns:
        #         if column_item in food_item:
        #             for row_index in survey_result.iterrows():
        #                 survey_df[column_item] = 1
        #         else:
        #             survey_df.fillna(0)

        for food_item in food_value:
            for column_item in survey_df.columns:
                if column_item in food_item:
                    survey_df[food_item] = 1
        survey_df.fillna(0)
        self.data = survey_df

    def recommend_cheese(self):
        return self.predict_data(self.model, self.data)
    # def predict_data(self, model, data):        
    #     recom_cheese = data['chooseFood_1', 'chooseFood_2']
        


if __name__ == '__main__':
    recommendAi = RecommendAi()
    recommendAi.dump_to_csv('com_cheese_api', 'com_cheese_api/cop/rec/recommend/data/recommend_data.csv')


# from com_cheese_api.cop.rec.recommend.model.recommend_dfo import RecommendDfo
# import pandas as pd
# import numpy as np
# import os

# import joblib
# from com_cheese_api.cmm.utl.file import FileReader


# class RecommendAi(object):
#     def __init__(self):
#         self.data = RecommendDfo().dump_to_csv
#         # self.cheese_model = joblib.load("com_cheese_api/cop/machine/cheese_knn_model.pkl")
#         self.cheese_model = joblib.load("com_cheese_api/cop/machine/cheese_model.h5")


#     def recommend_cheese(self, user_id, file_path):
#         query = """SELECT * FROM recommends WHERE user_id = 'user_id'"""
#         survey = self.data(query)
#         # cheese_data = FileReader.csv_load(file_path, 'utf-8-sig')
#         return self.predict_data(self.model, survey)

#     def predict_data(self, model, data):        
#         recom_cheese = data['chooseFood_1', 'chooseFood_2']
        


# if __name__ == '__main__':
#     recommendAi = RecommendAi()
#     # recommendAi.dump_to_csv('com_cheese_api', 'com_cheese_api/cop/rec/recommend/data/recommend_data.csv')