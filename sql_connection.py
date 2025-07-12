import mysql.connector
import os

__cnx = None

def get_sql_connection():
    global __cnx

    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_name = os.environ.get('DB_NAME')

    print("Connecting to DB with:")
    print("HOST:", db_host)
    print("PORT:", db_port)
    print("USER:", db_user)
    print("NAME:", db_name)

    if None in [db_host, db_port, db_user, db_pass, db_name]:
        raise Exception("Missing required environment variables")

    if __cnx is None:
        __cnx = mysql.connector.connect(
            host=db_host,
            port=int(db_port),
            user=db_user,
            password=db_pass,
            database=db_name
        )
    return __cnx
