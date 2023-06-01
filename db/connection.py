# 데이터베이스 사용 방법

# 1. Connection 맺기 (Python ===== DB)
#  - IP : 컴퓨터 주소
#  - Port : 27017
#  - ID & PW : 계정 정보
# 2. 명령 보내기      (Python ----→ DB)
# 3. 결과 받기        (Python ←---- DB)
# 4. Connection 끊기 (Python XXXXX DB)

# MongoDB 구조
#  - MongoDB(DBMS): 데이터베이스 관리 시스템
#   ㄴ DB(NAVER): 프로젝트 단위
#       ㄴ Collection - CRUD
#       ㄴ Collection(카페) - CRUD
#       ㄴ Collection(쇼핑) - CRUD
#       ㄴ Collection(메일) - CRUD
#   ㄴ DB(KAKAO)
#   ㄴ DB(BLOG)

# MongoDB 데이터 주고 받기
#  - BSON Type으로 데이터 주고 받음
#  - Bson(Binary JSON) = JSON과 거의 동일
#  - 그냥 JSON Type으로 사용하면 됨(문제 없음)
#  - Python에서 JSON은 Dict Type 사용!(Python Dict = JSON)

from pymongo import MongoClient


# MomgoDB Connection
def conn():
    #                    mongodb_web : ip + port + id&pw
    # Python-mongodb 연결 => client
    client = MongoClient("mongodb+srv://cnu:wldnr9620~@cluster0.xwp17zu.mongodb.net/") # IP, Port, ID&PW
    db = client["movie"]  # DB 선택

    collection = db.get_collection("movie")  # Collection 선택
    return collection
