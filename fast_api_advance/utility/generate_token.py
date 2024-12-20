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
