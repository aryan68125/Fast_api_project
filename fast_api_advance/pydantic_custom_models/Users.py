from datetime import datetime

# import pydantic 
from pydantic import BaseModel , Field
from typing import Optional

class CreateUpdateUserModel(BaseModel):
    email : str
    password : str

class BlockUnblockUsersModel(BaseModel):
    is_blocked : bool

class SoftDeleteRestoreUserModel(BaseModel):
    is_deleted : bool