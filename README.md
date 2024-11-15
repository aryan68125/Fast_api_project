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
Install FastAPI ORM sqlmodel
<br>
``` 
pip install sqlmodel 
```

## Direcotry structure
#### fast_api_beginner folder
This folder holds the code that demonstrates
- How to use [GET] method
    - Imports and FastAPI Initialization
        - Creating an Instance of FastAPI
    - Defining the index Route
        - path parameter in fastAPI
        - query parameter in fastAPI
            - Accepting a single query
            - Multiple query chaining example
            - Make your query optional
        - FastAPI can differentiate between path parameters and query parameters
- Request body [POST , PATCH]
    - model.py
    - main.py
- Change the port of the FastAPI server

#### fast_api_intermediate
- Pydantic Schemas

## Some common Problems and their solutions (Troubleshooting)
#### Module not found error when running server in FastAPI
My code in main.py file looks like this
```
from fastapi import FastAPI

# Utility related imports
# import common response from utility
from utility.common_response import common_response
#importing common success message
from utility.common_success_message import (
    DATA_SENT,
)

app = FastAPI()

@app.get("/")
def index():
    data = "This endpoint is the entry point for the apis in the intermediate section."
    return common_response(status_code=200,message=DATA_SENT,data=data)
```
The Directory structrue in the project
```
fast_api_intermediate
├── blog
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── __pycache__
│       ├── __init__.cpython-312.pyc
│       ├── main.cpython-312.pyc
│       └── models.cpython-312.pyc
├── __pycache__
│   └── main.cpython-312.pyc
└── utility
    ├── common_error_message.py
    ├── common_response.py
    ├── common_success_message.py
    ├── __init__.py
    ├── __pycache__
    │   ├── common_response.cpython-312.pyc
    │   ├── common_success_message.cpython-312.pyc
    │   └── __init__.cpython-312.pyc
    ├── validation_regex_patterns.py
    └── validations.py
```
If you have the directory structure that looks somthing like what is shown above then you can't use this command ```uvicorn main:app --reload``` to run your fastAPI server. 
<br>
If you use this command then you will get the error that looks something like this 
```
  File "/home/aditya/github/Fast_api_project/fast_api_intermediate/blog/main.py", line 5, in <module>
    from utility.common_response import common_response
ModuleNotFoundError: No module named 'utility'
```
You need to get one level out of your blog folder if you are inside of it and run this command instead ``` uvicorn blog.main:app --reload ``` to run your FastAPI server. This tells uvicorn to treat blog.main as a module in the blog package, and Python can then resolve the relative imports properly. Hence resolving the issue.

## Sample code in FastAPI [GET]
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

## path parameter in fastAPI
A path parameter in fast api works in the same way as dynamic urls in django and django DRF.
The code below is a demo of a path parameter
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

## query parameter in fastAPI
The example of how a query parameter may look like 

<br>

