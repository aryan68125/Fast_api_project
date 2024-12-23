from fastapi import FastAPI, status, Depends, APIRouter

#utilities
from utility.common_response import response
#import success messages from utility
from utility.common_success_messages import (
   DATA_SENT_SUCCESS , DATA_INSERT_SUCCESS, DATA_UPDATE_SUCCESS, DATA_SOFT_DELETE_SUCCESS, DATA_RESTORE_SUCCESS, DATA_HARD_DELETE_SUCCESS, OTP_VERIFICATION_SUCCESS, MAIL_SENT_SUCCESS, PASSWORD_RESET_SUCCESS
)
#import error messages from utility
from utility.common_error_messages import (
   DATA_SENT_ERR , DATA_INSERT_ERR, DATA_NOT_FOUND_ERR, DATA_UPDATE_ERR, DATA_SOFT_DELETE_ERR, DATA_RESTORE_ERR, DATA_HARD_DELETE_ERR, OTP_VERIFICATION_ERR, MAIL_SENT_ERR, USER_ACTIAVTED_ERR, PASSWORD_MATCH_ERR
)

#import sql alchemy model
from .. import sql_alchemy_models
#import sql alchemy database engine
from database_handler.sql_alchemy_db_handler import db_engine, SessionLocal, db_flush
#import session from sql alchemy
from sqlalchemy.orm import Session

#import query operation functions from sql alchemy
from sqlalchemy import desc

#make url parameters optional
from typing import Optional
#usae pydantic model to define the structure of the data that is to be inserted in the api end-point
from pydantic_custom_models.Posts import InsertPostsModel, UpdatePostsModel, SoftDeleteRestorePostsModel, RatingPostsModel



router = APIRouter(
    prefix="/posts",
    tags = ['Posts']
)

sql_alchemy_models.Base.metadata.create_all(bind=db_engine)

#Create a post
@router.post('/')
def create_post(post : InsertPostsModel,db : Session = Depends(db_flush)):
    new_post = sql_alchemy_models.posts_sql_alchemy_table(
        **post.model_dump()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    if not new_post:
        return response(status=status.HTTP_400_BAD_REQUEST,error=DATA_INSERT_ERR)
    return response(status=status.HTTP_201_CREATED,message=DATA_INSERT_SUCCESS,data=new_post)

#get all rows from the table using sql alchemy
from utility import OAuth2
@router.get('/',)
def get_all_posts(db:Session=Depends(db_flush),get_current_user : int = Depends(OAuth2.get_current_user)):
    print(f"Authenticated user: {get_current_user}")
    # This is gonna grab every single entry withing the posts_sql_alchemy_table
    # posts = db.query(sql_alchemy_models.posts_sql_alchemy_table).all()
    posts = db.query(sql_alchemy_models.posts_sql_alchemy_table).order_by(desc(sql_alchemy_models.posts_sql_alchemy_table.id)).all()
    if not len(posts):
        return response(status=status.HTTP_404_NOT_FOUND,error=DATA_NOT_FOUND_ERR)
    return response(status=status.HTTP_200_OK,message=DATA_SENT_SUCCESS,data=posts)

#get one row from the table using sql alchemy
@router.get('/{id}',)
def get_one_post(id:int, db: Session = Depends(db_flush)):
    post = db.query(sql_alchemy_models.posts_sql_alchemy_table).filter(sql_alchemy_models.posts_sql_alchemy_table.id == id).first()
    if not post:
        return response(status=status.HTTP_404_NOT_FOUND,error=DATA_NOT_FOUND_ERR)
    return response(status=status.HTTP_200_OK,message=DATA_SENT_SUCCESS,data=post)

#Update post
@router.patch('/{id}')
def update_post(id:int,postModel : UpdatePostsModel ,db: Session = Depends(db_flush)):
    post_query = db.query(sql_alchemy_models.posts_sql_alchemy_table).filter(sql_alchemy_models.posts_sql_alchemy_table.id == id)
    post = post_query.first()
    if not post:
         return response(status = status.HTTP_404_NOT_FOUND,error=DATA_NOT_FOUND_ERR)
    post_query.update(postModel.model_dump(), synchronize_session=False)
    db.commit()
    return response(status=status.HTTP_200_OK,message=DATA_UPDATE_SUCCESS,data=post_query.first())

# Update rating of a post
@router.patch('/rate-posts/{id}')
def rate_post(id:int, PostModel : RatingPostsModel,db:Session = Depends(db_flush)):
    post_query = db.query(sql_alchemy_models.posts_sql_alchemy_table).filter(sql_alchemy_models.posts_sql_alchemy_table.id == id)
    post = post_query.first()
    if not post:
         return response(status=status.HTTP_404_NOT_FOUND,error=DATA_NOT_FOUND_ERR)
    post_query.update(PostModel.model_dump(),synchronize_session=False)
    db.commit()
    return response(status=status.HTTP_200_OK,message=DATA_UPDATE_SUCCESS,data=post_query.first())

#Soft delete or restore posts
@router.patch('/soft-delete-or-restore/{id}')
def soft_delete_or_restore(id:int, PostModel : SoftDeleteRestorePostsModel, db : Session = Depends(db_flush)):
    post_query = db.query(sql_alchemy_models.posts_sql_alchemy_table).filter(sql_alchemy_models.posts_sql_alchemy_table.id == id)
    post = post_query.first()
    if not post:
         return response(status = status.HTTP_404_NOT_FOUND,error=DATA_NOT_FOUND_ERR)
    PostModelUpdated = PostModel.model_dump()
    PostModelUpdated['is_published'] = not PostModelUpdated.get('is_deleted')
    post_query.update(PostModelUpdated, synchronize_session=False)
    db.commit()
    if PostModel.is_deleted:
         return response(status=status.HTTP_200_OK,message=DATA_SOFT_DELETE_SUCCESS,data=post_query.first())
    return response(status=status.HTTP_200_OK,message=DATA_RESTORE_SUCCESS,data=post_query.first())

#Hard delete post
@router.delete('/{id}')
def hard_delete_post(id:int, db: Session = Depends(db_flush)):
    existing_post = db.query(sql_alchemy_models.posts_sql_alchemy_table).filter(
        sql_alchemy_models.posts_sql_alchemy_table.id == id
    )
    post_exists = existing_post.first()
    if not post_exists:
        return response(status=status.HTTP_404_NOT_FOUND,error=DATA_NOT_FOUND_ERR)
    existing_post.delete(synchronize_session=False)
    db.commit()
    return response(status=status.HTTP_200_OK,message=DATA_HARD_DELETE_SUCCESS)       
