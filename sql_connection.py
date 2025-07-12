import os
import mysql.connector

def get_sql_connection():
    print("========== DB ENV CHECK ==========", flush=True)
    MYSQLHOST = os.environ.get("DB_HOST")
    MYSQLUSER = os.environ.get("DB_USER")
    MYSQLPASSWORD = os.environ.get("DB_PASS")
    MYSQLDATABASE = os.environ.get("DB_NAME")
    MYSQLPORT = int(os.environ.get("DB_PORT", 3306))
    print(f"MYSQLHOST = {MYSQLHOST}", flush=True)
    print(f"MYSQLUSER = {MYSQLUSER}", flush=True)
    print(f"MYSQLPASSWORD = {MYSQLPASSWORD}", flush=True)
    print(f"MYSQLDATABASE = {MYSQLDATABASE}", flush=True)
    print(f"MYSQLPORT = {MYSQLPORT}", flush=True)
    print("===================================", flush=True)

    connection = mysql.connector.connect(
        host=MYSQLHOST,
        user=MYSQLUSER,
        password=MYSQLPASSWORD,
        database=MYSQLDATABASE,
        port=MYSQLPORT
    )
    return connection
