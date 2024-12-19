from pydantic import EmailStr, BaseModel, Field

class LoginModel(BaseModel):
    email = EmailStr
    password = str