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
        print('====== access post 요청 받음 ======')
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
        # if data[0]:
        #     session['user'] = data[0]
        # print(session)

        # return json.dumps(data.json[0]), 200
        return data[0], 200


    def get(self):
        return {'message': 'Login API Start !!'}

    # @staticmethod
    # def delete(user_id):
    #     print('====== access delete 요청 받음 ======')
    #     print(session)
    #     session.pop('user', N)
        