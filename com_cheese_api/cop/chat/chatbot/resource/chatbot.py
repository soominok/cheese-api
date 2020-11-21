from flask_restful import Resource, reqparse
from flask import request
from com_cheese_api.cop.itm.cheese.model.cheese_ai import CheeseAi
import json


class Chatbot(Resource):
    # @staticmethod
    # def post():
    #     print("들어옴")
    #     ai = CheeseAi()
    #     args = request.get_json()
    #     print(args)
    #     args = [args[i]['value'] for i in args.keys()]
    #     print(args)
    #     name = ai.train_actors(args)
    #     print(name)
    #     return name

    @staticmethod
    def load_model():
        print('=== load_model ===')
        