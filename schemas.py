from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title:str
    body:str
    author:str
    tags:str
    # published: Optional [bool] = False

class ShowBlog(BaseModel):
    title:str
    body:str
    author:str
    tags:str
    class config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str
    user_type:str
    status:str
