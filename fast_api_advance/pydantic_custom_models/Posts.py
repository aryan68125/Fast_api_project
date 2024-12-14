from datetime import date

# import pydantic
from pydantic import BaseModel, Field
from typing import Optional

# POST APP PYDANTIC MODEL : request STARTS
class InsertPostsModel(BaseModel):
    title:str
    content: str
    is_published : bool = True
    rating : int = 0

class UpdatePostsModel(BaseModel):
    title:str
    content: str
    is_published : bool = True

class RatingPostsModel(BaseModel):
    rating : int = 0

class SoftDeleteRestorePostsModel(BaseModel):
    is_deleted : bool

class HardDeletePostsModel(BaseModel):
    id:int
# POST APP PYDANTIC MODEL : request ENDS
    