from datetime import datetime
from sqlmodel import SQLModel , Field

class BlogModel(SQLModel,table=True):
    id: int | None = Field(default=None,primary_key=True)
    title: str | None = Field(index=True)
    body : str | None = Field(default = None,index=True)
    created_at = datetime = Field(default_factory=datetime.now)
    is_deleted = boolean | None = Field(default_factory=False)