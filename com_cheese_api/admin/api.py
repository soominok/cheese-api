from flask_restful import Resource, reqparse

class Admin(Resource):
    def get(self):
        return {'message': 'Server Start'}