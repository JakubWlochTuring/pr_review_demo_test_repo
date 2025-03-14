from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

class User(UserBase):
    id: Optional[int] = None
    password: str
    disabled: Optional[bool] = False