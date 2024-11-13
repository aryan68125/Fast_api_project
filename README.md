# Fast_api_project
This repo holds the fast api project for learning purposes
## Installation
Create a virtual environment <br>
```
virtualenv venv
```
Activate your virtual environment <br>
```
source venv/bin/activate
```
Install Fast api <br>
```
pip3 install fastapi
```
OR you can run the command below to install Fastapi in your system <br>
```
pip3 install fastapi
```
Install the server for fastapi <br>
```
pip install uvicorn
```
## Sample code in FastAPI
The code below is a sample code of FastAPI.
```
from fastapi import FastAPI
#import common_respone 
from common_response import common_response 
#import success message from common success message file
from common_success_message import (
    DATA_SENT
)

app = FastAPI()

@app.get("/")
def index():
    data = "Well hello there"
    return common_response(status_code=200,message=DATA_SENT,data=data)

@app.get("/about")
def about():
    data = "This Api is created by Aditya Kumar"
    return common_response(status_code=200,message=DATA_SENT,data=data)
```
### Explaination of the above code is as follows
#### Imports and FastAPI Initialization <br>
```
from fastapi import FastAPI 
```
<br>

- Explanation: FastAPI is a modern Python web framework that allows you to build APIs quickly and easily. It's designed to work seamlessly with asynchronous programming and type hints, and it has built-in support for features like request validation and automatic documentation generation.
- Purpose of from fastapi import FastAPI: This line imports the FastAPI class from the FastAPI library, which is used to create an instance of the FastAPI application. This instance is needed to register routes, handle requests, and define the overall structure of the API.

<br>

#### Creating an Instance of FastAPI

```
app = FastAPI()
```

<br>

- Explanation: This line creates an instance of the FastAPI application. Here, app is the instance of FastAPI, which represents the web application and handles all incoming requests and outgoing responses.
- Purpose: The app object allows you to add routes, middlewares, and other configuration settings for your FastAPI application. Once instantiated, it can register route handlers for different HTTP methods and endpoints.

#### Defining the index Route

<br>

```
@app.get("/")
def index():
    data = "Well hello there"
    return common_response(status_code=200, message=DATA_SENT, data=data)
```

<br>

Explanation of @app.get("/"):
- @app.get("/") is a decorator that registers this function (index) as a handler for GET requests to the / route.
- In FastAPI, decorators like @app.get, @app.post, etc., allow you to bind specific routes (URLs) to specific HTTP methods (GET, POST, etc.). This lets the server know which function to call when a request is made to a specific endpoint.
- Here, @app.get("/") binds the index function to the root URL /, so when a client sends a GET request to http://localhost:8000/, this function will be called.

Explanation of the index function:
- This function initializes a data variable with the string "Well hello there".
- It then calls the common_response function, passing status_code=200 (indicating success), message=DATA_SENT (the standardized success message from common_success_message.py), and data=data (the actual data to send as part of the response).
- Purpose: This endpoint sends a "Hello" message as data along with a standardized success response when accessed.

## NOTE:
FastAPI executes the functions sequentially and so we have to be carefull what functions to execute and when
```
from fastapi import FastAPI
#import common_respone 
from common_response import common_response 
#import success message from common success message file
from common_success_message import (
    DATA_SENT
)

app = FastAPI()

@app.get("/")
def index():
    data = "This endpoint is the entry point for the apis"
    return common_response(status_code=200,message=DATA_SENT,data=data)

@app.get("/about")
def about():
    data = "This Api is created by Aditya Kumar"
    return common_response(status_code=200,message=DATA_SENT,data=data)

@app.get("/blog/blog-list/")
def blog_list():
    data = [
        {"author":"Aditya Kumar","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
        {"author":"Aastha Rajpurohit","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
        {"author":"Vaibhav Tailor","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
        {"author":"Neha Sharma","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
    ]
    return common_response(status_code=200,message=DATA_SENT,data=data)

@app.get("/blog/blog-unpublished/")
def unpublished_blogs():
    data = [
        {"author":"Aastha Rajpurohit","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":"","status":"Unpublished"},
        {"author":"Neha Sharma","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":"","status":"Unpublished"},
    ]
    return common_response(status_code=200,message=DATA_SENT,data=data)

@app.get("/blog/blog-detail/{blog_id}")
def blog_detail(blog_id):
    try:
        data_list = [
            {"author":"Aditya Kumar","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
            {"author":"Aastha Rajpurohit","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
            {"author":"Vaibhav Tailor","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
            {"author":"Neha Sharma","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
        ]
        print(blog_id)
        data = data_list[int(blog_id)]
        return common_response(status_code=200,message=DATA_SENT,data=data)
    except Exception as e:
        return common_response(status_code=400,error=str(e))

@app.get("/blog/blog-detail/{blog_id}/comments/")
def blog_comments(blog_id : int):
    try:
        data_list = [
            {"author":"Aditya Kumar","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
            {"author":"Aastha Rajpurohit","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
            {"author":"Vaibhav Tailor","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
            {"author":"Neha Sharma","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
        ]
        print(blog_id)
        data = data_list[blog_id]
        return common_response(status_code=200,message=DATA_SENT,data=data)
    except Exception as e:
        return common_response(status_code=400,error=str(e))
```

