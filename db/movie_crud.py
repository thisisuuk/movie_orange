# CDUD
#  - CREATE: 생성
#  - READ  : 조회
#  - UPDATE: 수정
#  - DELETE: 삭제

from db.connection import conn


# MongoBD에 리뷰 저장
def add_review(data):
    collection = conn()
    collection.insert_one(data)  # Review 저장

# MongoDB 리뷰 조회
def get_reviews():
    pass