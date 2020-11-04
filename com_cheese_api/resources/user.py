import numpy as np
import pandas as pd
from com_cheese_api.util.file import FileReader
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

from sklearn.model_selection import train_test_split

import os

class UserDf:
    def __init__(self):
        self.fileReader = FileReader()
        self.data = os.path.join(os.path.abspath(os.path.dirname(__file__))+'/data')
        self.user = None
        self.odf = None

    #------------------------------------------ 데이터셋 1차 정제 ------------------------------------------#

    def new_model(self, payload):
        this = self.fileReader
        this.data = self.data
        this.fname = payload
        print(f'{self.data}')
        print(f'{this.fname}')
        return pd.read_csv(Path(self.data, this.fname))


    def user_hook(self):
        user_origin = 'users.csv'
        cheese = 'cheese_data.csv'
        this = self.fileReader
        this.user_origin = self.new_model(user_origin) # payload
        this.cheese = self.new_model(cheese)

        # print(this.user_origin)
        # print(this.cheese)

        category_count = self.category_Count(this.user_origin)
        item_count = self.item_Count(this.user_origin, category_count)
        this.user = self.change_to_cheese(this.cheese, item_count)
        user_split = self.user_data_split(this.user)
        # print(f'Preprocessing User Dataset : {this.user}')

        # print(min(this.user['user_age'])) # 고객 최소 나이 : 10
        # print(max(this.user['user_age'])) # 고객 최대 나이 : 80
        
        show_age_plot = self.find_requency(this.user, 'user_index', 'user_age') 
        # 30대(1만5천) > 40대(1만4천) > 20대(3천5백) > 50대(3천1백) > 60대(523) > 10대=70대(80) >80대
        print(show_age_plot)

        return this


    def new(self):
        # train, test 데이터#
        train = 'user_train.csv'
        test = 'user_test.csv'
        this = self.fileReader
        this.train = self.new_model(train) # payload
        this.test = self.new_model(test) # payload

        '''
        Original Model Generation
        '''

        self.odf = pd.DataFrame(
            {
                'user_id': this.train.user_id,
                'password': '1'
            }
        )

        train_find_null = self.find_null(this.train)
        test_find_null = self.find_null(this.test)
        
        # print(test_find_null)
        
        this.id = this.test['user_id'] # This becomes a question.
        
        # print(f'Preprocessing Train Variable : {this.train.columns}')
        # print(f'Preprocession Test Variable : {this.test.columns}')
        
        this = self.cheese_rank_oridinal(this)
        this = self.user_gender_norminal(this)
        this = self.user_age_norminal(this)
        print(this)

        
        # 변수들 수치로 바꾸고 해보기
        #show_corr = self.make_corr(this.train)





    @staticmethod
    def make_barplot(x_name, y_name, data_name):
        # font_path = 'C:\\Windows\\Fonts\\NanumGothic.ttf'
        # font_name1 = fm.FontProperties(fname = font_path).get_name()
        # plt.rc('font', family = font_name1)
        plt.xticks(rotation = 45)
        sns.barplot(x = x_name, y = y_name, data = data_name)
        plt.show()

    @staticmethod
    def find_requency(data, column1, column2):
        count_size = data[column1].groupby(data[column2]).count().reset_index(name='counts')
        count_size['rank'] = count_size['counts'].rank(ascending=False)
        barplot = UserDf.make_barplot(column2, 'counts', count_size)
        return count_size

    @staticmethod
    def category_Count(data) -> object:
        sub_size = data['buy_count'].groupby(data['sub1_category']).sum().reset_index(name='sub1_counts')
        sub_size['sub1_rank'] = sub_size['sub1_counts'].rank(ascending=False)
        # barplot = UserDf.make_barplot('sub1_category', 'sub1_counts', sub_size)
        return sub_size

    @staticmethod
    def item_Count(data, category_count):
        item_size = data['buy_count'].groupby([data['sub1_category'],data['sub2_category']]).sum().reset_index(name='sub2_counts')
        item_size['sub2_rank'] = item_size['sub2_counts'].rank(ascending=False, method="dense")

        category_item_rank = pd.merge(category_count, item_size, on = 'sub1_category', how = 'right')
        user_item_rank = pd.merge(data, category_item_rank, on = 'sub2_category', how = 'left')
        # print(user_item_rank)

        user_items_ranks = user_item_rank.drop(['sub1_category_y'], axis=1)
        users_item_data = user_items_ranks.rename(columns={'sub1_category_x': 'sub1_category'})
        # print(users_item_data)

        return users_item_data    


    @staticmethod
    def change_to_cheese(data, item_count):
        cheese_df = data.rename(columns={'ranking': 'sub2_rank'})
        user_cheese_merge = pd.merge(item_count, cheese_df, on = 'sub2_rank', how = 'left')
        user_data1 = user_cheese_merge.drop(['item_code', 'item_name', 'item_add_name', 'category_x', 'sub1_category', 'sub2_category', 'item_brand', 'sub1_counts', 'sub1_rank', 'sub2_counts', 'buy_price'], axis=1)
        user_data2 = user_data1.drop(['country', 'matching', 'matching.1', 'content', 'img'], axis=1)
        user_data_fin = user_data2.rename(columns={'Unnamed: 0_x': 'user_index', 'Unnamed: 0_y': 'cheese_code', 'brand': 'cheese_brand', 'name': 'cheese_name', 'price' : 'cheese_one_price', 'sub2_rank': 'cheese_rank', \
                                                        'category_y': 'cheese_category', 'texture': 'cheese_texture', 'types': 'cheese_types'})
        # print(list(users_cheese_merge))
        # print(user_data_fin)
        user_data_fin.to_csv(os.path.join('com_cheese_api/resources/data', 'user_data.csv'), index=False)
        return user_data_fin
    # item_Change()


    @staticmethod
    def user_data_split (data):
        user_train, user_test = train_test_split(data, test_size=0.3, random_state = 32)
        user_train.to_csv(os.path.join('com_cheese_api/resources/data', 'user_train.csv'), index=False)
        user_test.to_csv(os.path.join('com_cheese_api/resources/data', 'user_test.csv'), index=False)
        return user_train, user_test

    @staticmethod
    def find_null(data):
        null_num = data.isnull().sum()
        return null_num

    #-------------------------------------------데이터 2차 정제-------------------------------------------#
    
    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('cheese_category', axis=1) # Train is a dataset in which the answer is removed. 

    @staticmethod
    def create_label(this) -> object:
        return this.train['cheese_category'] # Label is the answer.

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis = 1)
        this.test = this.test.drop([feature], axis = 1)
        return this


    ###### 데이터 drop, ordinal, nomianl #####

    @staticmethod
    def cheese_rank_oridinal(this) -> object:
        return this

    @staticmethod
    def user_gender_norminal(this) -> object:
        combine = [this.train, this.test] # Train and test are bound.
        gender_mapping = {'M': 0, 'F': 1}
        for dataset in combine:
            dataset['user_gender'] = dataset['user_gender'].map(gender_mapping)
        this.train = this.train # overriding
        this.test = this.test
        return this


    @staticmethod
    def user_age_norminal(this) -> object:
        train = this.train
        test = this.test

        bins = [20, 30, 40, 50, np.inf]
        labels = ['Youth', 'Adult30', 'Adult40', 'Adult50' 'Senior']
        train['age_group'] = pd.cut(train['user_age'], bins, labels = labels)
        test['age_group'] = pd.cut(test['user_age'], bins, labels = labels)
        age_title_mapping = {
            1: 'Youth',
            2: 'Adult30',
            3: 'Adult40',
            4: 'Adult50',
            5: 'Senior'
        }
        for x in range(len(train['age_group'])):
            if train['age_group'][x] == 'Unknown':
                train['age_group'][x] = age_title_mapping[train['Title'][x]]
        for x in range(len(test['age_group'])):
            if test['age_group'][x] == 'Unknow':
                test['age_group'][x] = age_title_mapping[test['Title'][x]]

        age_mapping = {
            'Youth': 1,
            'Adult30': 2 ,
            'Adult40': 3 ,
            'Adult50': 4,
            'Senior': 5
        }
        train['age_group'] = train['age_group'].map(age_mapping)
        test['age_group'] = test['age_group'].map(age_mapping)
        this.train = this.train
        this.test = this.test
        return this




    @staticmethod
    def make_Corr(data):
        make_corr = data.corr()
        return 

    @staticmethod
    def make_heatmap(make_corr):
        sns.clustermap(make_corr, annot = True, cmap = 'RdylBu_r', mask = mask, linewidths = .5, cbar_kws = {"shrink": .5}, vmin = -1, vmax = 1)
        plt.show()





