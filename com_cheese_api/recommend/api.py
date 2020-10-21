from flask_restful import Resource, reqparse

class Recommend(Resource):
    def get(self):
        return {'message': 'Server Start'}