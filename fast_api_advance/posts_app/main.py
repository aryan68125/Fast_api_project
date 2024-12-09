from fastapi import FastAPI, status

#utilities
from utility.common_response import response

#Pydantic models 
from pydantic_custom_models import Posts

app = FastAPI()

@app.get('/')
def home():
    return response(status=status.HTTP_200_OK,message="This is a posts app homepage")
