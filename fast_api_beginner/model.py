from pydantic import BaseModel
from typing import Optional

class BlogModel(BaseModel):
    title:str
    body:str
    published_at :Optional[bool] = False