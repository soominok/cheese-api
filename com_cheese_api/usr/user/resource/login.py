from flask_restful import Resource, reqparse
from com_cheese_api.usr.user.model.user_dao import UserDao 
from com_cheese_api.usr.user.model.user_dto import UserVo
import json
from flask import jsonify

parser = reqparse.RequestParser()

class Login(Resource):
    print(f'[ User Login Resource Enter ]')

    @staticmethod
    def post():
        parser.add_argument('user_id', type=str, required=True, 
                                help = 'This field should be a user_id')
        parser.add_argument('password', type=str, required=True,
                                help = 'This field should be a password')
        args = parser.parse_args()
        print(args)
        user = UserVo()
        # print(f'[ ID ] {args.user_id} \n [ Password ] {args.password}')
        user.user_id = args.user_id
        user.password = args.password

        print('아이디: ', user.user_id)
        print('비밀번호: ', user.password)

        data = UserDao.login(user)
        print(f'Login Result : {data}')

        return json.dumps([data.json]), 200
        # return data[0], 200


    def get(self):
        return {'message': 'Login API Start !!'}