from com_cheese_api.ext.db import db

'''

	    PD_C	PD_NM	                CLAC1_NM	CLAC2_NM            CLAC3_NM	CLNT_ID	HITS_SEQ	PD_ADD_NM	PD_BRA_NM	PD_BUY_AM	PD_BUY_CT	CLNT_GENDER	CLNT_AGE
0	    114	    가고시마 현미흑초 720㎖	    건강식품	영양제	             기타영양제	    2391853	146	1개	가고시마	43000	1	M	40
1	    114	    가고시마 현미흑초 720㎖	    건강식품	영양제	             기타영양제	    1799897	8	1개	가고시마	43000	1	F	40
2	    189	    신가네여주농장 여주즙 100ml  건강식품	건강진액	        채소즙	        1614947	117	1개	신가네여주농장	50000	1	F	50
3	    189	    신가네여주농장 여주즙 100ml  건강식품	건강진액	        채소즙	    1614947	27	1개	신가네여주농장	50000	1	F	50
4	    804126	새우볶음밥 270g	           냉동식품	   냉동간편식	        냉동밥	    1614947	251	5개	천일냉동	1990	5	F	50
...	    ...	...	...	...	...	...	...	...	...	...	...	...	...
36868	847511	산지애 알뜰 못난이 사과       과일        국산과일	            사과	    6159545	36	1개	산지애	39900	1	F	30
36869	847554	6년근 홍삼정환(丸) (160g)	건강식품	홍삼/인삼가공식품	홍삼정/분말/환	1942828	87	상품명:동원천지인 6년근 홍삼정환 (丸)|상품명:동원천지인 6년근 홍삼정환 (丸) ...	천지인	46000	1	M	40
36870	847554	6년근 홍삼정환(丸) (160g)	건강식품	홍삼/인삼가공식품	홍삼정/분말/환	1942828	197	상품명:동원천지인 6년근 홍삼정환 (丸)|상품명:동원천지인 6년근 홍삼정환 (丸) ...	천지인	46000	1	M	40
36871	847555	글루코사민1500세트      	건강식품	영양제	          글루코사민	  6284056	29	2개	대상웰라이프	39000	2	M	30
36872	847556	르젠또 발사믹 식초 포도퓨레   건강식품	  영양제	        기타영양제	    1306045	61	1개	두에 비토리에	48000	1	F	40
[36873 rows × 14 columns]

'''


class UserDto(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}


    CLNT_ID: str = db.Column(db.String(10), primary_key = True, index = True)
    #password: str = db.Column(db.String(1))
    #name: str = db.Column(db.String(100))
    PD_C: int = db.Column(db.Integer)
    PD_NM: str = db.Column(db.String(255))
    CLAC1_NM: str = db.Column(db.String(100))
    CLAC2_NM
    age_group: int = db.Column(db.Integer)
