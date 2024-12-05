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
pip3 install fastapi[all]
```
OR you can run the command below to install Fastapi in your system <br>
```
pip3 install fastapi[all]
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

## Some tips and tricks in FastAPI
### PostgreSQL Installation process 
Folow the guide from the official postgreSQL docs provided in the link given below <br>
https://www.postgresql.org/download/linux/debian/

### Set password to the default user in postgreSQL server
In PostgreSQL, the `postgres` role does not have a password set by default, and you cannot log in using this role with a password until one is explicitly set. Here's how you can set or change the password for the `postgres` role:

---

#### 1. **Log In as the `postgres` User**
Since you’re already logged in to the system, you can switch to the `postgres` user and enter the PostgreSQL shell:
```bash
sudo -u postgres psql
```

---

#### 2. **Set a Password for `postgres`**
In the PostgreSQL shell, run the following command to set or change the password:
```sql
ALTER USER postgres WITH PASSWORD 'your_secure_password';
```
Replace `your_secure_password` with a strong password of your choice.

---

#### 3. **Verify the Password**
Exit the PostgreSQL shell:
```sql
\q
```
Then try logging in using the `postgres` user with the password:
```bash
psql -U postgres -W
```
You’ll be prompted to enter the password.

---

#### 4. **Optional: Update Authentication Method in `pg_hba.conf`**
If the `pg_hba.conf` file is configured for `peer` or `trust` authentication, PostgreSQL will not ask for a password. To require a password, you need to update the authentication method:

1. Open the `pg_hba.conf` file (usually located in `/etc/postgresql/<version>/main/`):
   ```bash
   sudo nano /etc/postgresql/<version>/main/pg_hba.conf
   ```

2. Find the line for the `postgres` user or `local` connections and change the method to `md5`:
   ```plaintext
   local   all   postgres   md5
   ```

3. Save and close the file, then restart PostgreSQL:
   ```bash
   sudo systemctl restart postgresql
   ```

Now, the `postgres` role will require a password to log in.

### Run server when your main.py file is inside a python package 
The directory structure looks something like this : 
```
.
├── blog_app
│   ├── __init__.py
│   ├── main.py
│   └── __pycache__
│       ├── __init__.cpython-312.pyc
│       └── main.cpython-312.pyc
├── dummy_data_CRUD.py
├── images
│   └── readme_images
│       ├── crud.png
│       ├── path_operation.png
│       └── post_request.png
├── naive_main_code.py
├── __pycache__
│   ├── Blog.cpython-312.pyc
│   └── main.cpython-312.pyc
├── pydantic_custom_models
│   ├── Blog.py
│   ├── __init__.py
│   └── __pycache__
│       ├── Blog.cpython-312.pyc
│       └── __init__.cpython-312.pyc
└── utility
    ├── common_response.py
    ├── dummy_data.py
    ├── __init__.py
    └── __pycache__
        ├── common_response.cpython-312.pyc
        ├── dummy_data.cpython-312.pyc
        └── __init__.cpython-312.pyc
```
This command is used to run the FastAPI server if your main.py file is inside a python package.
```
uvicorn blog_app.main:app --reload 
```
Here ```blog_app``` is the package (folder) name , ```main``` is the file name , ```app``` is defined in the main.py file like this ```app = FastAPI()```. ```app``` is nothing but a FastAPI instance which allows us to use decorators and make our common python functions into a FastAPI routes

### Open swagger UI to test your apis 
The way to open swagger UI so that you can test your apis in an interactive way all you need to do is add docs after the server's url in your browser as shown here :-> ``` http://127.0.0.1:8000/docs ``` You don't need to do any additional configurations to enable swagger UI.

### Change the port of the FastAPI server 
Add the code below at the last after you have added all of you api end-points in your ```main.py``` file.
```
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8001)
```
**NOTE** : The command ```uvicorn main:app --reload``` will run the server in its default port i.e 8000
If you want the changes made by the above code to take effect and start the server in the port that you defined in main.py file as shown above then use this command to do so ```python3 main.py```

