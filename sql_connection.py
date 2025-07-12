import os
import mysql.connector

def get_sql_connection():
    connection = mysql.connector.connect(
        host=os.environ.get('MYSQLHOST'),
        user=os.environ.get('MYSQLUSER'),
        password=os.environ.get('MYSQLPASSWORD'),
        database=os.environ.get('MYSQLDATABASE'),
        port=int(os.environ.get('MYSQLPORT', 3306))
    )
    print("✅ Successfully connected to DB!")
    return connection
