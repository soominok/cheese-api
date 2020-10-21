from com_cheese_api.home.api import Home

def initialize_routes(api):
    api.add_resource(Home, '/api')