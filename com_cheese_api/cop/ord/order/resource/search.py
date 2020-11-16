from com_cheese_api.cop.ord.order.model.order_dto import OrderDto
from com_cheese_api.cop.ord.order.model.order_dao import OrderDao

import numpy as np
import pandas as pd
from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify
import json


class OrderSearch(Resource):
        @staticmethod
        def get(user_id):
                print("SEARCH 진입")
                print(f'타이틀: {user_id}')
                order = OrderDao.find_by_id(user_id)
                
                orderlist = []
                for lis in order:
                        orderlist.append(lis)
                print(f'Review List : {orderlist}')
                return jsonify([item.json for item in orderlist])