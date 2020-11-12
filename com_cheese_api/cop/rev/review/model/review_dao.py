from com_cheese_api.cop.rev.review.model.review_dto import ReviewDto
from com_cheese_api.ext.db import db, openSession
# ==============================================================
# ====================                     =====================
# ====================       Modeling      =====================
# ====================                     =====================
# ==============================================================
# DB에 있는 데이터 가져오는 작업

Session = openSession()
session = Session()

class ReviewDao(ReviewDto):

    @classmethod
    def bulk(cls, review_dfo):
        dfo = review_dfo.create()
        print("리뷰 데이터 insert!!!")
        print(dfo.head())
        session.bulk_insert_mappings(cls, dfo.to_dict(orient="records"))
        session.commit()
        session.close()

    @staticmethod
    def save(review):
        Session = openSession()
        session = Session()
        session.add(review)
        session.commit()

    @staticmethod
    def update(review, review_id):
        Session = openSession()
        session = Session()
        session.query(ReviewDto).filter(ReviewDto.review_id == review.review_id)\
            .update({ReviewDto.review_title: review.review_title,
                        ReviewDto.review_detail: review.review_detail})
        session.commit()

    @classmethod
    def delete(cls, review_id):
        Session = openSession()
        session = Session()
        cls.query(ReviewDto.review_id == review_id).delete()
        session.commit()


    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filer_by(name == name).all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter(ReviewDto.review_id == id).one()


class ReviewTF():
    ...
    
class ReviewAi():
    ...