if __name__ == '__main__':
    userDf = UserDf()
    userDf.new()





#     @staticmethod
#     def create_label(this):
#         return this.train['cheese_category'] # Label = answer

#     @staticmethod
#     def drop_feature(this, feature):
#         this.train = this.train.drop([feature], axis = 1)
#         this.test = this.test.drop([feature], axis = 1)
#         return this
        
#     @staticmethod
#     def gender_norminal(this):
#         combine = [this.train, this.test]
#         gender_mapping = {'male': 0, 'female': 1}
#         for dataset in combine:
#             dataset['user_gender'] = dataset['user_gender'].map(gender_mapping)
#         this.train = this.train
#         this.test = this.test
#         return this




# if __name__ == '__main__':
#     UserDf.show_User_Df()

# #------------------------------------------ 데이터 탐색 & 시각화 ------------------------------------------#

#     # def make_wordcloud(self):
#     #     user_data = show_df()
#     #     user_df = _data.loc[:,['cheese_name']]
#     #     user_lists = np.array(user_df['cheese_name'].tolist())
                
#     #     with open('com_cheese_api/user/data/stopword.txt', 'r') as file:
#     #         lines = file.readlines()
#     #         stop_str = ''.join(lines)
#     #         stopword = stop_str.replace('\n', ' ')
#     #     stopwords = stopword.split(' ')

