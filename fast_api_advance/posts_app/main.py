from fastapi import FastAPI, status

#utilities
from utility.common_response import response

#Pydantic models 
from pydantic_custom_models import Posts

#import db handler 
from database_handler.database_connection import database_conn

app = FastAPI()

# call this function establish connection with the database
database_conn()

@app.get('/')
def home():
    return response(status=status.HTTP_200_OK,message="This is a posts app homepage")
