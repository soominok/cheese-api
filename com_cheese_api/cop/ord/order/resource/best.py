from com_cheese_api.cop.ord.order.model.order_dto import OrderDto
from com_cheese_api.cop.ord.order.model.order_dao import OrderDao

import numpy as np
import pandas as pd
from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify
import json

class OrderBest(Resource):
        @staticmethod
        def get():
                print("SEARCH 진입")
                # print(f'성별: {gender}')
                # print(f'나이: {age}')
                # print(f'치즈 카테고리: {cheese_category}')
                # print(f'치즈 이름: {cheese_name}')
                best = OrderDao.find_cheese_by_gender_count()

                print(f'Best List : {best}')
                print(type(best))

                print(f'Best json : {jsonify(best)}')
                # itemList = []
                # for item in best:
                #         print(f'for문 결과: ', item)
                #         itemList.append(item)
                # print(f'Best List : {itemList}')
                # print(type(itemList))
                        
                
                # return jsonify([item.json for item in best])
                return jsonify(best)
                