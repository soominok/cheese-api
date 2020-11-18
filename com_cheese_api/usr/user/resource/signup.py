from flask_restful import Resource, reqparse
from com_cheese_api.usr.user.model.user_dao import UserDao
from com_cheese_api.usr.user.model.user_dto import UserDto

class SignUp(Resource):
    # self, user_id, password, name, gender, age, phone, email
    @staticmethod
    def post():
        """
        유저 정보를 받아와 새로운 유저를 생성해 준다.
        """
        print("-------- 여기는 user.py Auth --------")
        parser = reqparse.RequestParser() # only allow price changes, no name changes all allowed
        parser.add_argument('user_id', type=str, required=True,
                                        help='This field should be a user_id')
        parser.add_argument('password', type=str, required=True,
                                        help='This field should be a password')
        parser.add_argument('name', type=str, required=True,
                                        help='This field should be a name') 
        parser.add_argument('gender', type=str, required=True,
                                        help='This field should be a gender')
        # parser.add_argument('age', type=int, required=True,
        #                                 help='This field should be a age')
        parser.add_argument('phone', type=str, required=True,
                                        help='This field should be a phone')
        parser.add_argument('email', type=str, required=True,
                                        help='This field should be a email')
        args = parser.parse_args()
        user = UserDto(args.user_id, args.password, args.name, args.gender, 
                        args.age, args.phone, args.email)

        print('아이디: ', user.user_id)
        print('비밀번호: ', user.password)
        print('이름: ', user.name)
        # print('성별: ', user.gender)
        print('나이: ', user.age)
        print('핸드폰 번호: ', user.phone)
        print('이메일: ', user.email)
        try:
            UserDao.register(user)
            return "worked"
        except Exception as e:
            return e