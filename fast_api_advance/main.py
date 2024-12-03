from fastapi import FastAPI
from fastapi.params import Body

#custom response structure import
from utility.common_response import response

#import pydantic model
from pydantic_custom_models.Blog import Blogs

app = FastAPI()

@app.get('/')
def root():
    return response(status=200,message="This api follows best practices")

@app.get("/blogs/")
def get_blogs():
    dummy_data = [
        {"post_title 1":"this is post 1 body"},
        {"post_title 2":"this is post 2 body"},
        {"post_title 3":"this is post 3 body"}
    ]
    return response(status=200,message="Post Sent!", data=dummy_data)

#post method implementation with pydantic model
@app.post("/blogs/")
def create_blog(Blog:Blogs):
    print(f"++++Printing Pydantic model : {Blog}") # print the entire data coming from the front-end
    print(f"----Extracting a field from a pydantic model : {Blog.updated_at}") #extract and print the field from incoming data 
    print(f">>>>Converting Pydantic model to Python dictionary : {Blog.dict()}") #converts a pydantic model into a python dictionary
    return response(status=201,message="Blog created!")