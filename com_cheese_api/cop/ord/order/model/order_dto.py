import numpy as np
import pandas as pd
# from com_cheese_api.util.file import FileReader
# from com_cheese_api.cmm.utl.file import FileReader
from pathlib import Path
from com_cheese_api.ext.db import url, db, openSession, engine
from com_cheese_api.cop.rev.review.model.review_dto import ReviewDto

from sqlalchemy import func
from sqlalchemy import ForeignKey
# from sqlalchemy.ext.declarative import declarative_base

import os
import json


# class OrderDto(db.Model):
#     __tablename__ = 'orders'
#     __table_args__ = {'mysql_collate':'utf8_general_ci'}

#     order_no: int = db.Column(db.Integer, primary_key= True, autoincrement=True, index = True)
#     user_id: str = db.Column(db.String(20))
#     gender: str = db.Column(db.String(5))
#     age: int = db.Column(db.Integer)
#     cheese_name: str = db.Column(db.String(100))
#     cheese_texture: str = db.Column(db.String(100))
#     cheese_category: str = db.Column(db.String(50))
#     buy_count: int = db.Column(db.Integer)
#     total_price: int = db.Column(db.Integer)

#     # 관계 설정
#     # reviews = db.relationship('ReviewDto', back_populates='users', lazy='dynamic')
    

#     def __init__(self, order_no, user_id, gender, age, cheese_texture, buy_count):
#         self.order_no = order_no
#         self.user_id = user_id
#         self.gender = gender
#         self.age = age
#         self.cheese_name = cheese_name
#         self.cheese_texture = cheese_texture
#         self.cheese_category = cheese_category
#         self.buy_count = buy_count
#         self.total_price = total_price

#     def __repr__(self):
#         return f'User(order_no={self.order_no}, user_id={self.user_id}, \
#                     gender = {self.gender}, age={self.age}, cheese_name={self.cheese_name},\
#                     cheese_texture={self.cheese_texture}, cheese_category={self.cheese_category}, \
#                     buy_count={self.buy_count}, total_price={self.total_price})'

#     def __str__(self):
#         return f'User(order_no={self.order_no}, user_id={self.user_id}, \
#                     gender = {self.gender}, age={self.age}, cheese_name={self.cheese_name},\
#                     cheese_texture={self.cheese_texture}, cheese_category={self.cheese_category}, \
#                     buy_count={self.buy_count}, total_price={self.total_price})'

#     @property
#     def json(self):
#         return {
#             'order_no' : self.order_no,
#             'user_id' : self.user_id,
#             'gender': self.gender,
#             'age': self.age,
#             'cheese_name': self.cheese_name,
#             'cheese_texture': self.cheese_texture,
#             'cheese_category': self.cheese_category,
#             'buy_count': self.buy_count,
#             'total_price': self.total_price,
#             # 'count': self.count
#             # 'rank': self.rank
#         }

# # Json 형태로 쓰기 위해 씀!
# class OrderVo():
#     order_no: int = 0
#     user_id: str = ''
#     gender: str = ''
#     age: int = 0
#     cheese_name: str = ''
#     cheese_texture: str = ''
#     cheese_category: str = ''
#     buy_count: int = 0
#     total_price: int = 0



class OrderDto(db.Model):
    __tablename__ = 'orders'
    __table_args__ = {'mysql_collate':'utf8_general_ci'}

    order_no: int = db.Column(db.Integer, primary_key= True, autoincrement=True, index = True)
    user_id: str = db.Column(db.String(20), ForeignKey('users.user_id'))
    cheese_id: str = db.Column(db.String(20), ForeignKey('cheeses.cheese_id'))
    buy_count: int = db.Column(db.Integer)
    total_price: int = db.Column(db.Integer)

    # 관계 설정
    # reviews = db.relationship('ReviewDto', back_populates='users', lazy='dynamic')
    users = db.relationship('UserDto', back_populates='orders', lazy='dynamic')
    cheeses = db.relationship('CheeseDto', back_populates='orders', lazy='dynamic')

    def __init__(self, order_no, user_id, cheese_id, buy_count, total_price):
        self.order_no = order_no
        self.user_id = user_id
        self.cheese_id = cheese_id
        self.buy_count = buy_count
        self.total_price = total_price

    def __repr__(self):
        return f'User(order_no={self.order_no}, user_id={self.user_id}, \
                    cheese_id={self.cheese_id}, \
                    buy_count={self.buy_count}, total_price={self.total_price})'

    def __str__(self):
        return f'User(order_no={self.order_no}, user_id={self.user_id}, \
                    cheese_id={self.cheese_id}, \
                    buy_count={self.buy_count}, total_price={self.total_price})'

    @property
    def json(self):
        return {
            'order_no' : self.order_no,
            'user_id' : self.user_id,
            'cheese_id' : self.cheese_id,
            'buy_count' : self.buy_count,
            'total_price' : self.total_price,
            # 'count' : self.count
        }

# Json 형태로 쓰기 위해 씀!
class OrderVo():
    order_no: int = 0
    user_id: str = ''
    cheese_id: str = ''
    buy_count: int = 0
    total_price: int = 0

# # db.init_app(app)
# # with app.app_context():
# #     db.create_all()