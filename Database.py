import pymysql
from local_config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def connection():
    con = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset="utf8"
    )
    return con