import MySQLdb
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_db_connection():
    conn = MySQLdb.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return conn
