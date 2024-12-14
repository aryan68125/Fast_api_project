from datetime import date

# import pydantic
from pydantic import BaseModel, Field
from typing import Optional

# POST APP PYDANTIC MODEL STARTS
# defining requests using pydantic model starts
class InsertPostsModel(BaseModel):
    title:str
    content: str
    is_published : bool = True

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
# defining requests using pydantic model ends



# defining response using pydantic model starts

# defining response using pydantic model ends
# POST APP PYDANTIC MODEL ENDS
    