If suppose I write the function in order like this
```
@app.get("/blog/blog-detail/{blog_id}")
def blog_detail(blog_id:int):
    try:
        data_list = [
            {"author":"Aditya Kumar","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
            {"author":"Aastha Rajpurohit","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
            {"author":"Vaibhav Tailor","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
            {"author":"Neha Sharma","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
        ]
        print(blog_id)
        data = data_list[int(blog_id)]
        return common_response(status_code=200,message=DATA_SENT,data=data)
    except Exception as e:
        return common_response(status_code=400,error=str(e))

@app.get("/blog/blog-unpublished/")
def unpublished_blogs():
    data = [
        {"author":"Aastha Rajpurohit","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":"","status":"Unpublished"},
        {"author":"Neha Sharma","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":"","status":"Unpublished"},
    ]
    return common_response(status_code=200,message=DATA_SENT,data=data)
```
Then in this case FastAPI will throw and error saying that the blog_id is of the wrong type because instead of an integer as in this url path ``` /blog/blog-detail/{blog_id} ``` We are trying to go into this url path ``` /blog/blog-unpublished/ ```. Which should be a valid url path but since FastAPI matches the url sequentially one by one from top to bottom.

<br>

**Note** : We need to put all the dynamic routes must come after all the static routes are written

## query parameter in fastAPI
The example of how a query parameter may look like 

<br>

```
http://127.0.0.1:8000/items/?skip=0&limit=10
```
In order for query parameter to be able to make changes in the back-end we need to accept the query parameter in our function just like what we did in dynamic urls as shown below:
Sample code of how to accept blog_id in dynamic url
```
@app.get("/blog/blog-detail/{blog_id}")
def blog_detail(blog_id:int):
    try:
        data_list = [
            {"author":"Aditya Kumar","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
            {"author":"Aastha Rajpurohit","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
            {"author":"Vaibhav Tailor","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
            {"author":"Neha Sharma","blog_title":"Intel","blog_content":"Some sample text","created_by":"","created_at":""},
        ]
        print(blog_id)
        data = data_list[int(blog_id)]
        return common_response(status_code=200,message=DATA_SENT,data=data)
    except Exception as e:
        return common_response(status_code=400,error=str(e))
```

Now an example of how to accept a query in the back-end via url <br>
Dummy data to simulate the response that we will get from the database
```
data = [
    {"author": "Aditya Kumar", "blog_title": "Intel", "blog_content": "Some sample text", "created_by": "", "created_at": ""},
    {"author": "Aastha Rajpurohit", "blog_title": "Intel", "blog_content": "Some sample text", "created_by": "", "created_at": ""},
    {"author": "Vaibhav Tailor", "blog_title": "Intel", "blog_content": "Some sample text", "created_by": "", "created_at": ""},
    {"author": "Neha Sharma", "blog_title": "Intel", "blog_content": "Some sample text", "created_by": "", "created_at": ""},
    {"author": "Rohit Mehra", "blog_title": "AI Innovations", "blog_content": "Exploring the future of AI", "created_by": "", "created_at": ""},
    {"author": "Suman Verma", "blog_title": "Tech Trends", "blog_content": "Technology trends to watch in 2024", "created_by": "", "created_at": ""},
    {"author": "Ravi Kumar", "blog_title": "Machine Learning", "blog_content": "Introduction to ML algorithms", "created_by": "", "created_at": ""},
    {"author": "Priya Patel", "blog_title": "AI Ethics", "blog_content": "Understanding ethical implications of AI", "created_by": "", "created_at": ""},
    {"author": "Manish Yadav", "blog_title": "Intel", "blog_content": "Intel's latest breakthroughs", "created_by": "", "created_at": ""},
    {"author": "Kavita Singh", "blog_title": "Cloud Computing", "blog_content": "The future of cloud technologies", "created_by": "", "created_at": ""},
    {"author": "Sandeep Rao", "blog_title": "Quantum Computing", "blog_content": "Breaking down quantum computing basics", "created_by": "", "created_at": ""},
    {"author": "Divya Rathi", "blog_title": "Big Data", "blog_content": "How big data is transforming industries", "created_by": "", "created_at": ""},
    {"author": "Amit Sharma", "blog_title": "Cybersecurity", "blog_content": "Latest trends in cybersecurity", "created_by": "", "created_at": ""},
    {"author": "Harshita Soni", "blog_title": "Blockchain", "blog_content": "What is blockchain technology?", "created_by": "", "created_at": ""},
    {"author": "Deepak Choudhury", "blog_title": "5G Networks", "blog_content": "Impact of 5G on global connectivity", "created_by": "", "created_at": ""},
    {"author": "Anjali Gupta", "blog_title": "IoT", "blog_content": "The Internet of Things and its applications", "created_by": "", "created_at": ""},
    {"author": "Nikhil Joshi", "blog_title": "Robotics", "blog_content": "Future of robotics in daily life", "created_by": "", "created_at": ""},
    {"author": "Shivani Mehta", "blog_title": "Edge Computing", "blog_content": "Edge computing and its benefits", "created_by": "", "created_at": ""},
    {"author": "Siddharth Kapoor", "blog_title": "Data Science", "blog_content": "Introduction to data science and analytics", "created_by": "", "created_at": ""},
    {"author": "Neelam Desai", "blog_title": "Artificial Intelligence", "blog_content": "AI applications in healthcare", "created_by": "", "created_at": ""}
]

```
sample code to demonstrate limit
```
#example of query parameter
@app.get("/blog/blog-list-v2/")
def index(limit:int):
    # only get blogs <= to the limit that is accepted from the front-end
    data = dummy_data[:limit]
    return common_response(status_code=200,message=DATA_SENT,data=data)
```