## Some common Problems and their solutions (Troubleshooting)
### Module not found error when running server in FastAPI
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

**Path Operation** :  <br>
![image info](fast_api_advance/images/readme_images/path_operation.png)

<br>

Explanation of @app.get("/"):
- @app.get("/") is a decorator that registers this function (index) as a handler for GET requests to the / route. This decorator is what makes a normal python function into a path operation function.
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

## POST requests
**POST request** To create a data in the DB -->
![image info](fast_api_advance/images/readme_images/post_request.png)

<br>

In post request we can send data from the front-end to the back-end to create data resource in the database in the body. <br>

Here is an example of a post request made in FastAPI : <br>
```
from fastapi.params import Body
@app.post("/create-posts/")
def create_posts(data: dict = Body(...)):
    print(data)
    return response(status=201,message="Post Created!")
```

```data: dict = Body(...)```

<br>

- Body(...) = Its gonna extract all of the fields from the body.
- dict = Its gonna convert the extracted fields into a python dictionary.
- data = It is a variable name which is gonna save the dictionary of data that has been recently converted

<br>

When you pass in this in your swagger post api end-point that creates posts
```
{
"title":"Intels downfall",
"body":"Intels downfall body of blog"
}
```
You will get a response that the posts is created if everything works well. <br>
In your back-end since you printed the data you will get the output in your server's terminal that looks something like this : 
```
.....

INFO:     127.0.0.1:60996 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:32780 - "POST /create-posts/ HTTP/1.1" 422 Unprocessable Entity
{'title': 'Intels downfall', 'body': 'Intels downfall body of blog'}
INFO:     127.0.0.1:40038 - "POST /create-posts/ HTTP/1.1" 200 OK

.....
```
Issues in this methods are discussed below : <br>
- It's a pain to get all the values from the body. right now we need to extract the fields individually and then convert it into a python dictionary and then save it into a variable.
- Client side can send whatever data they want. Allowing the front-end to send arbitrary data is a bad move. The back-end must accept data in a particular format in this case where we are trying to create a blog we need : <br>
    - Title : Title of the blog
    - Body : Body of the blog
    - created_by : The user who created that blog
    - created_at : Stores the creation date of the blog
    - updated_at : Stores the date when the blog is updated
    - is_deleted : Flag that will allow us to soft delete the blog 
- The data is not getting validated. So how do I ensure that the user sends the data what I want ? <br>
**NOTE** : One important thing to note is none of these fields are allowed to be empty because we don't want users to create a blog that have a any of the above fields to be empty. <br>
Hence I can't have a post having a blank title or body so how do we make sure that the data that the user sends is actually valid. <br>
- Ultimately we want to force the client to send the data in a schema that we expect.
<br>

**Schema** : The defination of how the data should look like so that it is almost like a contract. <br>

The way to force the client to send data in a way that the back-end api expects it to be is to use Pydantic. Pydantic is used to define how our schema should look like.

## Pydantic Models
Pydantic has nothing to do with FastAPI. It is it's own completely different and separate library that you can use with any of the python application. FastAPI just makes use of it so that we can define the schema.
#### Example : How to use Pydantic to define a schema for the api-end point
pydantic models named Blog.py
```
#datetime imports
from datetime import date

#import pydantic
from pydantic import BaseModel, Field
from typing import Optional

#Pydantic model
class Blogs(BaseModel):
    title: str
    content:str
    is_published:bool = True
    created_by:int
    created_at:date = Field(default_factory=date.today)
    updated_at:date
    is_deleted:bool = False
    rating : Optional[int] = None
```

## CRUD Operation : Using Dummy data without database
![image info](fast_api_advance/images/readme_images/crud.png)
CRUD is and acronym for Create Read Update Delete operations that we perform on the records in the database. 

