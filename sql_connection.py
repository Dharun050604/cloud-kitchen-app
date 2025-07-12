import os
import mysql.connector

def get_sql_connection():
    print("========== DB ENV CHECK ==========", flush=True)
    print("MYSQLHOST =", os.environ.get("MYSQLHOST"), flush=True)
    print("MYSQLUSER =", os.environ.get("MYSQLUSER"), flush=True)
    print("MYSQLPASSWORD =", os.environ.get("MYSQLPASSWORD"), flush=True)
    print("MYSQLDATABASE =", os.environ.get("MYSQLDATABASE"), flush=True)
    print("MYSQLPORT =", os.environ.get("MYSQLPORT"), flush=True)
    print("===================================", flush=True)

    connection = mysql.connector.connect(
        host=os.environ.get('MYSQLHOST'),
        user=os.environ.get('MYSQLUSER'),
        password=os.environ.get('MYSQLPASSWORD'),
        database=os.environ.get('MYSQLDATABASE'),
        port=int(os.environ.get('MYSQLPORT', 3306))
    )
    print("✅ Connected to DB!", flush=True)
    return connection
