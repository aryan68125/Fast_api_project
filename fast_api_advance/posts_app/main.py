from fastapi import FastAPI, status

#utilities
from utility.common_response import response
#import success messages from utility
from utility.common_success_messages import (
   DATA_SENT_SUCCESS , DATA_INSERT_SUCCESS, DATA_UPDATE_SUCCESS
)
#import error messages from utility
from utility.common_error_messages import (
   DATA_SENT_ERR , DATA_INSERT_ERR, DATA_NOT_FOUND_ERR, DATA_UPDATE_ERR
)

#Pydantic models 
from pydantic_custom_models.Posts import PostsModel

#import db handler for query management
from database_handler.database_query_handler import database_query_handler_fun

app = FastAPI()

#Insert data using database function written in PGAdmin using cursor
import json
@app.post('/posts')
def create_posts(post:PostsModel):
    post_dict = post.dict()
    title = post_dict.get('title')
    content = post_dict.get('content')
    is_published = post_dict.get('is_published')
    query = f"""SELECT insert_post('{title}', '{content}', {is_published})"""
    database_response = database_query_handler_fun(query)
    result_from_db = database_response.get('insert_post')
    if not result_from_db.get('status'):
        return response(status=status.HTTP_400_BAD_REQUEST,message=DATA_INSERT_ERR,error=result_from_db.get("db_message"))
    return response(status=status.HTTP_201_CREATED,message=DATA_INSERT_SUCCESS,data=result_from_db)

# Get data using database function written in pgAdmin using cursor
# OPTIMIZED WAY
# GET ALL RECORDS
@app.get('/posts')
def get_all_posts():
    query = """SELECT read_posts()"""
    data_rows = database_query_handler_fun(query)
    result_from_db = data_rows.get("read_posts")
    print(result_from_db.get('data'))
    if not result_from_db.get('data'):
        return response(status=status.HTTP_404_NOT_FOUND,message = DATA_NOT_FOUND_ERR,error=result_from_db.get("db_message"))
    return response(status=status.HTTP_200_OK, message=DATA_SENT_SUCCESS, data=data_rows)
#GET ONE RECORD
@app.get('/posts/{id}')
def get_one_post(id:int):
    query = f"""SELECT read_posts({id})"""
    data_row = database_query_handler_fun(query)
    result_from_db = data_row.get("read_posts")
    print(result_from_db.get('data'))
    if not result_from_db.get('data'):
        return response(status=status.HTTP_404_NOT_FOUND,message = DATA_NOT_FOUND_ERR,error=result_from_db.get("db_message"))
    return response(status=status.HTTP_200_OK, message=DATA_SENT_SUCCESS, data=data_row)

@app.patch('/posts/{id}')
def update_post(post: PostsModel):
    post_dict = post.dict()
    id = post_dict.get('id')
    title = post_dict.get('title')
    content = post_dict.get('content')
    is_published = post_dict.get('is_published')
    query = f"""SELECT update_post({id},'{title}','{content}',{is_published})"""
    database_response = database_query_handler_fun(query)
    result_from_db = database_response.get('update_post')
    if not result_from_db.get('status'):
        return response(status=status.HTTP_400_BAD_REQUEST,message=DATA_UPDATE_ERR,error=result_from_db.get("db_message"))
    return response(status=status.HTTP_200_OK,message=DATA_UPDATE_SUCCESS,data=result_from_db)