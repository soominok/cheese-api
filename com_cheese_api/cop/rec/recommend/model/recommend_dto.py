from com_cheese_api.usr.user.model.user_dto import UserDto
import numpy as np
import pandas as pd
from pathlib import Path
from com_cheese_api.ext.db import url, db, openSession, engine

import os
import json

class RecommendDto(db.Model):
    __tablename__ = 'recommends'
    __table_args__ = {'mysql_collate':'utf8_general_ci'}

    recommend_id: str = db.Column(db.String(20), primary_key=True, index=True)
    chooseFood_1: str = db.Column(db.String(100))
    chooseFood_2: str = db.Column(db.String(100))
    # user_id = db.Column(db.String(20), db.ForeignKey(UserDto.user_id)) # FK(user_id)
    user_id = db.Column(db.String(20))

    # orders = db.relationship('OrderDto', back_populates='user', lazy='dynamic')
    # cheeses = db.relationship('CheeseDto', back_populates='users', lazy='dynamic')
    # reviews = db.relationship('ReviewDto', back_populates='user', lazy='dynamic')
    
    # 관계 설정
    #reviews = db.relationship('ReviewDto', back_populates='users')

    def __init__(self, recommend_id, chooseFood_1, chooseFood_2, user_id):
        self.recommend_id = recommend_id
        self.chooseFood_1 = chooseFood_1
        self.chooseFood_2 = chooseFood_2
        self.user_id = user_id


    def __repr__(self):
        return f'recommend_id={self.recommend_id}, chooseFood_1={self.chooseFood_1}, chooseFood_2={self.chooseFood_2}, \
                    user_id = {self.user_id}'

    def __str__(self):
        return f'recommend_id={self.recommend_id}, chooseFood_1={self.chooseFood_1}, chooseFood_2={self.chooseFood_2}, \
                    user_id = {self.user_id}'

    #     def __repr__(self):
    #         return f'chooseFood_1={self.chooseFood_1}, chooseFood_2={self.chooseFood_2}, \
    #                 user_id = {self.user_id}'

    # def __str__(self):
    #     return f'chooseFood_1={self.chooseFood_1}, chooseFood_2={self.chooseFood_2}, \
    #                 user_id = {self.user_id}'

    @property
    def json(self):
        return {
            'recommend_id' : self.recommend_id,
            'chooseFood_1': self.chooseFood_1,
            'chooseFood_2': self.chooseFood_2,
            'user_id': self.user_id
        }

# Json 형태로 쓰기 위해 씀!
class RecommendVo():
    recommend_id: str = ''
    chooseFood_1: str = ''
    chooseFood_2: str = ''
    user_id: str = ''



# db.init_app(app)
# with app.app_context():
#     db.create_all()