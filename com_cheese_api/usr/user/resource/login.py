from flask_restful import Resource, reqparse
from com_cheese_api.usr.user.model.user_dao import UserDao 
from com_cheese_api.usr.user.model.user_dto import UserVo

parser = reqparse.RequestParser()

class LoginAPI(Resource):
    print(f'[ User Login Resource Enter ]')

    @staticmethod
    def post():
        parser.add_argument('user_id')
        parser.add_argument('password')
        args = parser.parse_args()

        user = UserVo()
        print(f'[ ID ] {args.user_id} \n [ Password ] {args.password}')
        user.user_id = args.userId
        user.password = args.password
        data = UserDao.login(user)
        print(f'Login Result : {data}')

        return data.json(), 200


    def get(self):
        return {'message': 'Login API Start !!'}