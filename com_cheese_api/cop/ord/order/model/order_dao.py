from com_cheese_api.cop.ord.order.model.order_dto import OrderDto
from com_cheese_api.cop.ord.order.model.order_dfo import OrderDfo
import numpy as np
import pandas as pd
# from com_cheese_api.util.file import FileReader
# from com_cheese_api.cmm.utl.file import FileReader
from pathlib import Path
from com_cheese_api.ext.db import url, db, openSession, engine
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from sqlalchemy import func
from sqlalchemy import and_, or_
from sqlalchemy.ext.declarative import declarative_base

import os
import json


Session = openSession()
session = Session()

class OrderDao(OrderDto):

    # @classmethod
    # def bulk(cls, user_dfo):
    #     user_dfo = OrderDfo()
    #     dfo = user_dfo.create()
    #     print(user_dfo.head())
    #     session.bulk_insert_mappings(cls, dfo.to_dict(orient="records"))
    #     session.commit()
    #     session.close()

    @staticmethod
    def bulk():
        orderDfo = OrderDfo()
        df = orderDfo.new()
        print(df.head())
        session.bulk_insert_mappings(OrderDto, df.to_dict(orient="records"))
        session.commit()
        session.close()

    @staticmethod
    def save(user):
        session.add(user)
        session.commit()

    @classmethod
    def update(cls, user):
        session.query(cls).filter(cls.user_no == user['user_no'])\
                .update({cls.password: user['password'],\
                cls.gender:user['gender'],\
                cls.age_group:user['age_group']})
        session.commit()

    @classmethod
    def delete(cls, user_no):
        data = cls.query.get(user_no)
        db.session.delete(data)
        db.session.commit()

    @classmethod
    def count(cls):
        return session.query(func.count(cls.user_no)).one()

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    '''
    SELECT * FROM users
    WHERE user_name LIKE a
    '''

    @classmethod
    def find_one(cls, user_id):
        print('===================cls.user_id=====================')
        print(cls.user_id)
        print('===================user_id=====================')
        print(user_id)
        a = session.query(cls).filter(cls.user_id == user_id).one()
        print('=================find_one===================')
        print(a)
        print('=================find_one===================')
        return session.query(cls).filter(cls.user_id == user_id).one()

    # @classmethod
    # def find_by_name(cls, name):
    #     return session.query(cls).filter(cls.user_no.like(f'%{name}%')).all()

    @classmethod
    def find_by_id(cls, user_id):
        """
        주어진 아이디를 토대로 유저를 찾아서
        해당 정보를 리턴해준다.
        """
        # return session.query(cls).filter(cls.user_id.like(f'{user_id}')).all()
        return session.query(cls).filter(cls.user_id.like(f'{user_id}')).first()

        # return session.query(OrderDto).filter(OrderDto.user_id.like(f'{user_id}')).one()

    # @classmethod
    # def find_users_in_category(cls, start, end):
    #     return session.query(cls) \
    #         .filter(cls.user_id.in_([start, end])).all()

    # @classmethod
    # def find_users_by_gender_and_age(cls, gender, age_group):
    #     return session.query(cls) \
    #         .filter(and_(cls.gender.like(gender),
    #         cls.age_group.like(f'{age_group}%'))).all()


    # '''
    # SELECT *
    # FROM users
    # WHERE user_id IN (start, end)
    # '''
    # # List of users from start to end ?
    # @classmethod
    # def find_users_in_category(cls, start, end):
    #     return session.query(cls)\
    #                   .filter(cls.user_id.in_([start,end])).all()


    '''
    SELECT *
    FROM users
    WHERE user_id LIKE '1' AND password LIKE '1'
    '''

    # @classmethod
    # def login(cls, user):
    #     """
    #     유저 정보를 받아와, 해당 유저가 데이터베이스에 있는지 확인.
    #     확인 후, 있으면 로그인 시켜준다.
    #     Parameter: 유저 모델을 받아온다
    #     return: 유저 정보를 리턴해준다.
    #     """
    #     print("----------------login")
    #     sql = cls.query\
    #         .filter(cls.user_id.like(user.user_id))\
    #         .filter(cls.password.like(user.password))
    #     print("login type ", type(sql))
    #     df = pd.read_sql(sql.statement, sql.session.bind)
    #     print(json.loads(df.to_json(orient='records')))
    #     return json.loads(df.to_json(orient='records'))

        # return session.query(cls)\
        #     .filter(cls.user_id == user.user_id,
        #         cls.password == user.password).one()

    @classmethod
    def login(cls, user):
        return session.query(cls).filter(cls.user_id == user.user_id,
            cls.password == user.password).first()


    # '''
    # SELECT *
    # FROM users
    # WHERE gender LIKE 'gender' AND name LIKE 'name%'
    # '''
    # # Please enter this at the top. 
    # # from sqlalchemy import and_
    # @classmethod
    # def find_users_by_gender_and_name(cls, gender, name):
    #     return session.query(cls)\
    #                   .filter(and_(cls.gender.like(gender),
    #                    cls.name.like(f'{name}%'))).all()

    # '''
    # SELECT *
    # FROM users
    # WHERE pclass LIKE '1' OR age_group LIKE '3'
    # '''
    # # Please enter this at the top. 
    # # from sqlalchemy import or_
    # @classmethod
    # def find_users_by_gender_and_name(cls, gender, age_group):
    #     return session.query(cls)\
    #                   .filter(or_(cls.pclass.like(gender),
    #                    cls.age_group.like(f'{age_group}%'))).all()



if __name__ == '__main__':
    """
    데이터 베이스에 모든 유저 정보들을 넣어준다.
    """
    OrderDao.bulk()