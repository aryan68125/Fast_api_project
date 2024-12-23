from pydantic_custom_models.Token import TokenData
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from utility.generate_token import SECRET_KEY, ALGORITHM
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/auth/login")

'''
This function is used to verify the access token that we get from the front-end and if the token is invalid then it will raise and exception.
credentials_exception = 
'''
def verify_access_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id = payload.get('id')
        print(f"verify_access_token-> id : {id}")
        if id is None:
            raise credentials_exception
        #validate the data using pydantic model
        token_data = TokenData(id=id)
        print(f"verify_access_token -> token_data : {token_data}")
        return token_data
    except Exception as e:
        print(f"verify_access_token : {e}")
        return credentials_exception

'''
This function could be passed into the Path operations or our FastAPI end-point as a Dependency.
This function will be used to get the get the user from the token that we get from the front-end after validating the token.
Is gonna verify the token by using verify_access_token function

tokenurl = "login end-point

Anytime we have aspecific end-point that is to be protected the needs to be logged in to use it.
What we are gonna do it is we can just add in an extra dependency to the path operation function 
'''
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_access_token(token, credentials_exception)
