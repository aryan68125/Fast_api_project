from fastapi import FastAPI, status
from fastapi.params import Body

#custom response structure import
from utility.common_response import response
from utility.dummy_data import my_blogs

#import pydantic model
from pydantic_custom_models.Blog import Blogs

from random import randrange

app = FastAPI()

@app.get('/')
def root():
    return response(status=status.HTTP_200_OK,message="This api follows best practices")

@app.get("/blogs")
def get_blogs():
    dummy_data = my_blogs
    return response(status=status.HTTP_200_OK,message="Post Sent!", data=dummy_data)

#post method implementation with pydantic model
@app.post("/blogs")
def create_blog(Blog:Blogs):
    #Add the incoming data to the dummy data array
    blog_dict = Blog.dict()
    blog_dict['id'] = randrange(0,99999999)
    my_blogs.append(blog_dict)
    return response(status=status.HTTP_201_CREATED,message="Blog created!",data=blog_dict)

#get one blog from the dummy data
@app.get("/blogs/{id}")
def get_blog(id:int):
    print(type(id),id)
    # Create a dictionary keyed by blog IDs
    blogs_by_id = {blog["id"]: blog for blog in my_blogs}

    blog_id = id
    result = blogs_by_id.get(blog_id, False)
    if not result:
        return response(status=status.HTTP_404_NOT_FOUND,error="Blog not found!")
    return response(status=status.HTTP_200_OK,message="Blog sent!",data=result)

@app.delete('/blogs/{id}')
def delete_blog(id:int,status_code=status.HTTP_204_NO_CONTENT):
    blog_index = next((index for index,blog in enumerate(my_blogs) if blog['id']==id),None)
    if not blog_index:
        return response(status=status.HTTP_404_NOT_FOUND,error="Blog not found!")
    deleted_blog = my_blogs.pop(blog_index)
    return response(status=status.HTTP_204_NO_CONTENT)
    