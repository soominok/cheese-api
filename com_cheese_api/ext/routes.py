import logging
from flask import Blueprint
from flask_restful import Api

from com_cheese_api.cmm.hom.home import Home
from com_cheese_api.usr.user.resource.login import Login
from com_cheese_api.usr.user.resource.user import User, Users
from com_cheese_api.cop.rev.review.model.review_dto import ReviewVo
from com_cheese_api.cop.rev.review.resource.review import ReviewAPI, ReviewsAPI
from com_cheese_api.cop.itm.cheese.resource.cheese import Cheeses

home = Blueprint('home', __name__, url_prefix='/api')

login_user = Blueprint('login_user', __name__, url_prefix='/api/login')
user = Blueprint('user', __name__, url_prefix='/api/user')
users = Blueprint('users', __name__, url_prefix='/api/users')

# cheese = Blueprint('cheese', __name__, url_prefix='/api/cheese')
cheeses = Blueprint('cheeses', __name__, url_prefix='/api/cheeses')

# review = Blueprint('review', __name__, url_prefix='/api/review')
# reviews = Blueprint('reviews', __name__, url_prefix='/api/reviews')


api = Api(home)
api = Api(login_user)
api = Api(user)
api = Api(users)
# api = Api(cheeses)

def initialize_routes(api):
    
    api.add_resource(Home, '/api')
    api.add_resource(Login, '/api/login')
    api.add_resource(User, '/api/user', '/api/user/<user_id>')
    # api.add_resource(User, '/api/user/<user_id>')
    api.add_resource(Users, '/api/users')
    # api.add_resource(Cheeses, '/api/cheeses')



@home.errorhandler(500)
def home_api_error(e):
    logging.exception('An error occurred during home request. %s' % str(e))
    return 'An internal error occurred.', 500

@user.errorhandler(500)
def user_api_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
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
