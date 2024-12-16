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
from pydantic_custom_models.Posts import InsertPostsModel, UpdatePostsModel, SoftDeleteRestorePostsModel, RatingPostsModel
from pydantic_custom_models.Users import CreateUpdateUserModel, BlockUnblockUsersModel, SoftDeleteRestoreUserModel

#import a utility that hashes user password
from utility.hash_password import hash_pass_fun

#Email related imports
from utility.send_mail import send_email_async, send_email_background
from fastapi import BackgroundTasks
from random import randint

app = FastAPI()

sql_alchemy_models.Base.metadata.create_all(bind=db_engine)

#Create a post
@app.post('/post')
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
def get_one_post(id:int, db: Session = Depends(db_flush)):
    post = db.query(sql_alchemy_models.posts_sql_alchemy_table).filter(sql_alchemy_models.posts_sql_alchemy_table.id == id).first()
    if not post:
        return response(status=status.HTTP_404_NOT_FOUND,error=DATA_NOT_FOUND_ERR)
    return response(status=status.HTTP_200_OK,message=DATA_SENT_SUCCESS,data=post)

#Update post
@app.patch('/posts/{id}')
def update_post(id:int,postModel : UpdatePostsModel ,db: Session = Depends(db_flush)):
    post_query = db.query(sql_alchemy_models.posts_sql_alchemy_table).filter(sql_alchemy_models.posts_sql_alchemy_table.id == id)
    post = post_query.first()
    if not post:
         return response(status = status.HTTP_404_NOT_FOUND,error=DATA_NOT_FOUND_ERR)
    post_query.update(postModel.model_dump(), synchronize_session=False)
    db.commit()
    return response(status=status.HTTP_200_OK,message=DATA_UPDATE_SUCCESS,data=post_query.first())

# Update rating of a post
@app.patch('/post/rate-posts/{id}')
def rate_post(id:int, PostModel : RatingPostsModel,db:Session = Depends(db_flush)):
    post_query = db.query(sql_alchemy_models.posts_sql_alchemy_table).filter(sql_alchemy_models.posts_sql_alchemy_table.id == id)
    post = post_query.first()
    if not post:
         return response(status=status.HTTP_404_NOT_FOUND,error=DATA_NOT_FOUND_ERR)
    post_query.update(PostModel.model_dump(),synchronize_session=False)
    db.commit()
    return response(status=status.HTTP_200_OK,message=DATA_UPDATE_SUCCESS,data=post_query.first())

#Soft delete or restore posts
@app.patch('/posts/soft-delete-or-restore/{id}')
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
@app.delete('/post/{id}')
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

#Create a user in a database table
@app.post('/users')
def create_users(userModel : CreateUpdateUserModel, background_tasks : BackgroundTasks, db : Session = Depends(db_flush)):
    try:
       # before we create the user we need to create the hash of the password
       #hash the use password
       hashed_pass_user_model = hash_pass_fun(userModel)
       #Now that the password is hashed we can create a new user
       new_user = sql_alchemy_models.UserMaster(**hashed_pass_user_model.model_dump())
       db.add(new_user)
       db.commit()
       db.refresh(new_user)
       if not new_user:
           return response(status=status.HTTP_400_BAD_REQUEST,error=DATA_INSERT_ERR)

       # Generate otp and save it in the user_master table in the record which is recently created.
       otp = randint(100000, 999999)
       recently_created_user = db.query(sql_alchemy_models.UserMaster).filter(sql_alchemy_models.UserMaster.id == new_user.id)
       #save otp in this newly created user
       recently_created_user.update({'account_activation_otp' : otp},synchronize_session=False)
       db.commit()

       title = 'Activate your account'
       name = new_user.email
       email_sent_to = new_user.email
       send_email_background(background_tasks, title,email_sent_to, {'title': title, 'name': name, 'otp':otp})
       response_data_dict = {
           'id':new_user.id,
           'email' : new_user.email,
           'is_blocked' : new_user.is_blocked,
           'is_deleted' : new_user.is_deleted,
           'created_at' : new_user.created_at
       }
       return response(status=status.HTTP_201_CREATED,message = DATA_INSERT_SUCCESS,data=response_data_dict)
    except Exception as e:
        print(e)
        return response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,error=e)
