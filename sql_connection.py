import os

def get_sql_connection():
    print("==== PRINTING ALL ENVIRONMENT VARIABLES ====", flush=True)
    for key, value in os.environ.items():
        print(f"{key} = {value}", flush=True)
    print("============================================", flush=True)

    # No actual DB connect, just dummy return for now
    return None
