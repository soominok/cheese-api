from flask import Flask
from flask_restful import Api
from com_cheese_api.ext.db import url, db, openSession
from com_cheese_api.ext.routes import initialize_routes

from com_cheese_api.usr.user.model.user_dfo import UserDfo
from com_cheese_api.usr.user.model.user_dao import UserDao
# from com_cheese_api.usr.user.model.user_dto import UserDto

from com_cheese_api.cop.ord.order.model.order_dfo import OrderDfo
from com_cheese_api.cop.ord.order.model.order_dao import OrderDao
# from com_cheese_api.cop.ord.order.model.order_dto import OrderDto

from com_cheese_api.cop.itm.cheese.model.cheese_dfo import CheeseDfo
from com_cheese_api.cop.itm.cheese.model.cheese_dao import CheeseDao
# from com_cheese_api.cop.itm.cheese.model.cheese_dto import cheeseDto

# from com_cheese_api.cop.rev.review.model.review_dto import ReviewDto
from com_cheese_api.cop.rev.review.model.review_dao import ReviewDao

from flask_cors import CORS


Session = openSession()
session = Session()


app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "*"}})


app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

api = Api(app)



# if __name__ == '__main__':
with app.app_context():

    db.create_all()

# ================================= User =================================
    user_count = UserDao.count()

    # print(f'USER TABLE CNT : {user_count[0]:10}')

    # print(f'===== Users Total Count is {user_count} =====')
    if user_count[0] == 0:
        UserDao.bulk()
    else:
        print("Users Data exists...")

    # user_all = UserDao.find_all()
    # print(f'insert 테스트!!')
    # print(f'===== Users Total Count is {user_all} =====')
    # UserDao.bulk()
    # user_all.bulk()


# ================================= Order =================================

    order_count = OrderDao.count()

    # print(f'==========Order Data Insert!!!==========')
    # print(f'===== Order Total Count is {order_count} =====')
    if order_count[0] == 0:
        OrderDao.bulk()
    else:
        print("Order data exists...")


# ================================= Cheese =================================
    cheese_count = CheeseDao.count()

    
    # cheese_id =
    # cheese_find_one = CheeseDao.find_by_cheese(cheese_id)
    # print(f'===== Cheese find one {cheese_find_one} =====')

    # cheese_all = CheeseDao.find_all()
    # print(f'========Cheese all {cheese_all} ==========')

    # print(f'==========Cheeses Data Insert!!!==========')
    # print(f'===== Cheeses Total Count is {cheese_count} =====')
    if cheese_count[0] == 0:
        CheeseDao.bulk()
    else:
        print("Cheeses Data exists...")


# ================================= Review =================================
#     print(f'==========Reviews Data Insert!!!==========')
#     # ReviewDao.bulk()


initialize_routes(api)

# print("========== main.py END ==========")



# dfo = CheeseDfo()
# cheese_df = dfo.cheese_df()
# df = dfo.cheese_data_refine(cheese_df)

# ================ CheeseDfo 테스트 ================
# dfo = CheeseDfo()
# print('\nwow!!!!!\n')
# df = dfo.new()
# print(f'치즈 Dfo 테스트\n\n', df.head(10))


# =================================================
# kdd = ReviewKdd()
# temp = kdd.crawling()
# kdd.save_csv(temp)

# dfo = ReviewDfo()
# review_data_frame = dfo.review_df()
# df = dfo.data_refine(review_data_frame)
# print("-------------------------------------")
# print(df.head(10))

    