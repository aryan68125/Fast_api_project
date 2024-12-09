import psycopg2
from decouple import config

'''
There is one thing that is weird with this library is that when you make a query to retrieve a bunch of rows from a database it doesn't include the column name, It just gives you the values of the column.
'''
# So that's why we have to import RealDictCursor from psycopg2 library
from psycopg2.extras import RealDictCursor

from utility.common_success_messages import (
    DATABASE_CONN_SUCCESS
)
from utility.common_error_messages import (
    DATABASE_CONN_ERR
)
import time

def database_conn():
    while True:
        try:
            db_conn = psycopg2.connect(
                    host=config('DB_IP'),
                    database=config('DB_NAME'),
                    user=config('DB_USERNAME'),
                    password=config('DB_PASSWORD'),
                    cursor_factory=RealDictCursor
                )
            cursor = db_conn.cursor()
            print("Database connection successful!")
            break
        except Exception as e:
            time.sleep(2)
            print(e)