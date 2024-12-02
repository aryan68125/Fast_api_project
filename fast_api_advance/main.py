from fastapi import FastAPI
from fastapi.params import Body

#custom response structure import
from utility.common_response import response

#import the pydantic model
from pydantic_custom_models.Blog import Blogs

app = FastAPI()

@app.get("/")
def root():
    return response(status=200,message="Welcome to my api")

@app.get("/get-posts/")
def get_posts():
    dummy_data = [
        {"post_title 1":"this is post 1 body"},
        {"post_title 2":"this is post 2 body"},
        {"post_title 3":"this is post 3 body"}
    ]
    return response(status=200,message="Post Sent!", data=dummy_data)

#post method implementation without pydantic model
@app.post("/create-posts/")
def create_posts(data: dict = Body(...)):
    print(data)
    return response(status=201,message="Post Created!",data={"new_data":data})

#post method implementation with pydantic model
@app.post("/create-blog/")
def create_blog(Blog:Blogs):
    print(Blog) # print the entire data coming from the front-end
    print(Blog.updated_at) #extract and print the field from incoming data 
    return response(status=201,message="Blog created!")