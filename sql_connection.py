import mysql.connector
import os
import sys

__cnx = None

def get_sql_connection():
    global __cnx

    # Fetch expected variables
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_name = os.environ.get('DB_NAME')

    print("Connecting to DB with:", flush=True)
    print(f"HOST: {db_host}", flush=True)
    print(f"PORT: {db_port}", flush=True)
    print(f"USER: {db_user}", flush=True)
    print(f"NAME: {db_name}", flush=True)

    # Debug: dump all env keys to verify what's actually there
    print("\n--- ALL ENV KEYS ---", flush=True)
    for key in os.environ.keys():
        print(key, flush=True)
    print("--- END ENV KEYS ---\n", flush=True)

    # Check if any are missing
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
