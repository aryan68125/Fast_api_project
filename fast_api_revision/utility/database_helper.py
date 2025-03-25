import psycopg2
from decouple import config

from psycopg2.extras import RealDictCursor

from message_helper import CommonErrorMessage, CommonSuccessMessages

import time

def database_connection_handler():
        try:
            db_conn = psycopg2.connect(
                    host=config('DB_IP'),
                    database=config('DB_NAME'),
                    user=config('DB_USERNAME'),
                    password=config('DB_PASSWORD'),
                    cursor_factory=RealDictCursor
                )
            # cursor = db_conn.cursor()
            print("Database connection successfull!")
            # return db_conn, 
            return db_conn
        except Exception as e:
            time.sleep(2)
            print(e)

def database_query_handler(query:str):
    db_conn = None;
    try:
         db_conn = database_connection_handler()
         print(f"db_connection = {db_conn}")
         cursor = db_conn.cursor()
         cursor.execute(query)
         result = cursor.fetchone()
         db_conn.commit()
         return result
    except Exception as e:
         print(f"Database query error : {db_conn}")
    finally:
         if db_conn:
              db_conn.close()
              print(f"database_connection : {db_conn}")