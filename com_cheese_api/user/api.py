from flask_restful import Resource, reqparse

class User(Resource):
    def get(self):
        return {'message': 'Server Start'}