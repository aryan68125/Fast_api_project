from fastapi import FastAPI, status, Depends


#import sql alchemy model
from . import sql_alchemy_models
#import sql alchemy database engine
from database_handler.sql_alchemy_db_handler import db_engine, SessionLocal, db_flush
#import session from sql alchemy
from sqlalchemy.orm import Session


#import routers
from .routers import posts, users, auth

app = FastAPI()

#routes that handles all the posts
app.include_router(posts.router)
#routes that handles all the users
app.include_router(users.router)
#routes that handles all user authentications
app.include_router(auth.router)

sql_alchemy_models.Base.metadata.create_all(bind=db_engine)