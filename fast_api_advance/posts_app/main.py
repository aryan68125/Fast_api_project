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

#import db handler for query management
from database_handler.database_query_handler import database_query_handler_fun

app = FastAPI()

@app.get('/')
def home():
    return response(status=status.HTTP_200_OK,message="This is a posts app homepage")

# Get data using database function written in pgAdmin in cursor
# OPTIMIZED WAY
# GET ALL RECORDS
@app.get('/posts')
def get_all_posts():
    query = """SELECT read_posts()"""
    data_rows = database_query_handler_fun(query)
    return response(status=status.HTTP_200_OK, message=DATA_SENT_SUCCESS, data=data_rows)
#GET ONE RECORD
@app.get('/posts/{id}')
def get_one_post(id:int):
    query = f"""SELECT read_posts({id})"""
    data_row = database_query_handler_fun(query)
    return response(status=status.HTTP_200_OK, message=DATA_SENT_SUCCESS, data=data_row)