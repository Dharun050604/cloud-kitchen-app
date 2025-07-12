import mysql.connector
import os
import sys

__cnx = None

def get_sql_connection():
    global __cnx

    # Load environment variables
    db_host = os.environ.get("DB_HOST")
    db_port = os.environ.get("DB_PORT")
    db_user = os.environ.get("DB_USER")
    db_pass = os.environ.get("DB_PASS")
    db_name = os.environ.get("DB_NAME")

    # Debug prints (hide password)
    print(f"Connecting to DB with:")
    print(f"  HOST: {db_host}")
    print(f"  PORT: {db_port}")
    print(f"  USER: {db_user}")
    print(f"  NAME: {db_name}")

    # Check if any variable is missing
    missing = []
    if not db_host: missing.append("DB_HOST")
    if not db_port: missing.append("DB_PORT")
    if not db_user: missing.append("DB_USER")
    if not db_pass: missing.append("DB_PASS")
    if not db_name: missing.append("DB_NAME")

    if missing:
        print(f"❌ ERROR: Missing required environment variables: {', '.join(missing)}")
        sys.exit(1)

    # Convert port safely
    try:
        db_port = int(db_port)
    except ValueError:
        print(f"❌ ERROR: DB_PORT must be an integer. Got: {db_port}")
        sys.exit(1)

    # Connect if not already
    if __cnx is None:
        __cnx = mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_pass,
            database=db_name
        )

    return __cnx