This is an example of single query
```
http://127.0.0.1:8000/blog/blog-list-v2/?limit=6
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
#### Accepting a single query
Dummy data to simulate the response that we will get from the database
```
data = [
    {"author": "Aditya Kumar", "blog_title": "Intel", "blog_content": "Some sample text", "created_by": "", "created_at": "", "publish":True},
    {"author": "Aastha Rajpurohit", "blog_title": "Intel", "blog_content": "Some sample text", "created_by": "", "created_at": "","publish":False},
    {"author": "Vaibhav Tailor", "blog_title": "Intel", "blog_content": "Some sample text", "created_by": "", "created_at": "","publish":True},
    {"author": "Neha Sharma", "blog_title": "Intel", "blog_content": "Some sample text", "created_by": "", "created_at": "","publish":True},
    {"author": "Rohit Mehra", "blog_title": "AI Innovations", "blog_content": "Exploring the future of AI", "created_by": "", "created_at": "","publish":False},
    {"author": "Suman Verma", "blog_title": "Tech Trends", "blog_content": "Technology trends to watch in 2024", "created_by": "", "created_at": "","publish":True},
    {"author": "Ravi Kumar", "blog_title": "Machine Learning", "blog_content": "Introduction to ML algorithms", "created_by": "", "created_at": "","publish":False},
    {"author": "Priya Patel", "blog_title": "AI Ethics", "blog_content": "Understanding ethical implications of AI", "created_by": "", "created_at": "","publish":True},
    {"author": "Manish Yadav", "blog_title": "Intel", "blog_content": "Intel's latest breakthroughs", "created_by": "", "created_at": "","publish":False},
    {"author": "Kavita Singh", "blog_title": "Cloud Computing", "blog_content": "The future of cloud technologies", "created_by": "", "created_at": "","publish":True},
    {"author": "Sandeep Rao", "blog_title": "Quantum Computing", "blog_content": "Breaking down quantum computing basics", "created_by": "", "created_at": "","publish":False},
    {"author": "Divya Rathi", "blog_title": "Big Data", "blog_content": "How big data is transforming industries", "created_by": "", "created_at": "","publish":True},
    {"author": "Amit Sharma", "blog_title": "Cybersecurity", "blog_content": "Latest trends in cybersecurity", "created_by": "", "created_at": "","publish":False},
    {"author": "Harshita Soni", "blog_title": "Blockchain", "blog_content": "What is blockchain technology?", "created_by": "", "created_at": "","publish":True},
    {"author": "Deepak Choudhury", "blog_title": "5G Networks", "blog_content": "Impact of 5G on global connectivity", "created_by": "", "created_at": "","publish":False},
    {"author": "Anjali Gupta", "blog_title": "IoT", "blog_content": "The Internet of Things and its applications", "created_by": "", "created_at": "","publish":True},
    {"author": "Nikhil Joshi", "blog_title": "Robotics", "blog_content": "Future of robotics in daily life", "created_by": "", "created_at": "","publish":False},
    {"author": "Shivani Mehta", "blog_title": "Edge Computing", "blog_content": "Edge computing and its benefits", "created_by": "", "created_at": "","publish":True},
    {"author": "Siddharth Kapoor", "blog_title": "Data Science", "blog_content": "Introduction to data science and analytics", "created_by": "", "created_at": "","publish":False},
    {"author": "Neelam Desai", "blog_title": "Artificial Intelligence", "blog_content": "AI applications in healthcare", "created_by": "", "created_at": "","publish":True}
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
#### Multiple query chaining example 
This is an example of multiple query chaining
```
http://127.0.0.1:8000/blog/blog-list-v2-publish/?limit=6&publish=false
```
example of multiple query chaining 
```
@app.get("/blog/blog-list-v2-publish/")
def index(limit:int,publish: bool):
    # only get blogs <= to the limit that is accepted from the front-end
    if publish == True:
        filtered_data = [blog for blog in dummy_data if blog["publish"] == True]

        # Only return the filtered data up to the requested limit
        data = filtered_data[:limit]
        return common_response(status_code=200,message=DATA_SENT,data=data)
    if publish == False:
        filtered_data = [blog for blog in dummy_data if blog["publish"] == False]
        data = filtered_data[:limit]
        return common_response(status_code=200,message=DATA_SENT,data=data).
```
You can also provide a default value for limit and publish if you should so desire.
eaxmple sample code : 
```
def index(limit:int=5,publish: bool=True):
```
Now if nothing is provided from the front-end then the default value as shown above will be supplied.

#### Make your query optional
Make your query optional by using Optional after importing it from the library like this ``` from typing import Optional ```
```
from typing import Optional
#example of query parameter
@app.get("/blog/blog-list-v2-publish/")
def index(limit:int=5,publish: Optional[bool]=None):
    # only get blogs <= to the limit that is accepted from the front-end
    if publish == True:
        filtered_data = [blog for blog in dummy_data if blog["publish"] == True]

        # Only return the filtered data up to the requested limit
        data = filtered_data[:limit]
        return common_response(status_code=200,message=DATA_SENT,data=data)
    if publish == False:
        filtered_data = [blog for blog in dummy_data if blog["publish"] == False]
        data = filtered_data[:limit]
        return common_response(status_code=200,message=DATA_SENT,data=data)
    
    data = dummy_data[:limit]
    return common_response(status_code=200,message=DATA_SENT,data=data)
```
Here ``` publish: Optional[bool]=None ``` will set the query publish into an optional query which when not supplied will cause an api-endpoint to default to its default behaviour.

## NOTE : FastAPI can differentiate between path parameters and query parameters
- **Path Parameter** :
```
@app.get("/blog/blog-detail/{blog_id}")
def blog_detail(blog_id:int):
```
In case of path parameter we have to specify the path parameter in the url in the decorater like this ```@app.get('/url/{path_parameter}/')```
- **Query Parameter** : 
``` 
@app.get("/blog/blog-list-v2-publish/")
def index(limit:int=5,publish: Optional[bool]=None):
```
In case of query parameter we don't specify anything in the url in the decorator

## Change the port of the FastAPI server 
Add the code below at the last after you have added all of you api end-points in your ```main.py``` file.
```
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8001)
```
**NOTE** : The command ```uvicorn main:app --reload``` will run the server in its default port i.e 8000
If you want the changes made by the above code to take effect and start the server in the port that you defined in main.py file as shown above then use this command to do so ```python3 main.py```

## Pydantic Schemas [Handling (POST) request]
SQLmodel is an ORM library that allows us to communicate with the Database engine in a similar way to how django orm works. 

<br>

**Object-relational mapping (ORM)** is a way to align programming code with database structures. ORM uses metadata descriptors to create a layer between the programming language and a relational database. It thus connects object-oriented program (OOP) code with the database and simplifies the interaction between relational databases and OOP languages. 

<br>

In FastAPI we use sqlmodel ORM to communicate with the Database and the way to install it in  your virtual env is as shown below: 
<br>
```
pip install sqlmodel
```

### Accept the data from the front-end and store it in the Database
This is the project directory structure
```
fast_api_intermediate
├── blog
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── __pycache__
│       ├── __init__.cpython-312.pyc
│       ├── main.cpython-312.pyc
│       └── models.cpython-312.pyc
├── __pycache__
│   └── main.cpython-312.pyc
└── utility
    ├── common_error_message.py
    ├── common_response.py
    ├── common_success_message.py
    ├── __init__.py
    ├── __pycache__
    │   ├── common_response.cpython-312.pyc
    │   ├── common_success_message.cpython-312.pyc
    │   └── __init__.cpython-312.pyc
    ├── validation_regex_patterns.py
    └── validations.py
```
#### blog/models.py
```
from pydantic import BaseModel 
from typing import Optional

#import some additional field types manually that are not defined in FastAPI
from datetime import datetime, time, timedelta

class BlogModel(BaseModel):
    title : str
    body : str
    created_at : datetime
    created_by : Optional[int] = None
    is_deleted : bool = False
```
**Explaination** : <br>
- ```from pydantic import BaseModel```: This imports the BaseModel class from Pydantic. BaseModel is the core class in Pydantic used to create data models with built-in data validation
- ```from typing import Optional```: This imports Optional from Python's typing module. Optional is used to indicate that a variable or attribute can have a value or be None
- ```class BlogModel(BaseModel)```: This creates a new class BlogModel that inherits from BaseModel, making it a Pydantic model. 
    - A **Pydantic** model is a Python class derived from the BaseModel class provided by the Pydantic library. Pydantic models are primarily used for data validation and serialization. They allow you to define data structures with specific fields and types, and they automatically validate the data assigned to each field. This makes Pydantic models especially useful for applications that require robust data handling, such as APIs and data processing scripts.
- ```title: str```: This declares a field called title that must be a string. Pydantic will enforce that the value assigned to title is always a string.
- ```published_at: Optional[bool] = None```: This defines an optional field called published_at, which can be either a bool (True or False) or None. The = None default means that if no value is provided for published_at, it will default to None.
#### blog/main.py
```
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
```
**NOTE** : Use ```uvicorn blog.main:app --reload``` when you are in the ```./fast_api_intermediate``` directory.
#### Connect with the SQLite Database
In order to connect to the database in FastAPI you need SQLAlchemy. <br>
**SQLAlchemy** is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

- First you need to create a file called ```database.py``` .
    - After creating ```database.py``` file the project structure will look something like this: 
        ```
            fast_api_intermediate
        ├── blog
        │   ├── __init__.py
        │   ├── main.py
        │   ├── models.py
        │   └── __pycache__
        │       ├── __init__.cpython-312.pyc
        │       ├── main.cpython-312.pyc
        │       └── models.cpython-312.pyc
        ├── database.py
        ├── __pycache__
        │   └── main.cpython-312.pyc
        └── utility
            ├── common_error_message.py
            ├── common_response.py
            ├── common_success_message.py
            ├── __init__.py
            ├── __pycache__
            │   ├── common_response.cpython-312.pyc
            │   ├── common_success_message.cpython-312.pyc
            │   └── __init__.cpython-312.pyc
            ├── validation_regex_patterns.py
            └── validations.py
        ```
    - The start of any **SQLAlchemy** **application** is an object called the **Engine**. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a **connection** **pool** for these database connections. The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend. 
    <br> <br>
    if you want to use an in-memory-only database **[This kind of database is perfect for experimenting as it does not require any server nor does it need to create new files.]** : -> 

        ```
        from sqlalchemy import create_engine
        engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
        ```

        **Explaination** : <br>
        The main argument to ```create_engine``` is a string URL, above passed as the string ```sqlite+pysqlite:///:memory:```. This string indicates to the Engine three important facts:
        - What kind of database are we communicating with? This is the sqlite portion above, which links in SQLAlchemy to an object known as the **dialect**.
            - **dialect** : In SQLAlchemy, the “dialect” is a Python object that represents information and methods that allow database operations to proceed on a particular kind of database backend and a particular kind of Python driver (or DBAPI) for that database. SQLAlchemy dialects are subclasses of the Dialect class.
        - What **DBAPI** are we using? The Python **DBAPI** is a third party driver that SQLAlchemy uses to interact with a particular database. In this case, we’re using the name pysqlite, which in modern Python use is the sqlite3 standard library interface for SQLite. If omitted, SQLAlchemy will use a default **DBAPI** for the particular database selected.
            - **DBAPI** is shorthand for the phrase “Python Database API Specification”. This is a widely used specification within Python to define common usage patterns for all database connection packages. The DBAPI is a “low level” API which is typically the lowest level system used in a Python application to talk to a database. SQLAlchemy’s dialect system is constructed around the operation of the DBAPI, providing individual dialect classes which service a specific DBAPI on top of a specific database engine; for example, the create_engine() URL ```postgresql+psycopg2://@localhost/test``` refers to the psycopg2 DBAPI/dialect combination, whereas the URL ```mysql+mysqldb://@localhost/test``` refers to the MySQL for Python DBAPI/dialect combination
        - How do we locate the database? In this case, our URL includes the phrase ```/:memory:```, which is an indicator to the sqlite3 module that we will be using an in-memory-only database. This kind of database is perfect for experimenting as it does not require any server nor does it need to create new files. 

    <br>

    If you want to use an actual physical database i.e a ```.db``` file then you need to modify the previously used code in ```database.py``` file :->

    ```
    from sqlalchemy import create_engine
    SQLALCHAMY_DATABASE_URL = "sqlite+pysqlite:///./blog.db"        
    engine = create_engine(SQLALCHAMY_DATABASE_URL, echo=True)
    ```

    Here ```./blog.db``` is the location of the database to which you want to make a connection to.

    <br>

    Incase of **FastAPI** We need to add the code below in ```database.py``` file.
    
    ```
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker, relationship

    SQLALCHAMY_DATABASE_URL = "sqlite+pysqlite:///./blog.db"

    connect_args = {"check_same_thread": False}

    engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args=connect_args)

    SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

    Base = declarative_base()
    ```
    **Explaination** : <br>
    This code sets up a basic configuration for using SQLAlchemy with a SQLite database in a Python project. Let’s break down each part and its purpose:

    1. **Importing SQLAlchemy Modules**:
    ```python
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker, relationship
    ```
    - `create_engine`: This function is used to create a connection to the database.
    - `declarative_base`: Provides a base class for declarative class definitions. This is where models (tables) inherit from to be mapped to the database.
    - `sessionmaker`: A factory for creating new SQLAlchemy session objects, which allow interaction with the database.
    - `relationship`: Used to define relationships between tables, like foreign keys, which can link tables.

    2. **Database URL and Connection Arguments**:
    ```python
    SQLALCHAMY_DATABASE_URL = "sqlite+pysqlite:///./blog.db"
    connect_args = {"check_same_thread": False}
    ```
    - `SQLALCHAMY_DATABASE_URL`: Specifies the URL for the database connection. In this case, it’s a local SQLite database file named `blog.db`.
    - `connect_args`: Arguments passed to the SQLite database engine. Setting `check_same_thread` to `False` is necessary for SQLite to allow multiple threads to use the same connection, which is required for some applications.

    3. **Creating the Engine**:
    ```python
    engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args=connect_args)
    ```
    - `engine`: The engine is created using `create_engine()` with the database URL and connection arguments. This `engine` serves as the starting point for any database connection in SQLAlchemy, managing communication between the Python application and the SQLite database.

    4. **Session Factory**:
    ```python
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    ```
    - `SessionLocal`: This is a session factory, which provides instances of database sessions to interact with the database. 
    - `autoflush=False`: Disables automatic flushing of data changes to the database after each query. Instead, changes are only committed when explicitly called.
    - `autocommit=False`: This setting requires explicit commits on each transaction, giving more control over when data is saved.

    5. **Base Class for ORM Models**:
    ```python
    Base = declarative_base()
    ```
    - `Base`: The base class for all ORM (Object-Relational Mapping) models. Any table models you create will inherit from `Base`, allowing SQLAlchemy to map Python classes to database tables.

    ### How It All Works Together
    This setup prepares SQLAlchemy to interact with a SQLite database:
    - The `engine` creates a connection to the database file.
    - `SessionLocal` generates sessions, which are used to query and make changes to the database.
    - `Base` is used to define model classes for each table, allowing you to interact with tables as Python objects.


    Some important links that you can use for reference <br>
    <a href="https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine" target="_blank">SQLAlchamy : Database connection</a>
    
    <a href="https://docs.sqlalchemy.org/en/20/orm/quickstart.html" target="_blank">SQLAlchamy : Declare Models</a>

    <a href="https://fastapi.tiangolo.com/tutorial/sql-databases/?h=database#create-models" target="_blank">FastAPI : Database Connection</a>

    <a href="https://stackoverflow.com/questions/47644739/what-column-type-does-sqlalchemy-use-for-text-on-mysql" target="_blank">SQLAlchamy : what column type does sqlalchamy has for text on mysql</a>
#### Define SQLModel
Instead of using Pydantic BaseModel we are going to use ```SQLModel``` here and there is a reason for that because pydantic model is not enough for us to be able to store data in the database when we supply data from the front-end to our api-endpoint. <br>
SQLModel is an ORM (Object-Relational Mapper) library for Python that combines Pydantic and SQLAlchemy. It allows you to define database models as Python classes, which can then be used to interact with SQL databases. SQLModel is designed to simplify the work involved in creating, reading, updating, and deleting data in databases, while also enabling Pydantic's data validation and serialization features. <br>
In this code as shown below, SQLModel is used as a base class for the BlogModel, allowing it to act as both a Pydantic model for data validation and a database model. <br>
models.py file : 
```
from datetime import datetime
from sqlmodel import SQLModel, Field

class BlogModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    body: str | None = Field(default=None, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)  # Set to current UTC time
    created_by: int
```
**Explaination** : 
- ```table=True``` Parameter : <br>
    The ```table=True``` parameter in the BlogModel class marks it as a table in the database. When you set ```table=True```, SQLModel will create a corresponding SQL table for the class when create_all is called on the database engine. If ```table=True``` is omitted, the class will not represent a table, but it can still be used as a data model (like a Pydantic model). <br> <br>
    What ```table=True``` does: Creates a table in the database.
    What table itself represents: An attribute of the SQLModel metaclass to determine whether this class is a table model or just a data-only model.
- ```id: int | None = Field(default=None, primary_key=True)``` : <br>
    Type: ```int | None``` means that id is an integer but can initially be ```None```. <br> <br>
    ```default=None```: Initializes id as None until a value is assigned <br> <br>
    ```primary_key=True```: Sets this field as the primary key of the table, meaning it uniquely identifies each row. <br> <br>
    By default, primary keys are auto-incremented in SQLModel when using databases that support it (such as SQLite, PostgreSQL, or MySQL). For most SQL databases, primary_key=True will result in auto-increment behavior if default=None is set. Therefore, this field is likely to auto-increment in SQLModel unless the database does not support it.
- ```created_at: datetime = Field(default_factory=datetime.utcnow)``` <br>
    This line creates a ```created_at``` field with a datetime type, which stores the date and time when a record is created. Here’s a breakdown: <br>
    Field(```default_factory=datetime.utcnow```): <br>
    - ```default_factory=datetime.utcnow```: Calls datetime.utcnow to set the current UTC time as the default value when a new record is created.
    - This ensures that each new record has an automatic timestamp without needing to be set manually.
- ```datetime.utcnow:``` : 
    - ```datetime.utcnow()``` provides the current date and time in UTC (Coordinated Universal Time) instead of the local timezone. This is often preferred in databases for consistency across time zones.
    - ```default_factory``` allows a callable (like ```datetime.utcnow```) to run each time a new instance of the model is created, so ```created_at``` is always initialized to the exact creation time.
- Without ```default_factory```:
    - If ```default_factory``` were omitted, created_at would require an explicit value for each record, meaning you’d have to set the time manually every time a new row is created.
- ```index=True``` : <br>
    In SQLModel, index=True on a field (like title or body) tells the database to create an index for that column. <br> <br>
    An **index** is a database structure that improves the speed of data retrieval operations on that column. When you query for a specific title or body, the database can find the results faster using an **index**. <br> <br>
    **Use Cases for ```index=True```** : If you frequently search, filter, or sort by a specific field (e.g., title), indexing it can significantly speed up those queries. <br>

