from fastapi import FastAPI, status, Depends

# for sending in custom response
from utility.response_helper import CommonResponse

# for common error and success messages
from utility.message_helper import CommonErrorMessage, CommonSuccessMessages

#for database connection 
# from utility.database_helper import database_conn

# sql alchemy database helper 
from models.alchemy_model import blog
from utility.sql_alchemy import db_engine
from sqlmodel import SQLModel, Session
import datetime

#instance of fast api
app = FastAPI()

def create_db_and_tables():
    SQLModel.metadata.create_all(db_engine)

def get_db_session():
    with Session(db_engine) as session:
        yield session

@app.post("blog/")
def create_blog(pydantic_model: BlogModel, db: Session = Depends(get_session)):
    # Convert `created_at` to datetime if provided as a string
    if isinstance(blog.created_at, str):
        blog.created_at = datetime.datetime.fromisoformat(blog.created_at.replace("Z", "+00:00"))
    
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return CommonResponse(status_code=201, message=BLOG_CREATED)