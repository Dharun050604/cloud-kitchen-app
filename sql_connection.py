import mysql.connector
import os

__cnx = None

def get_sql_connection():
    global __cnx

    # DEBUG: Print all environment variables
    print("=== ENVIRONMENT VARIABLES DUMP ===")
    for key, value in os.environ.items():
        print(f"{key} = {value}")
    print("=== END DUMP ===")

    # Fetch expected variables
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_name = os.environ.get('DB_NAME')

    print("\nConnecting to DB with:")
    print(f"HOST: {db_host}")
    print(f"PORT: {db_port}")
    print(f"USER: {db_user}")
    print(f"NAME: {db_name}")

    # Check if any missing
    if None in [db_host, db_port, db_user, db_pass, db_name]:
        raise Exception("Missing required environment variables")

    # Establish connection
    if __cnx is None:
        __cnx = mysql.connector.connect(
            host=db_host,
            port=int(db_port),
            user=db_user,
            password=db_pass,
            database=db_name
        )
    return __cnx