### POST : Create operation
#### For now we are not gonna make connection to the database for our CRUD operations because its complicated at this time
We are gonna define a **dummy_data** that we will use to perform our CRUD operations. <br>
Define the dummy data into a seperate file and then import it into your main.py file
```
from datetime import date

my_blogs = [
    {"id": 1, "title": "The Rise of AI", "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "is_published": True, "created_by": 1, "created_at": date(2024, 11, 20), "updated_at": date(2024, 11, 21), "is_deleted": False, "rating": 4},
.....
.....
{"id": 20, "title": "Exploring Blockchain", "content": "Fusce auctor mauris vitae erat fermentum, sit amet ultricies arcu fermentum.", "is_published": True, "created_by": 10, "created_at": date(2024, 8, 15), "updated_at": date(2024, 8, 16), "is_deleted": False, "rating": 4}
]
```
main.py code
```
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
from random import randrange
@app.post("/blogs/")
def create_blog(Blog:Blogs):
    #Add the incoming data to the dummy data array
    blog_dict = Blog.dict()
    blog_dict['id'] = randrange(0,99999999)
    my_blogs.append(blog_dict)
    return response(status=201,message="Blog created!",data=blog_dict)
```
**Explaination** : <br>
```dummy_data``` gets serialized automatically by FastAPI into JSON format. You don't need to do anything here. <br> <be>
Since we are not using sql we need to assign pk randomly to the dictionary that we are appending into our dummy data array. This is done to simulate the database objects. <br>
**NOTE:** The best practice is to send the newly created posts after the post is saved along with the success message. Check this video out for more reference <br>
https://youtu.be/50YYelLKm3w?list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&t=478

### GET : Get one blog : Read operation
**NOTE** : This operation is performed on dummy data and not on actual database <br>
Sample code : <br>
```
@app.get("/blogs/{id}")
def get_blog(id):
    print(type(id),id)
    # Create a dictionary keyed by blog IDs
    blogs_by_id = {blog["id"]: blog for blog in my_blogs}

    blog_id = int(id)
    result = blogs_by_id.get(blog_id, False)
    if not result:
        return response(status=404,error="Blog not found!")
    return response(status=200,message="Blog sent!",data=result)
```
```@app.get("/blogs/{id}")``` The id here is a path parameter. The id represents the primary key of a specific record in the database. The FastAPI will automaticaly extract the id and then we can pass it right into the function like this as shown below: <br>
```
@app.get("/blogs/{id}")
def get_blog(id):
```
Now at this point our function has access to whatever value was in that url right there. <br>
**Dictionary Comprehension:** ```{blog["id"]: blog for blog in my_blogs}``` creates a new dictionary where the key is the blog's id and the value is the entire blog dictionary. <br>
**Efficient Lookup:** Using ```blogs_by_id.get(blog_id)``` allows you to fetch a blog by its id in ```O(1)``` time. <br>
**Fallback:** If the id is not found, the get method will return ```"Blog not found"``` as a default value. You can customize this as needed.
**NOTE** : <br>
- ```def get_blog(id):``` If you use this then the id you will get will be type str and this may cause issues since if you use this id then the dictionary comprehension logic won't be able to find the blog in the dummy data.
- ```def get_blog(id:int):``` This code automatically converts the id into integer this will work correctly with the dictionary comprehension code and will return the blog if the id matches in the dummy data.
    - Updated code : 
        ```
        @app.get("/blogs/{id}")
        def get_blog(id:int):
            print(type(id),id)
            # Create a dictionary keyed by blog IDs
            blogs_by_id = {blog["id"]: blog for blog in my_blogs}

            blog_id = int(id)
            result = blogs_by_id.get(blog_id, False)
            if not result:
                return response(status=404,error="Blog not found!")
            return response(status=200,message="Blog sent!",data=result)
        ```
### GET : Get all blogs : Read operation
**NOTE** : This operation is performed on dummy data and not on actual database <br>
Sample code : 
```
@app.get("/blogs")
def get_blogs():
    dummy_data = my_blogs
    return response(status=200,message="Post Sent!", data=dummy_data)
```
The above code sends all the blogs there is in dummy data.

