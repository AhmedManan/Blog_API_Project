from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class UpdateBlog(BaseModel):
    title: str
    body: str
    class Config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUserDetails(BaseModel):
    name: str
    email: str
    created_at: datetime  # Add created_at field
    updated_at: datetime  # Add updated_at field

    class Config:
        orm_mode = True

class ShowUserBlogs(BaseModel):
    name: str
    email: str

    blogs: List[Blog] = []

    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body:str
    created_at: datetime  # Add created_at field
    updated_at: datetime  # Add updated_at field
    creator: ShowUserDetails

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None