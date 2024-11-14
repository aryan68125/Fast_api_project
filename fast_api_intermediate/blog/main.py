from fastapi import FastAPI

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

app = FastAPI()

@app.get("/")
def index():
    data = "This endpoint is the entry point for the apis in the intermediate section."
    return common_response(status_code=200,message=DATA_SENT,data=data)

@app.post("/blog/create-blog/")
def create_blog(blog:BlogModel):
    print(f"Data from the front-end ---> {blog}")
    return common_response(status_code=201,message=BLOG_CREATED)