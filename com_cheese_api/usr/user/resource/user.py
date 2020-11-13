#from com_cheese_api.usr.model.user_dto import UserDto
#from com_cheese_api.usr.model.user_dao import UserDao
from com_cheese_api.usr.user.model.user_dto import UserDto
from com_cheese_api.usr.user.model.user_dao import UserDao

#from com_cheese_api.util.file import FileReader
from com_cheese_api.cmm.utl.file import FileReader

import numpy as np
import pandas as pd
from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify
import json
# from pathlib import Path
# from com_cheese_api.ext.db import url, db, openSession, engine
# from konlpy.tag import Okt
# from collections import Counter
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
# import seaborn as sns
# from sqlalchemy import func
# from sqlalchemy.ext.declarative import declarative_base
from com_cheese_api.usr.user.model.user_dao import UserDao
from com_cheese_api.usr.user.model.user_dto import UserDto

import os
import json

'''
json = json.loads() => dict
dict = json.dumps() => json
'''

'''
서버와 정보를 주고 받는다.
'''

parser = reqparse.RequestParser() 

class User(Resource):

    @staticmethod
    def post():
        print(f'[User Signup Resource Enter]')
        body = request.get_json()
        user = UserDto(**body)
        UserDao.save(user)
        user_id = user.user_id

        return {'user_id': str(user_id)}, 200

    @staticmethod
    def get(user_id: str):
        """
        유저 아이디를 받아와 해당 유저 객채를 리턴한다
        Parameter: User ID 를 받아온다
        return: 해당 아이디 유저 객체
        """
        print('===========user_id=============')
        print(user_id)
        try:
            print(f'User ID is {user_id}')
            user = UserDao.find_by_id(user_id)
            
            if user:
                return jsonify([user.json])
        except Exception as e:
            print(e)
            return {'message': 'User not found'}, 404


    @staticmethod
    def put(user_id: str):
        """
        서버에서 해당 ID 의 새로운 유저 정보를 받아온다.
        정보를 토대로 해당 ID 유저의 정보를 바꿔서
        정보를 서버에 보내준다.
        parameter: 유저 아이디를 받아온다
        return: 새로운 유저 데이터를 리턴 한다
        """
        parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
        parser.add_argument('user_id', type=str, required=True,
                                                help='This field should be a user_id')
        parser.add_argument('password', type=str, required=True,
                                                help='This field should be a password')
        parser.add_argument('gender', type=str, required=True,
                                                help='This field should be a gender')
        parser.add_argument('age_group', type=str, required=True,
                                                help='This field should be a age_group')

        print("argument added")
        # def __init__(self, user_id, password,fname, lname, age, gender,email):
        args = parser.parse_args()
        print(f'User {args["user_id"]} updated')
        print(f'User {args["password"]} updated')
        user = UserDto(args.user_id, args.password, args.gender, args.age_group,)
        print("user created")
        UserDao.update(user)
        data = user.json()
        return data, 200

    @staticmethod
    def delete(user_id: str):
        """
        유저 아이디를 받아와 해당 유저를 삭제한다.
        Parameter: 유저 아이디
        """
        # UserDao.delete(id)
        # print(f'User {id} Deleted')
        print(f'[ User Delete Resource Enter ]')
        args = parser.parse_args()
        print(f'User {args["user_id"]} deleted')
        return {'code': 0, 'message': 'SUCCESS'}, 200

    # @staticmethod
    # def get(user_id: str):
    #     """
    #     유저 아이디를 받아와 해당 유저 객채를 리턴한다
    #     Parameter: User ID 를 받아온다
    #     return: 해당 아이디 유저 객체
    #     """
    #     print('===========user_id=============')
    #     print(user_id)
    #     try:
    #         print(f'User ID is {user_id}')
    #         user = UserDao.find_by_id(user_id)
            
    #         if user:
    #             return json.dumps(user.json()), 200
    #     except Exception as e:
    #         print(e)
    #         return {'message': 'User not found'}, 404

    # @staticmethod
    # def get(user_id: str):
    #     """
    #     유저 아이디를 받아와 해당 유저 객채를 리턴한다
    #     Parameter: User ID 를 받아온다
    #     return: 해당 아이디 유저 객체
    #     """
    #     print('===========user_id=============')
    #     print(user_id)
    #     try:
    #         print(f'User ID is {user_id}')
    #         user = UserDao.find_one(user_id)
    #         if user:
    #             data = []
    #             data.append()
    #             return jsonify([item.json for item in data]), 200
    #     except Exception as e:
    #         print(e)
    #         return {'message': 'User not found'}, 404

    # def get(self):
    #     """
    #     유저 아이디를 받아와 해당 유저 객채를 리턴한다
    #     Parameter: User ID 를 받아온다
    #     return: 해당 아이디 유저 객체
    #     """
    #     result = self.dao.find_one(user_id)
    #     return jsonify([item.json for item in result])

    # @staticmethod
    # def get(user_id: str):
    #     """
    #     유저 아이디를 받아와 해당 유저 객채를 리턴한다
    #     Parameter: User ID 를 받아온다
    #     return: 해당 아이디 유저 객채
    #     """
    #     print(f'::::::::::::: User {user_id} added ')
    #     try:
    #         user = UserDao.find_by_id(user_id)
    #         data = user.json()
    #         return data, 200
    #     except Exception as e:
    #         print(e)
    #         return {'message': 'User not found'}, 404

    # @staticmethod
    # def put():
    #     print(f'[User Put Resource Enter]')
    #     parser.add_argument('userId')
    #     parser.add_argument('password')
    #     parser.add_argument('gender')
    #     parser.add_argument('age_group')
    #     args = parser.parse_args()
    #     UserDao.update(args)
    #     user = UserDao.find_by_id(args.userId)
    #     if args.password == user.password and \
    #         args.

class Users(Resource):

    @staticmethod
    def post():
        print(f'[ User Bulk Resource Enter ]')
        UserDao.bulk()

    @staticmethod
    def get():
        print(f'[ User List Resource Enter ]')
        data = UserDao.find_all()
        return jsonify([item.json for item in data])
        # return json.dumps(jsonify([item.json for item in data])), 200

    # def get():
    #     print(f'[ User List Resource Enter ]')
    #     data = UserDao.find_all()
    #     return json.dumps(data), 200
