import logging
from flask import Blueprint
from flask_restful import Api

from com_cheese_api.cmm.hom.home import Home
from com_cheese_api.usr.user.resource.user import User, Users
from com_cheese_api.usr.user.resource.login import Login
from com_cheese_api.usr.user.resource.signup import SignUp

from com_cheese_api.cop.ord.order.resource.order import Order, Orders
from com_cheese_api.cop.ord.order.resource.search import OrderSearch
from com_cheese_api.cop.ord.order.resource.best import GenderBest, AgeBest
# from com_cheese_api.cop.ord.order.resource.best import OrderBest

from com_cheese_api.cop.rev.review.model.review_dto import ReviewVo
from com_cheese_api.cop.rev.review.resource.review import ReviewAPI, ReviewsAPI
from com_cheese_api.cop.itm.cheese.resource.cheese import Cheeses

############################## HOME ##############################
home = Blueprint('home', __name__, url_prefix='/api')

api = Api(home)


############################## USER ##############################
user = Blueprint('user', __name__, url_prefix='/api/user')
users = Blueprint('users', __name__, url_prefix='/api/users')
login = Blueprint('login', __name__, url_prefix='/api/login')
signup = Blueprint('signup', __name__, url_prefix='/api/signup')

api = Api(user)
api = Api(users)
api = Api(login)
api = Api(signup)

############################## ORDER ##############################
order = Blueprint('order', __name__, url_prefix='/api/order')
orders = Blueprint('orders', __name__, url_prefix='/api/orders')
search = Blueprint('search', __name__, url_prefix='/api/search')
# best = Blueprint('gender_best', __name__, url_prefix='/api/best')
gender_best = Blueprint('gender_best', __name__, url_prefix='/api/gender_best')
age_best = Blueprint('age_best', __name__, url_prefix='/api/age_best')

api = Api(order)
api = Api(orders)
api = Api(search)
# api = Api(best)
api = Api(gender_best)
api = Api(age_best)

############################## CHEESE ##############################
# cheese = Blueprint('cheese', __name__, url_prefix='/api/cheese')
# cheeses = Blueprint('cheeses', __name__, url_prefix='/api/cheeses')

# api = Api(cheeses)


############################## REVIEW ##############################
# review = Blueprint('review', __name__, url_prefix='/api/review')
# reviews = Blueprint('reviews', __name__, url_prefix='/api/reviews')


############################## CHATBOT ##############################
# chatbot = Blueprint('chatbot', __name__, url_prefix='/api/chatbot')

# api = Api(chatbot)


####################################################################





def initialize_routes(api):    
    api.add_resource(Home, '/api')

############################## USER ##############################    
    api.add_resource(User, '/api/user', '/api/user/<user_id>')
    api.add_resource(Users, '/api/users')
    api.add_resource(Login, '/api/login')
    api.add_resource(SignUp, '/api/signup')

############################## ORDER ##############################
    api.add_resource(Order, '/api/order/<user_id>')
    api.add_resource(Orders, '/api/orders')
    api.add_resource(OrderSearch, '/api/search/<user_id>')
    # api.add_resource(OrderBest, '/api/best')
    api.add_resource(GenderBest, '/api/gender_best')
    api.add_resource(AgeBest, '/api/age_best')


############################## CHEESE ##############################    
    # api.add_resource(Cheeses, '/api/cheeses')



@home.errorhandler(500)
def home_api_error(e):
    logging.exception('An error occurred during home request. %s' % str(e))
    return 'An internal error occurred.', 500

@user.errorhandler(500)
def user_api_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occurred.', 500

@user.errorhandler(500)
def login_api_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occurred.', 500

@user.errorhandler(500)
def auth_api_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occurred.', 500

@order.errorhandler(500)
def order_api_error(e):
    logging.exception('An error occurred during home request. %s' % str(e))
    return 'An internal error occurred.', 500

# @cheeses.errorhandler(500)
# def cheeses_api_error(e):
#     logging.exception('An error occurred during cheeses request. %s' % str(e))
#     return 'An internal error occurred.', 500



# ==============================================================
# ====================                     =====================
# ====================         TEST        =====================
# ====================                     =====================
# ==============================================================

# from com_cheese_api.home.api import HomeAPI
# from com_cheese_api.cheese.cheese_api import CheeseAPI
# from com_cheese_api.board.board_api import BoardAPI
# from com_cheese_api.suggest.suggest_api import SuggestAPI
# from com_cheese_api.admin.admin_api import AdminAPI
# from com_cheese_api.login.login_api import LoginAPI
# from com_cheese_api.login.sign_up_api import SignUpAPI


# def initialize_routes(api):
#     api.add_resource(HomeAPI, '/api')
#     api.add_resource(CheeseAPI, '/api/cheese')
#     api.add_resource(BoardAPI, '/api/board')
#     api.add_resource(SuggestAPI, '/api/suggest')
#     api.add_resource(AdminAPI, '/api/admin')
#     api.add_resource(LoginAPI, '/api/login')
#     api.add_resource(SignUpAPI, '/api/sign_up')
