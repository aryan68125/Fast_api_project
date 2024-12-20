import jwt
from datetime import datetime, timedelta
from decouple import config

import secrets

# Import the JWT secret key from environment variables
SECRET_KEY = secrets.token_urlsafe(50)  # Make sure to add this to your .env file
ALGORITHM = "HS256"

def generate_token(data: dict, expires_delta: timedelta):
    """
    Generate a JWT token with the given data and expiration time.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def generate_refresh_token(user):
    """
    Generate a refresh token for the user with a longer expiration time.
    """
    refresh_token_data = {"user_id": user["id"]}
    refresh_token = generate_token(refresh_token_data, timedelta(days=30))
    return refresh_token

def generate_auth_token(user: dict):
    """
    Generate access and refresh tokens for the user.
    Returns a dictionary containing the tokens.
    """
    access_token_data = {"user_id": user["id"]}
    access_token = generate_token(access_token_data, timedelta(minutes=30))
    refresh_token = generate_refresh_token(user)
    token_data = {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }
    return token_data

'''
This function is used to verify the access token that we get from the front-end and if the token is invalid then it will raise and exception.
'''
from pydantic_custom_models.Token import TokenData
def verify_access_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        id = payload.get('id')
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id)
    except Exception as e:
        print(f"verify_access_token : {e}")
        return credentials_exception

'''
This function could be passed into the Path operations or our FastAPI end-point as a Dependency.
This function will be used to get the get the user from the token that we get from the front-end after validating the token.
'''
def get_current_user()