### DELETE : Delete blog by id : Delete operation
**NOTE** : This operation is performed on dummy data and not on actual database
<br>
sample code : <br>

```
@app.delete('/blogs/{id}')
def delete_blog(id:int,status_code=status.HTTP_204_NO_CONTENT):
    blog_index = next((index for index,blog in enumerate(my_blogs) if blog['id']==id),None)
    if not blog_index:
        return response(status=status.HTTP_404_NOT_FOUND,error="Blog not found!")
    deleted_blog = my_blogs.pop(blog_index)
    return response(status=status.HTTP_204_NO_CONTENT)
```
After deleting the record when sending the response you need to send status code 204 here is the link to the video if you want to confirm the info that is provided here : https://youtu.be/QxlryV2Zoi4?list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&t=297

<br>

**NOTE**: If you try to send any data when using status_code 204 in FastAPI it will throw an error. This is how FastAPI handles 204 status code responses. So make sure that you don't send any data when using status_code 204 in case if delete operation.

### PATCH : Partial update operation
**NOTE** : This operation is performed on dummy data and not on actual database
<br>
sample code : <br>

```
@app.patch('/blogs/{id}')
def update_blog(id:int,Blog:Blogs):
    front_end_blog_dict = Blog.dict()
    front_end_blog_dict['id'] = id
    blog_index = next((index for index,blog in enumerate(my_blogs) if blog['id']==id),None)
    if not blog_index:
        return response(status=status.HTTP_404_NOT_FOUND,error="Blog not found!")
    my_blogs[blog_index] = front_end_blog_dict
    return response(status=status.HTTP_200_OK,message="Blog updated!")
```
**Explaination** : 
```
front_end_blog_dict = Blog.dict()
front_end_blog_dict['id'] = id
```
Convert the incoming data into a python dictionary. Save the id back into the incoming data after it has been converted to the python dictionary. <br>
```
blog_index = next((index for index,blog in enumerate(my_blogs)
```
Extract blog index from the array of dictionaries in dummy data.
```
my_blogs[blog_index] = front_end_blog_dict
```
Assign the data coming from the front-end to the dummy data using blog index.

## FastAPI error handling in api response : 
Up until now we have been sending in hard coded status code in our api responses. There is a better way to send status code in our responses we can use FastAPIs status library <br>
```
from fastapi import status
``` 
<br>

Now you can use status code in your api-routes responses <br>
Sample code : 
```
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

    blog_id = int(id)
    result = blogs_by_id.get(blog_id, False)
    if not result:
        return response(status=status.HTTP_404_NOT_FOUND,error="Blog not found!")
    return response(status=status.HTTP_200_OK,message="Blog sent!",data=result)
```
Here is a docs related to status code : https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

## Database
Now before we start using GET, POST, PUT, PATCH and DELETE operations to perform CRUD on data in the database we need to understand what database actually is. <br>
**What is a Database?** 
- A database is a collection of organized data that can be easily accessed and managed.

<br>

**What is DBMS ?** 
![image info](fast_api_advance/images/readme_images/Database_and_dbms.png)
- We never interact with the database directly. 
- Instead we have a database management system thats going to sit in the middle. 
- So when we want to perform an operation on the database we are going to send that request to a database management system and that is then going to perform that operation on the database and then it's going to send that result back to us.
- So we never talk to the databases directly we always have a piece of software that sits in the middle and acts as the brains behind the database

<br>

**Types of databases :**

<br>

There two types of databases Relational and NoSQL
![image info](fast_api_advance/images/readme_images/Types_of_databases.png)
In this project we are gonna use PostgreSQL. Now all of the relational databases are 90% same with the 10% differences.
Now each of the databases implements SQL in a slightly different way. So you may see differences in some of the SQL commands in different types of relational databases that are currently being used in the market.

### SQL : Structured Query Language
![image info](fast_api_advance/images/readme_images/SQL_DBMS.png)
SQL is a language that is used to communicate with the DBMS.
- So when we want to perform an operation we are gonna send an sepcific SQL statement to the DBMS 
- DBMS is then gonna take that statement and then perform the operation on the database
- After completing that operation the DBMS is gonna send the result back to us.

