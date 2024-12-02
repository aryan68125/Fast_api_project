#datetime imports
from datetime import date

#import pydantic
from pydantic import BaseModel, Field

#Pydantic model
class Blogs(BaseModel):
    title: str
    content:str
    created_by:int
    created_at:date = Field(default_factory=date.today)
    updated_at:date
    is_deleted:bool = Field(default_factory=False)