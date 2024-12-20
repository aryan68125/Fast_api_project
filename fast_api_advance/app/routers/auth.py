from fastapi import APIRouter ,Depends,status

#import sql alchemy database handler
from database_handler.sql_alchemy_db_handler import Base, db_flush,db_engine
from sqlalchemy.orm import Session
#import sql alchemy models
from .. import sql_alchemy_models

# import pydantic model 
from pydantic_custom_models.Auth import LoginModel

#import password hashing function
from utility.hash_password import hash_reset_pass_fun, verify_hash_password

#import error message utils
from utility.common_error_messages import PASSWORD_MATCH_ERR,DATA_NOT_FOUND_ERR, INVALID_CREDS_ERR

#import success message utils 
from utility.common_success_messages import LOGIN_SUCCESS

#import generate token function
from utility.generate_token import generate_auth_token

#import response from common_response
from utility.common_response import response

# This allows us to retrieve the user's credetials using this FastAPI utility instead of recieving them in the body
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["User Authentication"]
)

sql_alchemy_models.Base.metadata.create_all(bind=db_engine)

@router.post("/login")
def login_user(login_model : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(db_flush)):
    user = db.query(sql_alchemy_models.UserMaster).filter(sql_alchemy_models.UserMaster.email == login_model.username).first()
    
    if not user:
        return response(status=status.HTTP_404_NOT_FOUND,error=INVALID_CREDS_ERR)
    if_password_matched = verify_hash_password(login_model.password, user.password)
    if not if_password_matched:
        return response(status=status.HTTP_400_BAD_REQUEST,error=PASSWORD_MATCH_ERR)
    user_data = {
        "id":user.id,
    }
    generated_token = generate_auth_token(user_data)
    return response(status=status.HTTP_200_OK,message=LOGIN_SUCCESS,data=generated_token)
    