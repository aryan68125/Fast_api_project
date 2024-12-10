from database_handler.database_connection import database_conn

def database_query_handler_fun(query:str):
    db_conn = None;
    try:
        db_conn = database_conn()
        print(f"db_conn : {db_conn}")
        cursor = db_conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(f"Database query error {e}")
    finally:
        if db_conn:
            db_conn.close()
            print(f"db_conn : {db_conn}")
