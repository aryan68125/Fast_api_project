from datetime import date

# import pydantic
from pydantic import BaseModel, Field
from typing import Optional

class InsertPostsModel(BaseModel):
    title:str
    content: str
    is_published : bool = True
    rating : int = 0

class UpdatePostsModel(BaseModel):
    id:int = None
    title:str
    content: str
    is_published : bool = True

class RatingPostsModel(BaseModel):
    id:int = None
    rating : int = 0

class SoftDeleteRestorePostsModel(BaseModel):
    id:int
    is_deleted : bool

class HardDeletePostsModel(BaseModel):
    id:int
    