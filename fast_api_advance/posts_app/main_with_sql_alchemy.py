from fastapi import FastAPI, status, Depends

#utilities
from utility.common_response import response
#import success messages from utility
from utility.common_success_messages import (
   DATA_SENT_SUCCESS , DATA_INSERT_SUCCESS, DATA_UPDATE_SUCCESS, DATA_SOFT_DELETE_SUCCESS, DATA_RESTORE_SUCCESS, DATA_HARD_DELETE_SUCCESS
)
#import error messages from utility
from utility.common_error_messages import (
   DATA_SENT_ERR , DATA_INSERT_ERR, DATA_NOT_FOUND_ERR, DATA_UPDATE_ERR, DATA_SOFT_DELETE_ERR, DATA_RESTORE_ERR, DATA_HARD_DELETE_ERR
)

#import sql alchemy model
from . import sql_alchemy_models
#import sql alchemy database engine
from database_handler.sql_alchemy_db_handler import db_engine, SessionLocal, db_flush
#import session from sql alchemy
from sqlalchemy.orm import Session

#import query operation functions from sql alchemy
from sqlalchemy import desc

#make url parameters optional
from typing import Optional
#usae pydantic model to define the structure of the data that is to be inserted in the api end-point
from pydantic_custom_models.Posts import InsertPostsModel

app = FastAPI()

sql_alchemy_models.Base.metadata.create_all(bind=db_engine)

#get all rows from the table using sql alchemy
@app.get('/posts',)
def get_all_posts(db:Session=Depends(db_flush)):
        # This is gonna grab every single entry withing the posts_sql_alchemy_table
        # posts = db.query(sql_alchemy_models.posts_sql_alchemy_table).all()
        posts = db.query(sql_alchemy_models.posts_sql_alchemy_table).order_by(desc(sql_alchemy_models.posts_sql_alchemy_table.id)).all()
        if not len(posts):
            return response(status=status.HTTP_404_NOT_FOUND,error=DATA_NOT_FOUND_ERR)
        return response(status=status.HTTP_200_OK,message=DATA_SENT_SUCCESS,data=posts)

#get one row from the table using sql alchemy
@app.get('/posts/{id}',)
def get_one_post(id:int,db: Session = Depends(db_flush)):
        post = db.query(sql_alchemy_models.posts_sql_alchemy_table).filter(sql_alchemy_models.posts_sql_alchemy_table.id == id).first()
        if not post:
            return response(status=status.HTTP_404_NOT_FOUND,error=DATA_NOT_FOUND_ERR)
        return response(status=status.HTTP_200_OK,message=DATA_SENT_SUCCESS,data=post)

@app.post('/post')
def create_post(post : InsertPostsModel,db : Session = Depends(db_flush)):
    new_post = sql_alchemy_models.posts_sql_alchemy_table(
        title=post.title,
        content=post.content,
        is_published=post.is_published
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    if not new_post:
        return response(status=status.HTTP_400_BAD_REQUEST,error=DATA_INSERT_ERR)
    return response(status=status.HTTP_201_CREATED,message=DATA_INSERT_SUCCESS,data=new_post)
