import pandas as pd
import pymysql
from datetime import datetime



class RecommendDfo:
    def dump_to_csv(self, query, param):
        # DB Connection
        conn = pymysql.connect(host='localhost', port= 3306,
                user='root',
                password='sum_9386+',
                database='com_cheese_api')

        # Start Time
        start_tm = datetime.now()

        # Get a DataFrame
        # global query_result

        query_result = pd.read_sql_query(query, conn, params = {'userId': param})

        # Close connection
        end_tm = datetime.now()

        print('START TIME: ', str(start_tm))
        print('END TIME: ', str(end_tm))
        print('ELAP time: ', str(end_tm - start_tm))
        conn.close()
        
        print(type(query_result))
        print(query_result)

    #     dummy_result = pd.get_dummies(query_result)
    #     print(dummy_result)
    #     features = ['user_id',  '간식', '감자', '견과류', '과일', '그라탕',
    #    '김가루', '꿀', '딥소스', '라자냐', '리소토', '마르게리타 피자', '막걸리', '맥앤치즈', '맥주',
    #    '멤브리요', '무화과', '바질', '발사믹 식초', '발사믹식초', '배', '베이컨', '볶음밥', '비스킷', '빵',
    #    '사케', '사퀘테리', '샌드위치', '샐러드', '샐러리', '샤퀴테리', '소금', '스테이크', '스프', '스프레드',
    #    '올리브오일', '올리브유', '와인', '위스키', '잼', '채소', '치즈케이크', '카나페', '카프레제',
    #    '카프레제 샐러드', '크래커', '크로스티니', '키쉬', '타르트', '타파스', '테이블치즈', '토마토', '토스트',
    #    '파스타', '팬케이크', '퐁듀', '피자', '핑거 푸드', '핑거푸드', '화이트와인']
    #     dummy_df = pd.DataFrame(dummy_result, columns=features)
    #     print(dummy_df)
    #     print(dummy_df.columns)
    #     print(dummy_df.isnull().sum())
        food_value = query_result.values
        print(food_value)
        print(type(food_value))

        return query_result

query = """
    SELECT * FROM recommends
"""

if __name__ == '__main__':
    recommendDfo = RecommendDfo()
    recommendDfo.dump_to_csv(query)





# import pandas as pd
# import pymysql
# from datetime import datetime



# class RecommendDfo:
#     def dump_to_csv(self, query):
#         # DB Connection
#         conn = pymysql.connect(host='localhost', port= 3306,
#                 user='root',
#                 password='sum_9386+',
#                 database='com_cheese_api')

#         # Start Time
#         start_tm = datetime.now()

#         # Get a DataFrame
#         # global query_result

#         query_result = pd.read_sql(query, conn)

#         # Close connection
#         end_tm = datetime.now()

#         print('START TIME: ', str(start_tm))
#         print('END TIME: ', str(end_tm))
#         print('ELAP time: ', str(end_tm - start_tm))
#         conn.close()
        
#         print(type(query_result))

#         dummy_result = pd.get_dummies(query_result)
#         print(dummy_result)
#         features = ['user_id',  '간식', '감자', '견과류', '과일', '그라탕',
#        '김가루', '꿀', '딥소스', '라자냐', '리소토', '마르게리타 피자', '막걸리', '맥앤치즈', '맥주',
#        '멤브리요', '무화과', '바질', '발사믹 식초', '발사믹식초', '배', '베이컨', '볶음밥', '비스킷', '빵',
#        '사케', '사퀘테리', '샌드위치', '샐러드', '샐러리', '샤퀴테리', '소금', '스테이크', '스프', '스프레드',
#        '올리브오일', '올리브유', '와인', '위스키', '잼', '채소', '치즈케이크', '카나페', '카프레제',
#        '카프레제 샐러드', '크래커', '크로스티니', '키쉬', '타르트', '타파스', '테이블치즈', '토마토', '토스트',
#        '파스타', '팬케이크', '퐁듀', '피자', '핑거 푸드', '핑거푸드', '화이트와인']
#         dummy_df = pd.DataFrame(dummy_result, columns=features)
#         print(dummy_df)
#         print(dummy_df.columns)
#         print(dummy_df.isnull().sum())
#         food_value = query_result.values
#         print(food_value)
#         print(type(food_value))

#         # df_dict = {}
#         # df_list = []
#         # for row in query_result.itertuples():
#         #     print(row)
#         #     for num in range(3):
#         #         for column_item in dummy_df.columns:
#         #             # for food_item in food_value[row]:
#         #                 # print(food_item)
#         #                 # print(dummy_df.isin([food_item]))
#         #             while column_item in row[num + 2]:
#         #                 dummy_df[row[num + 2]] = 1
#         #                 df_dict[row[num + 2]] = 1
#         #                 if row[0] == row[0] + 1:
#         #                     break
#         #     df_list.append(df_dict)
#         df_dict = {}
#         df_list = []

#         for column_item in dummy_df.columns:
#             for food_item in food_value:
#                 # print(food_item)
#                 # print(dummy_df.isin([food_item]))
#                 if (dummy_df.iloc[:, 0] == 0).all():
#                     if column_item in food_item:
#                         dummy_df.loc[0, column_item] = 1
#                         dummy_df.loc[1, column_item] = 1
#                     else:
#                         dummy_df.fillna(0)
#                 if (dummy_df.iloc[:, 0] == 1).all():
#                     if column_item in food_item:
#                         dummy_df.loc[0, column_item] = 1
#                         dummy_df.loc[1, column_item] = 1
#                     else:
#                         dummy_df.fillna(0)
#                 if (dummy_df.iloc[:, 0] == 2).all():
#                     if column_item in food_item:
#                         dummy_df.loc[0, column_item] = 1
#                         dummy_df.loc[1, column_item] = 1
#                     else:
#                         dummy_df.fillna(0)

#                 if (dummy_df.iloc[:, 0] == 3).all():
#                     if column_item in food_item:
#                         dummy_df.loc[0, column_item] = 1
#                         dummy_df.loc[1, column_item] = 1
#                     else:
#                         dummy_df.fillna(0)
#             # df_list.append(df_dict)

#         # df_list = {}
#         # for row in query_result.index:
#         #     for column_item in dummy_df.columns:
#         #         # for food_item in food_value[row]:
#         #             # print(food_item)
#         #             # print(dummy_df.isin([food_item]))
#         #         if column_item in food_value:
#         #             dummy_df.loc[row, column_item] = 1
#         #             # df_list[row[num + 2]] = 1
#         #         # break



#         print(dummy_df)
#         print(df_dict)  
#         print(df_list)

#         # df_list = {}
#         # for food_item in food_value:
#         #     # print(dummy_df.isin([food_item]))
#         #     # if (dummy_df.columns == food_item).any():
#         #     for column_item in dummy_df.columns:
#         #         if column_item in food_item:
#         #             df_list[column_item] = 1
#         #         # dummy_df[food_item] = 1


#         # print(df_list)

#         # for food_item in food_value:
#         #     for column_item in dummy_df.columns:
#         #         if column_item in food_item:
#         #             for row_index in query_result.iterrows():
#         #                 dummy_df[column_item] = 1
#         #         else:
#         #             dummy_df.fillna(0)

#         # for row_index, value in query_result.iterrows():
#         #     print (row_index,value)

#         # print(dummy_df)
#         # print(dummy_df.isnull().sum())
#         # print(dummy_result.values())
#         return query_result

# query = """
#     SELECT * FROM recommends
# """

# if __name__ == '__main__':
#     recommendDfo = RecommendDfo()
#     recommendDfo.dump_to_csv(query)

