from flask_restful import Resource, reqparse

class Cheese(Resource):
    def get(self):
        return {'message': 'Server Start'}