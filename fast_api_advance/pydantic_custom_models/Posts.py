from datetime import date

# import pydantic
from pydantic import BaseModel, Field
from typing import Optional

# POST APP PYDANTIC MODEL STARTS
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
    id:int = None
    rating : int = 0

class SoftDeleteRestorePostsModel(BaseModel):
    is_deleted : bool

class HardDeletePostsModel(BaseModel):
    id:int
# POST APP PYDANTIC MODEL ENDS
    