### Database Tables : Concept of tables
![image info](fast_api_advance/images/readme_images/database_tables.png)
A table is a representation of a subject or event in an application. <br>
Lets take an example of an e-commerce application : <br>
- Users table : Consists all of the records for all the users
- Products table : Consists all of the records for all the products that you want to sell
- Purchases tables : Consists all of the records related to purchases of products made by customers. <br>
All these tables are gonna form some form of relationship. That's why its called a relational database.

<br> 

#### Rows and Columns
![image info](fast_api_advance/images/readme_images/database_tables_rows_col.png)
- A table is made up of columns and rows
- Each column represents a different attribute
- Each row represents a different entry in the table

<br> 

#### DataTypes in a database tables
![image info](fast_api_advance/images/readme_images/Database_datatypes.png)
- Databases have datatypes just like any programming language.
- When create a column in a database table you need to specify what kind of data type that column is gonna store in a table.

<br>

#### Primary keys in a database table
![image info](fast_api_advance/images/readme_images/pk.png)
- When we create a table we have to specify something called a primary key.
- Primary key is a column or a group of columns that uniquely identifies each row in a table.
- We need to tell postgres how can we identify each enty in a table.
- We can only have one primary key per table. We cannot have multiple primary keys in a table.
- However primary key can span multiple columns.
- Each primary_key must be unique and no duplicate primary keys are allowed in a database table.

<br>

![image info](fast_api_advance/images/readme_images/pk_email.png)
- Normally the primary key is the id column as shown in the previous example picture just above this section but that's not always the case
- The table doesn't even have to have the id column. There are certain instances where you may not want an id column.
- If you don't have an id column or you may not want an id column there must be some column in a table that is able to uniquely identify the entries in that table.
- Email column or a phone number column could be used to uniquely identify the users in a users table. A user can only signup using a unique email address or a phone number hence these two fields can serve the purpose of being a primary key just like an id column in a table.

<br>

#### **Constraints in the database table**
#### Unique constrains in a database tables
![image info](fast_api_advance/images/readme_images/unique_constraints.png)
- We can add an extra constraints on any column in a database table.
- A unique constraints can be applied to any column to make sure every record has a unique value for that column.

<br>

#### Null constrains in a database tables
![image info](fast_api_advance/images/readme_images/null_constraints.png)
- When it comes to creating columns by default postgres allows you to leave a column blank. In the back-end postgres will put in a value of null if no value is supplied to that column in that particular entry of the table.
- We can use null constraint to tell postgres to prevent the creation of an entry in the table if a column in that entry is not provided with any value.

### Postgres
![image info](fast_api_advance/images/readme_images/postgres.png)
When you install an instance of postgres, what we can do is carve out multiple separate databases i.e we can create a separate database for our project other than the database that is provided by default by postgres after installation.These databases are completely isolated and have nothing to do with one another. <br>
The diagram below will help you to understand more of what is discussed above : 
![image info](fast_api_advance/images/readme_images/postgres_2_db.png)
The image above shows that the postgres allows you to carve out multiple databases from a postgres instance.
- By default every postgres installation comes with one database already created called **"postgres"**
- This is important because postgres requires you to specify the name of a database to make a connection. So there needs to always be one database.
**NOTE :** The reason why after postgres installation postgres creates a database called postgres is because : 
- If you ever want to connect with a posgres instance you need to specify a database that you want to connect to.
- This is the reason why post installation postgres gives a default database called postgres.
- You can't connect to postgres you have to specify a database.

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

#### write an api end-point in main.py file to create a blog 
```
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
```
### **Explanation of Key Concepts in the Code:**

---

### **What is `Depends`?**
- **What it is:** `Depends` is a utility provided by FastAPI to declare dependencies for a route handler.
- **How it works:** 
  - It allows injecting reusable logic (e.g., database sessions, authentication checks, etc.) into route handlers.
  - In the given code, `Depends(get_session)` is used to provide a session to the `create_blog` endpoint without manually managing the session lifecycle.
