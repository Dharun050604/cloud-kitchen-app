import mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(
            host='hopper.proxy.rlwy.net',
            port=29274,
            user='root',
            password='EXxXILiQvZRlAbUGuyxLvyHvpwFyzTiX',
            database='railway'
        )
    return __cnx
