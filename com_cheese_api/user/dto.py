from com_cheese_api.ext.db import db

'''
	    user_id	user_gender	user_age	cheese_code	cheese_name	            category	sub1_category  sub2_category	cheese_add_name	    cheese_brand	buy_price	buy_count
0	    2391853	M	        40	        114	        가고시마 현미흑초 720㎖	    건강식품	영양제	        기타영양제	        1개	                가고시마	      43000	        1
1	    1799897	F	        40	        114	        가고시마 현미흑초 720㎖	    건강식품	영양제	        기타영양제	        1개	                가고시마	      43000	        1
2	    1614947	F	        50	        189	        신가네여주농장 여주즙	    건강식품	건강진액	    채소즙	          1개	                신가네여주농장	  50000	        1
3	    1614947	F	        50	        189	        신가네여주농장 여주즙	    건강식품	건강진액	    채소즙	          1개	                신가네여주농장	  50000	        1
4	    1614947	F	        50	        804126	    새우볶음밥 270g	          냉동식품	    냉동간편식	    냉동밥	          5개	                천일냉동	     1990	       5
...	    ...	    ...	        ...	        ...	        ...	                    ...	        ...	            ...	            ...	                ...	...	...
36868	6159545	F	        30	        847511	    산지애 알뜰 못난이 사과 	과일	      국산과일	        사과	        1개	                  산지애	       39900	     1
36869	1942828	M	        40	        847554	    6년근 홍삼정환(丸) (160g) 건강식품	    홍삼/인삼가공식품	홍삼정/분말/환	상품명:동원천지인 	      천지인            46000	      1
36870	1942828	M	        40	        847554	    6년근 홍삼정환(丸) (160g) 건강식품	    홍삼/인삼가공식품	홍삼정/분말/환	상품명:동원천지인	      천지인            46000	      1
36871	6284056	M	        30	        847555	    글루코사민1500세트 	      건강식품	    영양제	        글루코사민	        2개             	대상웰라이프	    39000	      2
36872	1306045	F	        40	        847556	    아르젠또 발사믹 식초 	   건강식품	    영양제	        기타영양제	        1개	                두에 비토리에	     48000	        1

[36873 rows × 13 columns]

​

'''


class UserDto(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}


    user_id: str = db.Column(db.String(10), primary_key = True, index = True)
    #password: str = db.Column(db.String(1))
    #name: str = db.Column(db.String(100))
    user_gender: str = db.Column(db.String(10))
    user_age: int = db.Column(db.Integer)
    cheese_code: str = db.Column(db.String(100))
    cheese_name: str = db.Column(db.String(255))
    category: str = db.Column(db.string(100))
    sub1_category: str = db.Column(db.string(100))
    sub2_category: str = db.Column(db.string(100))
    cheese_add_name: str = db.Column(db.string(255))
    cheese_brand: str = db.Column(db.string(100))
    buy_price: int = db.Column(db.Integer)
    buy_count: int = db.Column(db.Integer)

    def __init__(self, user_id, user_gender, user_age, cheese_code, cheese_name, category, sub1_category, sub2_category, cheese_add_name, cheese_brand, buy_price, buy_count):
        self.user_id = user_id
        self.user_gender = user_gender
        self.user_age = user_age
        self.cheese_code = cheese_code
        self.cheese_name = cheese_name
        self.category = category
        self.sub1_category = sub1_category
        self.sub2_category = sub2_category
        self.cheese_add_name = cheese_add_name
        self.cheese_brand = cheese_brand
        self.buy_price = buy_price
        self.buy_count = buy_count

    def __repr__(self):
        return f'User(id={self.id}, user_id={self.user_id},\
            user_gender={self.password}, user_age={self.name}, cheese_code={self.cheese_code}, cheese_name={self.cheese_name}, category={self.category},\
            sub1_category={self.sub1_category}, sub2_category={self.sub2_category}, cheese_add_name={self.cheese_add_name}, cheese_brand={self.cheese_brand},\
            buy_price={self.buy_price}, buy_count={self.buy_count}'

    @property
    def json(self):
        return {
            'user_id' : self.user_id,
            'user_gender' : self.user_gender,
            'user_age' : self.user_age,
            'cheese_code' : self.cheese_code,
            'cheese_name' : self.cheese_name,
            'category' : self.category,
            'sub1_category' : self.sub1_category,
            'sub2_category' : self.sub2_category,
            'cheese_add_name' : self.cheese_add_name,
            'cheese_brand' : self.cheese_brand,
            'buy_price' : self.buy_price,
            'buy_count' : self.buy_count
        }

class UserVo:
    user_id : str = ''
    user_gender : str = ''
    user_age : int = 0
    cheese_code : str = ''
    cheese_name : str = ''
    category : str = ''
    sub1_category : str = ''
    sub2_category : str = ''
    cheese_add_name : str = ''
    cheese_brand : str = ''
    buy_price : int = 0
    buy_count : int = 0

