from fastapi import FastAPI, Depends

# Utility related imports
# import common response from utility
from utility.common_response import common_response
#importing common success message
from utility.common_success_message import (
    DATA_SENT,
    BLOG_CREATED,
)

#Model related imports
from blog.models import (
    BlogModel,
)
from database import engine
from sqlmodel import SQLModel,Session
import datetime

app = FastAPI()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def index():
    data = "This endpoint is the entry point for the apis in the intermediate section."
    return common_response(status_code=200,message=DATA_SENT,data=data)

@app.post("/blog/create-blog/")
def create_blog(blog: BlogModel, session: Session = Depends(get_session)):
    # Convert `created_at` to datetime if provided as a string
    if isinstance(blog.created_at, str):
        blog.created_at = datetime.datetime.fromisoformat(blog.created_at.replace("Z", "+00:00"))
    
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return common_response(status_code=201, message=BLOG_CREATED)