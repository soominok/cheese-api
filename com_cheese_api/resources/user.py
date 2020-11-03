import numpy as np
import pandas as pd
from com_cheese_api.util.file import FileReader

from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

from sklearn.model_selection import train_test_split

import os

# 1. 전처리 (Df로 전환) -> processing에 결과는 DF

# ==============================================================
# ====================                     =====================
# ====================    Preprocessing    =====================
# ====================                     =====================
# ==============================================================

class UserDf():
    def __init__(self):
        self.fileReader = FileReader()
        self.data = os.path.join(os.path.abspath(os.path.dirname(__file__))+'/data')
        self.odf = None

    def category_Count(self):
        users = self.data('users.csv')
        sub_size = users['buy_count'].groupby(users['sub1_category']).sum().reset_index(name='sub1_counts')
        sub_size['sub1_rank'] = sub_size['sub1_counts'].rank(ascending=False)
        item_count_plot = sns.barplot (x = 'sub1_category', y = 'sub1_counts', data = sub_size)
        # plt.show()
        # print(sub_size)
        return sub_size
    #category_Count()

    def item_Count():
        # sub1_category에서의 빈도 추출
        category_count = category_Count()

        # sub2_category에서의 빈도 추출
        item_size = users['buy_count'].groupby([users['sub1_category'],users['sub2_category']]).sum().reset_index(name='sub2_counts')
        
        #item_size['sub2_rank'] = item_size['sub2_counts'].rank(ascending=False, method="dense")
        item_size['sub2_rank'] = item_size['sub2_counts'].rank(ascending=False)

        # sub1 + sub2 rank 합치기
        category_item_rank = pd.merge(category_count, item_size, on = 'sub1_category', how = 'right')
        # print(category_item_rank)

        # 원래 데이터에 rank 주기 (중복에 대한 계산도 같이 해주기)
        user_item_rank = pd.merge(users, category_item_rank, on = 'sub2_category', how = 'left')
        print(user_item_rank)

        user_items_ranks = user_item_rank.drop(['sub1_category_y'], axis=1)
        users_item_data = user_items_ranks.rename(columns={'sub1_category_x': 'sub1_category'})

        # users_item_data.to_csv(os.path.join('com_cheese_api/resources/data', 'user_item_counts3.csv'), index=False)
        return users_item_data

    # item_count()

    @staticmethod
    def cheeseData():
        cheese_data = pd.read_csv("com_cheese_api/resources/data/cheese_data.csv")
        return cheese_data

    @staticmethod
    def item_Change():
        cheese_data = cheeseData()
        users_item_data = item_Count()
        cheese_df = cheese_data.rename(columns={'ranking': 'sub2_rank'})
        users_data = pd.merge(users_item_data, cheese_data, on = 'sub2_rank', how = 'left')
        user_datas = users_data.drop(['category_x', 'sub1_category', 'sub2_category', 'item_brand', 'sub1_counts', 'sub1_rank', 'sub2_counts', 'sub2_rank', 'content', 'buy_price', 'img'], axis=1)
        user_data = user_datas.drop(['Unnamed: 0', 'country', 'matching', 'matching.1', 'texture', 'types', 'category_y'], axis=1)
        user_data_fin = user_data.rename(columns={'brand': 'cheese_brand', 'name': 'cheese_name', 'price' : 'cheese_one_price'})
        print(user_data_fin)

        user_data_fin.to_csv(os.path.join('com_cheese_api/resources/data', 'user_data.csv'), index=False)
    #item_Change()


def show_df():
    user_data_1 = pd.read_csv('com_cheese_api/resources/data/user_data.csv')
    user_data = user_data_1.rename(columns={"name" : "cheese_name"})
    show_user = user_data.head(10)
    show_column = list(user_data)
    print(show_user)
    print(show_column)
    return user_data


def make_wordcloud(self):
        user_data = show_df()
        user_df = _data.loc[:,['cheese_name']]
        user_lists = np.array(user_df['cheese_name'].tolist())
                
        with open('com_cheese_api/user/data/stopword.txt', 'r') as file:
            lines = file.readlines()
            stop_str = ''.join(lines)
            stopword = stop_str.replace('\n', ' ')
        stopwords = stopword.split(' ')

        sentences_tag = []
        
        #형태소 분석하여 리스트에 넣기
        for sentence in _lists:
            morph = self.okt.pos(sentence)
            sentences_tag.append(morph)
            #print(morph)
            #print('-' * 30)
        
        #print(sentences_tag)
        #print('\n' * 3)
        
        noun_adj_list = []
        #명사와 형용사만 구분하여 이스트에 넣기
        for sentence1 in sentences_tag:
            for word, tag in sentence1:
                if word not in stopwords:
                    if tag in ['Noun']:
                        if len(word) >= 2:
                            noun_adj_list.append(word)
                        
        
        word_count_list = []
        #형태소별 count
        counts = Counter(noun_adj_list)
        tags = counts.most_common(100)
        word_count_list.append(tags)
        word_list = sum(word_count_list, [])
        print(word_list)
        print(type(word_list))
        
        
        # wordCloud 생성
        # 한글 깨지는 문제 해결하기 위해 font_path 지정
        wc = WordCloud(font_path='/usr/share/fonts/truetype/nanum/NanumBarunGothicBold.ttf', background_color='white', width=800, height=600)
        #print(dict(tags))
        cloud = wc.generate_from_frequencies(dict(tags))
        plt.figure(figsize=(10, 8))
        plt.axis('off')
        plt.imshow(cloud)
        return plt.show()

    #make_wordcloud()

