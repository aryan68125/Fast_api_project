from fastapi import FastAPI, status

#utilities
from utility.common_response import response
#import success messages from utility
from utility.common_success_messages import (
   DATA_SENT_SUCCESS 
)
#import error messages from utility
from utility.common_error_messages import (
   DATA_SENT_ERR 
)

#Pydantic models 
from pydantic_custom_models import Posts

#import db handler 
from database_handler.database_connection import database_conn

app = FastAPI()

# call this function establish connection with the database
db_conn, cursor = database_conn()

@app.get('/')
def home():
    return response(status=status.HTTP_200_OK,message="This is a posts app homepage")

@app.get('/posts')
def get_posts():
    cursor.execute("""SELECT * FROM posts ORDER BY id ASC;""")
    data_rows = cursor.fetchall()
    print(data_rows)
    return response(status=status.HTTP_200_OK,message=DATA_SENT_SUCCESS,data=data_rows)

@app.get('/posts/database_function/')
def get_posts():
    cursor.execute("""SELECT * FROM posts ORDER BY id ASC;""")
    data_rows = cursor.fetchall()
    print(data_rows)
    return response(status=status.HTTP_200_OK,message=DATA_SENT_SUCCESS,data=data_rows)