- **Purpose:** Simplifies dependency injection and ensures better modularity and cleaner code.

---

### **What is `Session`?**
- **What it is:** `Session` is a class from `sqlmodel` (built on top of SQLAlchemy) used to interact with the database.
- **How it works:**
  - It acts as a connection to the database and provides methods to perform operations like querying, adding, committing, and rolling back transactions.
- **Role in the code:** It is used to interact with the database when creating or modifying data.

---

### **What is `engine`?**
- **What it is:** `engine` is a SQLAlchemy `Engine` object, which manages the database connection.
- **How it works:**
  - It encapsulates the connection details, such as the database URL, and handles creating connections to the database as needed.
- **Role in the code:** It is passed to `Session` and `SQLModel` for establishing connections and performing database operations.

---

### **What is `SQLModel`?**
- **What it is:** `SQLModel` is a Python ORM (Object-Relational Mapper) library built on top of SQLAlchemy.
- **How it works:**
  - It allows you to define database tables as Python classes and interact with the database using these models.
  - Models inherit from `SQLModel`, and the library generates SQL queries behind the scenes.
- **Role in the code:** `BlogModel` is a subclass of `SQLModel`, representing a database table.

---

### **What is `SQLModel.metadata.create_all(engine)`?**
- **What it does:** 
  - It creates database tables based on the `SQLModel` models defined in the code.
- **How it works:**
  - `SQLModel.metadata` contains the schema definitions for all the models.
  - `create_all(engine)` generates the SQL commands (like `CREATE TABLE`) and executes them against the connected database.
- **Role in the code:** Ensures all required tables are created when the application starts.

---

### **What does the code below do?**
```python
with Session(engine) as session:
    yield session
```
- **What it does:** 
  - Creates a session (database connection) tied to the `engine`, ensuring proper resource management.
  - The `yield` keyword makes it a generator, allowing FastAPI to use this function as a dependency.
  - Once the session is used, it is automatically closed after the request is processed.
- **How it works:**
  - `with Session(engine)` manages the session lifecycle, opening and closing the connection safely.
  - The `yield` statement provides the session to the endpoint logic.

---

### **What is `on_event` and `"startup"`?**
- **What it is:** `@app.on_event("startup")` is a FastAPI event hook for performing actions when the application starts.
- **How it works:**
  - The `"startup"` event is triggered when the FastAPI app starts running.
  - The decorated function (`on_startup`) runs during this event.
- **Role in the code:**
  - Ensures the database tables are created before any endpoint is accessed by calling `create_db_and_tables()`.

---

### **Why is `"Z"` added in the front-end API endpoint?**
- **What it is:** `"Z"` represents "Zulu time," another name for UTC time, as per ISO 8601 format.
- **How it works:**
  - When the front-end sends a timestamp, it often uses UTC (coordinated universal time) for consistency across time zones.
  - `"Z"` signifies that the timestamp is in UTC.
- **Role in the code:** The `created_at` field is converted from an ISO 8601 string (with `"Z"`) to a Python `datetime` object using:
  ```python
  blog.created_at = datetime.datetime.fromisoformat(blog.created_at.replace("Z", "+00:00"))
  ```
  This replaces `"Z"` with the timezone offset `+00:00`.

---

### **What does the following code do?**
```python
session.add(blog)
session.commit()
session.refresh(blog)
```
- **`session.add(blog)`**
  - Adds the `blog` object to the database session, marking it for insertion into the database.
- **`session.commit()`**
  - Commits the transaction, saving the changes (e.g., inserting the blog) permanently into the database.
- **`session.refresh(blog)`**
  - Reloads the `blog` object from the database to update it with any changes made during the commit (e.g., auto-generated fields like `id`).
- **Role of `session`:** 
  - Manages the transaction lifecycle and database operations.
  - Ensures safe and consistent interaction with the database.











