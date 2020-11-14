import numpy as np
import pandas as pd
# from com_cheese_api.util.file import FileReader
# from com_cheese_api.cmm.utl.file import FileReader
from pathlib import Path
from com_cheese_api.ext.db import url, db, openSession, engine
# from com_cheese_api.cop.rev.review.model.review_dto import ReviewDto

# from sqlalchemy import func
# from sqlalchemy.ext.declarative import declarative_base

import os
import json

# class UserDto(db.Model):
#     __tablename__ = 'users'
#     __table_args__ = {'mysql_collate':'utf8_general_ci'}

#     user_no: int = db.Column(db.Integer, primary_key= True, index = True)
#     user_id: str = db.Column(db.String(20))
#     password: str = db.Column(db.String(1))
#     gender: int = db.Column(db.Integer)
#     age_group: int = db.Column(db.Integer)
#     cheese_texture: int = db.Column(db.Integer)
#     buy_count: int = db.Column(db.Integer)

#     # orders = db.relationship('OrderDto', back_populates='user', lazy='dynamic')
#     # prices = db.relationship('PriceDto', back_populates='user', lazy='dynamic')
#     # articles = db.relationship('ArticleDto', back_populates='user', lazy='dynamic')

#     # reviews = db.relationship('ReviewDto', back_populates='users', lazy='dynamic')
    
#     # 관계 설정
#     #reviews = db.relationship('ReviewDto', back_populates='users')

#     # def __init__(self, user_no, user_id, password, gender, age_group, cheese_texture, buy_count):
#     #     self.user_no = user_no
#     #     self.user_id = user_id
#     #     self.password = password
#     #     self.gender = gender
#     #     self.age_group = age_group
#     #     self.cheese_texture = cheese_texture
#     #     self.buy_count = buy_count

#     def __repr__(self):
#         return f'User(user_no={self.user_no}, user_id={self.user_id}, password={self.password}, \
#                     gender = {self.gender}, age_group={self.age_group}, \
#                     cheese_texture={self.cheese_texture}, \
#                     buy_count={self.buy_count})'

#     def __str__(self):
#         return f'User(user_no={self.user_no}, user_id={self.user_id}, password={self.password}, \
#                     gender = {self.gender}, age_group={self.age_group},\
#                     cheese_texture={self.cheese_texture}, \
#                     buy_count={self.buy_count})'

#     @property
#     def json(self):
#         return {
#             'user_no' : self.user_no,
#             'user_id' : self.user_id,
#             'password': self.password,
#             'gender': self.gender,
#             'age_group': self.age_group,
#             'cheese_texture': self.cheese_texture,
#             'buy_count': self.buy_count
#         }

# # Json 형태로 쓰기 위해 씀!
# class UserVo():
#     user_no: int = 0
#     user_id: str = ''
#     password: str = ''
#     gender: int = 0
#     age_group: int = 0
#     cheese_texture: int = 0
#     buy_count: int = 0


class UserDto(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'mysql_collate':'utf8_general_ci'}

    user_no: int = db.Column(db.Integer, primary_key= True, index = True)
    user_id: str = db.Column(db.String(20))
    password: str = db.Column(db.String(5))
    gender: str = db.Column(db.String(5))
    age: int = db.Column(db.Integer)
    cheese_name: str = db.Column(db.String(100))
    cheese_texture: str = db.Column(db.String(100))
    cheese_category: str = db.Column(db.String(50))
    buy_count: int = db.Column(db.Integer)
    total_price: int = db.Column(db.Integer)

    # orders = db.relationship('OrderDto', back_populates='user', lazy='dynamic')
    # prices = db.relationship('PriceDto', back_populates='user', lazy='dynamic')
    # articles = db.relationship('ArticleDto', back_populates='user', lazy='dynamic')

    # reviews = db.relationship('ReviewDto', back_populates='users', lazy='dynamic')
    
    # 관계 설정
    #reviews = db.relationship('ReviewDto', back_populates='users')

    def __init__(self, user_no, user_id, password, gender, age, cheese_texture, buy_count):
        self.user_no = user_no
        self.user_id = user_id
        self.password = password
        self.gender = gender
        self.age = age
        self.cheese_name = cheese_name
        self.cheese_texture = cheese_texture
        self.cheese_category = cheese_category
        self.buy_count = buy_count
        self.total_price = total_price

    def __repr__(self):
        return f'User(user_no={self.user_no}, user_id={self.user_id}, password={self.password}, \
                    gender = {self.gender}, age={self.age}, cheese_name={self.cheese_name},\
                    cheese_texture={self.cheese_texture}, cheese_category={self.cheese_category}, \
                    buy_count={self.buy_count}, total_price={self.total_price})'

    def __str__(self):
        return f'User(user_no={self.user_no}, user_id={self.user_id}, password={self.password}, \
                    gender = {self.gender}, age={self.age}, cheese_name={self.cheese_name},\
                    cheese_texture={self.cheese_texture}, cheese_category={self.cheese_category}, \
                    buy_count={self.buy_count}, total_price={self.total_price})'

    @property
    def json(self):
        return {
            'user_no' : self.user_no,
            'user_id' : self.user_id,
            'password': self.password,
            'gender': self.gender,
            'age': self.age,
            'cheese_name': self.cheese_name,
            'cheese_texture': self.cheese_texture,
            'cheese_category': self.cheese_category,
            'buy_count': self.buy_count,
            'total_price': self.total_price
        }

# Json 형태로 쓰기 위해 씀!
class UserVo():
    user_no: int = 0
    user_id: str = ''
    password: str = ''
    gender: str = ''
    age: int = 0
    cheese_name: str = ''
    cheese_texture: str = ''
    cheese_category: str = ''
    buy_count: int = 0
    total_price: int = 0


# db.init_app(app)
# with app.app_context():
#     db.create_all()