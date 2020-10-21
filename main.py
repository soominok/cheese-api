from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from com_cheese_api.ext.routes import initialize_routes
app = Flask(__name__)
CORS(app)
api = Api(app)
initialize_routes(api)