#     #     sentences_tag = []
        
#     #     #형태소 분석하여 리스트에 넣기
#     #     for sentence in _lists:
#     #         morph = self.okt.pos(sentence)
#     #         sentences_tag.append(morph)
#     #         #print(morph)
#     #         #print('-' * 30)
        
#     #     #print(sentences_tag)
#     #     #print('\n' * 3)
        
#     #     noun_adj_list = []
#     #     #명사와 형용사만 구분하여 이스트에 넣기
#     #     for sentence1 in sentences_tag:
#     #         for word, tag in sentence1:
#     #             if word not in stopwords:
#     #                 if tag in ['Noun']:
#     #                     if len(word) >= 2:
#     #                         noun_adj_list.append(word)
                        
        
#     #     word_count_list = []
#     #     #형태소별 count
#     #     counts = Counter(noun_adj_list)
#     #     tags = counts.most_common(100)
#     #     word_count_list.append(tags)
#     #     word_list = sum(word_count_list, [])
#     #     print(word_list)
#     #     print(type(word_list))
    
#     #     # wordCloud 생성
#     #     # 한글 깨지는 문제 해결하기 위해 font_path 지정
#     #     wc = WordCloud(font_path='/usr/share/fonts/truetype/nanum/NanumBarunGothicBold.ttf', background_color='white', width=800, height=600)
#     #     #print(dict(tags))
#     #     cloud = wc.generate_from_frequencies(dict(tags))
#     #     plt.figure(figsize=(10, 8))
#     #     plt.axis('off')
#     #     plt.imshow(cloud)
#     #     return plt.show()

