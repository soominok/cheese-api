
from com_sba_api.uia.model.user_dto import UserDto
import numpy as np
import pandas as pd
from com_cheese_api.util.file import FileReader
from com_cheese_api.ext.db import url, db, openSession, engine
from pathlib import Path
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from sqlalchemy.ext.declarative import declarative_base
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold  # k value is understood as count
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.tree import DecisionTreeClassifier # dtree
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.naive_bayes import GaussianNB # nb
from sklearn.neighbors import KNeighborsClassifier # knn
from sklearn.svm import SVC # svm


import os
import json


Session = openSession()
session = Session()
    

class UserDao(UserDto):
    @classmethod
    def bulk(cls, UserDf):
        userDf = UserDf()
        df = UserDf.new()
        print(df.head())
        session.bulk_insert_mappings(UserDto, df.to_dict(orient="records"))
        session.commit()
        session.close()

    @staticmethod
    def save(user):
        session.add(user)
        session.commit()

    @classmethod
    def update(cls, user):
        session.query(cls).filter(cls.user_index == user['user_index'])\
            .update({cls.password: user['password']})
        session.commit()

    @classmethod
    def delete(cls, user_id):
        data = cls.query.get(user_index)
        db.session.delete(data)
        db.session.commit()

    @classmethod
    def count(cls):
        return session.query(func.count(cls.user_index)).one()

    @classmethod
    def find_all(cls):
        # sql = cls.query
        # df = pd.read_sql(sql.statement, sql.session.bind)
        # return json.loads(df.to_json(orient='records'))
        return session.query(cls).all()

    @classmethod
    def find_one(cls, user_id):
        return session.query(cls)\
            .filter(cls.user_id == user_id).one()
#     '''
#     SELECT *
#     FROM users
#     WHERE user_name LIKE 'name'
#     '''

#     @classmethod
#     def find_by_name(cls, name):
#         return session.query(cls).filter(cls.user_id.like(f'%{name}%')).all()

    '''
    SELECT *
    FROM users
    WHERE user_id IN (start, end)
    '''
    # List of users from start to end ?
    @classmethod
    def find_user_in_category(cls, start, end):
        return session.query(cls)\
                      .filter(cls.user_id.in_([start,end])).all()

    '''
    SELECT *
    FROM users
    WHERE gender LIKE 'gender' AND name LIKE 'name%'
    '''
    # Please enter this at the top. 
    # from sqlalchemy import and_
    @classmethod
    def find_users_by_gender_and_age(cls, gender, id):
        return session.query(cls)\
                      .filter(and_(cls.gender.like(gender),
                       cls.name.like(f'{id}%'))).all()

    '''
    SELECT *
    FROM users
    WHERE pclass LIKE '1' OR age_group LIKE '3'
    '''
    # Please enter this at the top. 
    # from sqlalchemy import or_
    @classmethod
    def find_users_by_gender_and_name(cls, gender, age_group):
        return session.query(cls)\
                      .filter(or_(cls.pclass.like(gender),
                       cls.age_group.like(f'{age_group}%'))).all()
    
    '''
    SELECT *
    FROM users
    WHERE user_id LIKE '1' AND password LIKE '1'
    '''
    @classmethod
    def login(cls, user):
        return session.query(cls)\
            .filter(cls.user_id == user.user_id, 
            cls.password == user.password).one()
            
if __name__ == '__main__':
    UserDao.bulk()