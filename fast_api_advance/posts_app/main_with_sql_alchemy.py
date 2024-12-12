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

#Pydantic models 
# from pydantic_custom_models.Posts import (
#     InsertPostsModel, UpdatePostsModel, RatingPostsModel, SoftDeleteRestorePostsModel, HardDeletePostsModel
# )

#import sql alchemy model
from . import sql_alchemy_models
#import sql alchemy database engine
from database_handler.sql_alchemy_db_handler import db_engine, SessionLocal, db_flush
#import session from sql alchemy
from sqlalchemy.orm import Session

app = FastAPI()

sql_alchemy_models.Base.metadata.create_all(bind=db_engine)

@app.get('/posts/{id}')
def get_one_or_all_posts(db : Session = Depends(db_flush)):
    # This is gonna grab every single entry withing the posts_sql_alchemy_table
    posts = db.query(sql_alchemy_models.posts_sql_alchemy_table).all()
    return response(status=status.HTTP_200_OK,message=DATA_SENT_SUCCESS,data=posts)
