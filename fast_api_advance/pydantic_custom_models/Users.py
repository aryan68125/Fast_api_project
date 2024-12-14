from datetime import datetime

# import pydantic 
from pydantic import BaseModel , Field, EmailStr
from typing import Optional

class CreateUpdateUserModel(BaseModel):
    email : EmailStr
    password : str

class BlockUnblockUsersModel(BaseModel):
    is_blocked : bool

class SoftDeleteRestoreUserModel(BaseModel):
    is_deleted : bool

class CreateUpdateUserResponse(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime
    is_deleted : bool
    is_blocked : bool

    class Config:
        orm_mode = True