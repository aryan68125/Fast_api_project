#import user password encryption libraries
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_pass_fun(UserModel):
    hashed_password = pwd_context.hash(UserModel.password)
    UserModel.password = hashed_password
    return UserModel

def hash_reset_pass_fun(password: str):
    hashed_password = pwd_context.hash(password)
    return hashed_password
