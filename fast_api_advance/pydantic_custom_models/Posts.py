from datetime import date

# import pydantic
from pydantic import BaseModel, Field
from typing import Optional

class PostsModel(BaseModel):
    id:int
    title:str
    content: str
    is_published : bool = True
    rating : int = 0
    is_deleted : bool = False

    