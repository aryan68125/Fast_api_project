from fastapi import FastAPI
from fastapi.params import Body

#custom response structure import
from utility.common_response import response
from utility.dummy_data import my_blogs

#import pydantic model
from pydantic_custom_models.Blog import Blogs

app = FastAPI()

@app.get('/')
def root():
    return response(status=200,message="This api follows best practices")

@app.get("/blogs/")
def get_blogs():
    dummy_data = my_blogs
    return response(status=200,message="Post Sent!", data=dummy_data)

#post method implementation with pydantic model
@app.post("/blogs/")
def create_blog(Blog:Blogs):
    #Add the incoming data to the dummy data array
    my_blogs.append(Blog.dict())
    return response(status=201,message="Blog created!")