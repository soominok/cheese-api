from flask import request
from flask_restful import Resource, reqparse
from com_cheese_api.usr.user.model.user_dao import UserDao
from com_cheese_api.usr.user.model.user_dto import UserDto, UserVo

class SignUp(Resource):
    # self, user_id, password, name, gender, age, phone, email
    # @staticmethod
    # def post():
    #     """
    #     유저 정보를 받아와 새로운 유저를 생성해 준다.
    #     """
    #     print('====== user post 요청 받음 ======')
    #     print(f'[User Signup Resource Enter]')

    #     parser = reqparse.RequestParser() # only allow price changes, no name changes all allowed
    #     print(parser)
    #     # parser.add_argument('user_id', type=str, required=True,
    #     #                                 help='This field should be a user_id')
    #     # parser.add_argument('password', type=str, required=True,
    #     #                                 help='This field should be a password')
    #     # parser.add_argument('name', type=str, required=True,
    #     #                                 help='This field should be a name') 
    #     # parser.add_argument('gender', type=str, required=True,
    #     #                                 help='This field should be a gender')
    #     # parser.add_argument('age', type=int, required=True,
    #     #                                 help='This field should be a age')
    #     # parser.add_argument('phone', type=str, required=True,
    #     #                                 help='This field should be a phone')
    #     # parser.add_argument('email', type=str, required=True,
    #     #                                 help='This field should be a email')

    #     # parser.add_argument('user_id')
    #     # parser.add_argument('password')
    #     # parser.add_argument('name') 
    #     # parser.add_argument('gender')
    #     # parser.add_argument('age')
    #     # parser.add_argument('phone')
    #     # parser.add_argument('email')

    #     args = parser.parse_args()
    #     print('type(args): ', type(args))
    #     print('args: ', args)

    #     body = request.get_json()
    #     print('type(body): ', type(body))
    #     print('body: ', body)

    #     # print(f'====>> {body['user_id']}')

    #     # create 구현
    #     user = UserDto(**body)
    #     # user = UserDto(args.user_id, args.password, args.name, args.gender, 
    #     #                 args.age, args.phone, args.email)

    #     try:
    #         UserDao.register(user)
    #         return "worked"
    #     except Exception as e:
    #         return e
    #     # user_id = user.user_id


    #     print("====== user post 요청 받음 ======")
    #     parser = reqparse.RequestParser() # only allow price changes, no name changes all allowed
    #     parser.add_argument('user_id', type=str, required=True,
    #                                     help='This field should be a user_id')
    #     parser.add_argument('password', type=str, required=True,
    #                                     help='This field should be a password')
    #     parser.add_argument('name', type=str, required=True,
    #                                     help='This field should be a name') 
    #     parser.add_argument('gender', type=str, required=True,
    #                                     help='This field should be a gender')
    #     parser.add_argument('age', type=int, required=True,
    #                                     help='This field should be a age')
    #     parser.add_argument('phone', type=str, required=True,
    #                                     help='This field should be a phone')
    #     parser.add_argument('email', type=str, required=True,
    #                                     help='This field should be a email')

    #     args = parser.parse_args()
    #     print('type(args): ', type(args))
    #     print('args: ', args)

    #     user = UserDto(args.user_id, args.password, args.name, args.gender, 
    #                     args.age, args.phone, args.email)
    #     user = UserDto(args.user_id, args.password, args.name,
    #                     args.phone, args.email)
    #     print(f'user ==> {user}')
    #     print('아이디: ', user.user_id)
    #     print('비밀번호: ', user.password)
    #     print('이름: ', user.name)
    #     print('성별: ', user.gender)
    #     print('나이: ', user.age)
    #     print('핸드폰 번호: ', user.phone)
    #     print('이메일: ', user.email)
    #     try:
    #         UserDao.register(user)
    #         return "worked"
    #     except Exception as e:
    #         return e

    # @staticmethod
    # def post():
    #     print(f'[ User Signup Resource Enter ] ')
                                               

    #     parser = reqparse.RequestParser() # only allow price changes, no name changes all allowed
    #     print(parser)

    #     parser.add_argument('user')
    #     # print(f'user => {user}')

    #     # parser.add_argument('user.user_id')
    #     # print("2시작")
    #     # parser.add_argument('user.password')
    #     # print("3시작")
    #     # parser.add_argument('user.name')                                  
    #     # print("4시작")
    #     # parser.add_argument('user.gender')
    #     # print("5시작")                   
    #     # parser.add_argument('user.age')
    #     # print("8시작")                        
    #     # parser.add_argument('user.phone')
    #     # print("6시작")                                        
    #     # parser.add_argument('user.email')
    #     # print("7시작") 

    #     args = parser.parse_args()
    #     print(args)

    #     # print(f'password: {args.user_id}')
    #     # print(f'name: {args.user_id}')
    #     # print(f'gender: {args.user_id.gender}')
    #     # print(f'age: {args.user_id.age}')
    #     # print(f'phone: {args.user_id.phone}')
    #     # print(f'email: {args.user_id.email}')

    #     user = UserDto(args.user_id, args.password, args.name, args.gender, 
    #                     args.age, args.phone, args.email)

    #     print(f'[ ID ] {user.user_id}')
    #     data = UserDao.register(user)
    #     print(f'Login Result : {data}')
    #     return data.json(), 200


    @staticmethod
    def post():
        print(f'[ User Signup Resource Enter ] ')
        
        body = request.get_json()
        print('type(body): ', type(body))
        print('body: ', body)

        #  user = UserDto(args.user_id, args.password, args.name, args.gender, 
    #                     args.age, args.phone, args.email)
        user = UserDto(**body)
        print(f'[ user Dto ] {user}')

        # print(f'user ==> {user}')
        print('아이디: ', user.user_id)
        print('비밀번호: ', user.password)
        print('이름: ', user.name)
        print('성별: ', user.gender)
        print('나이: ', user.age)
        print('핸드폰 번호: ', user.phone)
        print('이메일: ', user.email)
        try:
            UserDao.register(user)
            return "worked"
        except Exception as e:
            return e

        # data = UserDao.register(user)
        # print(f'Login Result : {data}')
        # return data.json()

    # @staticmethod
    # def post():
    #     """
    #     유저 정보를 받아와 새로운 유저를 생성해 준다.
    #     """
    #     print("------------------여기는 user.py Auth ------------------- ")
    #     parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
        
    #     parser.add_argument('user_id', type=str, required=True,
    #                                     help='This field should be a user_id')
    #     parser.add_argument('password', type=str, required=True,
    #                                     help='This field should be a password')
    #     parser.add_argument('name', type=str, required=True,
    #                                     help='This field should be a name') 
    #     parser.add_argument('gender', type=str, required=True,
    #                                     help='This field should be a gender')
    #     parser.add_argument('age', type=int, required=True,
    #                                     help='This field should be a age')
    #     parser.add_argument('phone', type=str, required=True,
    #                                     help='This field should be a phone')
    #     parser.add_argument('email', type=str, required=True,
    #                                     help='This field should be a email')
    #     args = parser.parse_args()
    #     user = UserDto(args.usr_id, args.password, args.fname, args.lname,
    #                    args.age, args.gender, args.email)
    #     print("아이디: ", user.usr_id)
    #     print("비밀번호: ", user.password)
    #     print("이메일 :", user.email)
    #     print("성 :", user.lname)
    #     print("이름 :", user.fname)
    #     print("나이 :", user.age)
    #     print("성별 :", user.gender)
    #     try:
    #         UserDao.register(user)  # return 하긴 함
    #         return "worked"
    #     except Exception as e:
    #         return e