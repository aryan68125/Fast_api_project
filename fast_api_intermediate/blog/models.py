from datetime import datetime
from sqlmodel import SQLModel, Field

class BlogModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    body: str | None = Field(default=None, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)  # Set to current UTC time
    created_by: int