def change_category() :
    user_data = show_user()
    u_df = _data.loc[:,['sub1_category']]
    u_lists = np.array(_df['sub1_category'].tolist())
    #print(type(_lists))

    rank_category = u_data['sub1_category'].value_counts()
    categories = np.array(rank_category.index).tolist()

    cheese_data = pd.read_csv("com_cheese_api/resources/data/cheese_data.csv")
    cheese_df = cheese_data.loc[:,['name']]
    cheese_lists = np.array(cheese_df['name']).tolist()
    #print(cheese_lists)

    match_value = {'영양제' : '모짜렐라', '생수' : '리코타', '닭고기류' : '블루치즈' , '냉동간편식' : '체다',\
                    '홍삼/인삼가공식품' : '파르미지아노 레지아노', '견과류' : '파르미지아노 레지아노', \
                        '포장반찬' : '고다', '건강진액' : '에멘탈', '건강보조식품' : '까망베르', '국산과일' : '부라타',\
                            '두유' : '만체고', '기능성음료' : '부라타', '축산선물세트' : '까망베르' }

    for u_list in range(len(u_lists)):
        u_df = _data.replace({'sub1_category': match_value})
    print(u_df)

def data_split ():
    users = pd.read_csv("com_cheese_api/resources/data/users.csv")
    user_train, user_test = train_test_split(users, test_size=0.3, random_state = 32)
    user_train.to_csv(os.path.join('com_cheese_api/resources/data', 'user_train.csv'), index=False)
    user_test.to_csv(os.path.join('com_cheese_api/resources/data', 'user_test.csv'), index=False)

def new(self):
    train = 'user_train.csv'
    test = 'user_test.csv'
    this = self.fileReader
    this.train = self.new_model(train) # payload
    this.test = self.new_model(test) # payload

    '''
    Original Model Generation
    '''

    self.odf = pd.Data

def corrs():
    return 


@staticmethod
def drop_feature(this, feature) -> object:
    this.train = this.train.drop([feature], axis = 1)
    this.test = this.test.drop([feature], axis = 1)
    return this

@staticmethod
def category_ordinal(this) -> object:
    category_title_mapping = {
        0 : '모짜렐라',
        1 : '블루치즈',
        2 : '리코타',
        3 : '체다',
        4 : '파르미지아노 레지아노',
        5 : '고다',
        6 : '까망베르',
        7 : '브리',
        8 : '만체고',
        9 : '에멘탈',
        10: '부라타'
    }

    for x in range(len(_df['sub1_category'])):
        if _df['sub1_category'][x] == '모짜렐라':
            _df['sub1_category'][x] == category_title_mapping[_df['Title'][x]]

    category_mapping = {
        0 : '모짜렐라',
        1 : '블루치즈',
        2 : '리코타',
        3 : '체다',
        4 : '파르미지아노 레지아노',
        5 : '고다',
        6 : '까망베르',
        7 : '브리',
        8 : '만체고',
        9 : '에멘탈',
        10: '부라타'
    }

    u_df['sub1_category'] = _df['sub1_category'].map(category_mapping)



# 3. 모델링 (Dto)

# ==============================================================
# =======================                =======================
# =======================    Modeling    =======================
# =======================                =======================
# ==============================================================

class UserDto():
    __tablename__ = 'users'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    user_id: str = db.Column(db.String(10), primary_key = True, index = True)
    password: str = db.Column(db.String(1))
    name: str = db.Column(db.String(100))
    pclass: int = db.Column(db.Integer)
    gender: int = db.Column(db.Integer)
    age_group: int = db.Column(db.Integer)
    embarked: int = db.Column(db.Integer)
    rank: int = db.Column(db.Integer)

    # orders = db.relationship('OrderDto', back_populates='user', lazy='dynamic')
    # prices = db.relationship('PriceDto', back_populates='user', lazy='dynamic')
    articles = db.relationship('ArticleDto', back_populates='user', lazy='dynamic')

    def __init__(self, user_id, password, name, pclass, gender, age_group, embarked, rank):
        self.user_id = user_id
        self.password = password
        self.name = name
        self.pclass = pclass
        self.gender = gender
        self.age_group = age_group
        self.embarked = embarked
        self.rank = rank

    def __repr__(self):
        return f'User(user_id={self.user_id},\
            password={self.password},name={self.name}, pclass={self.pclass}, gender={self.gender}, \
                age_group={self.age_group}, embarked={self.embarked}, rank={self.rank})'

    
    def __str__(self):
        return f'User(user_id={self.user_id},\
            password={self.password},name={self.name}, pclass={self.pclass}, gender={self.gender}, \
                age_group={self.age_group}, embarked={self.embarked}, rank={self.rank})'


    
    def json(self):
        return {
            'userId' : self.user_id,
            'password' : self.password,
            'name' : self.name,
            'pclass' : self.pclass,
            'gender' : self.gender,
            'ageGroup' : self.age_group,
            'embarked' : self.embarked,
            'rank' : self.rank
        }

# Json 형태로 쓰기 위해 씀!
class UserVo():
    user_id: str = ''
    password: str = ''
    name: str = ''
    pclass: int = 0
    gender: int = 0
    age_group: int = 0
    embarked: int = 0
    rank: int =  0

Session = openSession()
session = Session()
user_df = UserDf()

# 텐서플로우가 걸리는 곳
class UserTf():
    ...

# 인공지능 판단해주는 곳
class UserAi():
    ...

# 4. 프론트에 데이터 보내주는 행위 (프론트에서 이 내용이 보임!!)

# ==============================================================
# =====================                  =======================
# =====================    Resourcing    =======================
# =====================                  =======================
# ==============================================================

class User():
    ...