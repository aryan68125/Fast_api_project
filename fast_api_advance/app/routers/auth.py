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

router = APIRouter(
    prefix="/auth",
    tags=["User Authentication"]
)

sql_alchemy_models.Base.metadata.create_all(bind=db_engine)

@router.post("/login")
def login_user(login_model : LoginModel, db : Session = Depends(db_flush)):
    login_dict = login_model.model_dump()
    user = db.query(sql_alchemy_models.UserMaster).filter(sql_alchemy_models.UserMaster.email == login_dict.get("email")).first()
    
    if not user:
        return response(status=status.HTTP_404_NOT_FOUND,error=INVALID_CREDS_ERR)
    if_password_matched = verify_hash_password(login_dict.get("password"), user.password)
    if not if_password_matched:
        return response(status=status.HTTP_400_BAD_REQUEST,error=PASSWORD_MATCH_ERR)
    generated_token = generate_auth_token(user)
    return response(status=status.HTTP_200_OK,message=LOGIN_SUCCESS,data=generated_token)
    