from flask_restful import Resource, reqparse, fields, marshal_with
from com_cheese_api.cop.rev.review.model.review_dao import ReviewDao
from com_cheese_api.cop.rev.review.model.review_dto import ReviewDto, ReviewVo


'''
결과물 적어서 남겨놓기
'''

# 웹크롤링, 텍스트 마이닝 -> 데이터 마이닝

# 마일드 스톤(미국 도로보면 지역의 경계에 웰컴 어디어디 지역명 적어놓은것)
# ==============================================================
# ====================                     =====================
# ====================      Resourcing     =====================
# ====================                     =====================
# ==============================================================

review_fields = {
    'review_title': fields.String,
    'review_detail': fields.String,
    'user_id': fields.String,
    'item_id': fields.Integer
}

# API로 만드는 부분
class ReviewAPI(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
    
    @marshal_with(review_fields)
    def post(self):
        parser = self.parser
        # parser.add_argument('user_id', type=int, required=False, help='This field cannot be left blank')
        # parser.add_argument('item_id', type=int, required=False, help='This field cannot be left blank')
        # parser.add_argument('review_title', type=str, required=False, help='This field cannot be left blank')
        # parser.add_argument('review_detail', type=str, required=False, help='This field cannot be left blank')
        args = parser.parse_args()
        review = ReviewDto(args['review_title'], args['review_detail'],\
                            args['user_id'], args['item_id'])
        try:
            ReviewDao.save(review)
            return {'code' : 0, 'message' : 'SUCCESS'}, 200
        except:
            return {'message': 'An error occured inserting the review'}, 500

    @staticmethod
    def get(id):
        review = ReviewDao.find_by_id(id)
        if review:
            return review.json()
        return {'message': 'Review not found'}, 404

    @staticmethod
    def put(self, review, review_id):
        parser = self.parser
        parser.add_argument('review_id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('user_id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('item_id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('review_title', type=str, required=False, help='This field cannot be left blank')
        parser.add_argument('review_detail', type=str, required=False, help='This field cannot be left blank')
        args = parser.parse_args()
        review = ReviewVo()
        review.review_title = args['review_title']
        review.review_detail = args['review_detail']
        review.review_id = args['review_id']
        try:
            ReviewDao.update(review, review_id)
            return {'message': 'Review was Updated Successfully'}, 200
        except:
            return {'message': 'An Error Occured Updating the Review'}, 500


# 리뷰 리스트 
class ReviewsAPI(Resource):
    def get(self):
        return {'reivews': list(map(lambda review: review.json(), ReviewDao.find_all()))}