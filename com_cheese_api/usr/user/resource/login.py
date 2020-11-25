from flask_restful import Resource, reqparse
from com_cheese_api.usr.user.model.user_dao import UserDao 
from com_cheese_api.usr.user.model.user_dto import UserVo
import json
from flask import jsonify, request



class Login(Resource):

    @staticmethod
    def post():
        print('====== access post 요청 받음 ======')
        parser = reqparse.RequestParser()
        print(f'parser ===> {parser}')

        parser.add_argument('user_id')
        parser.add_argument('password')

        args = parser.parse_args()
        print(f'args ===> {args}')

        print(f'*********>')

        user = UserVo()
        print(f'user : {user}')
        
        print(f'[ ID ] {args.user_id} \n [ Password ] {args.password}')
        user.user_id = args.user_id
        user.password = args.password

        user = UserVo()
        user.user_id = args.user_id
        user.password = args.password

        data = UserDao.login(user)
        return data[0], 200

    def get(self):
        return {'message': 'Login API Start !!'}, 200

    # @staticmethod
    # def delete(user_id):
    #     print('====== access delete 요청 받음 ======')
    #     print(session)
    #     session.pop('user', N)
        