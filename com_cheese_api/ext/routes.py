from com_cheese_api.home.api import Home
from com_cheese_api.cheese.api import Cheese
from com_cheese_api.fnq.api import Fnq
from com_cheese_api.recommend.api import Recommend
from com_cheese_api.admin.api import Admin
from com_cheese_api.user.api import User

def initialize_routes(api):
    api.add_resource(Home, '/api')
    api.add_resource(Cheese, '/api/cheese')
    api.add_resource(Fnq, '/api/fnq')
    api.add_resource(Recommend, '/api/recommend')
    api.add_resource(Admin, '/api/admin')
    api.add_resource(User, '/api/user')