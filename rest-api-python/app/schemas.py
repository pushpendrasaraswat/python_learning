from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime

from app import models


class PostBase(BaseModel):
    title: str
    content: str
    published : bool = True
    rating: Optional[int] = None  # Optional field, default is None


class PostCreate(PostBase):
    pass

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    model_config = ConfigDict(from_attributes=True)
    owner: UserResponse


class UserBase(BaseModel):
    email: EmailStr
    password: str



class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id : Optional[int] = None