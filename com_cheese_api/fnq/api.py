from flask_restful import Resource, reqparse

class Fnq(Resource):
    def get(self):
        return {'message': 'Server Start'}