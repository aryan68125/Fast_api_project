from pydantic import BaseModel
from typing import Optional

class ValidateToken(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None

class RefreshToken(BaseModel):
    refresh_token : str
