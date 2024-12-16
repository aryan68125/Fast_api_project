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

class VerifyOTPUsersModel(BaseModel):
    id : int
    otp : int

class ResendOtp(BaseModel):
    id : int