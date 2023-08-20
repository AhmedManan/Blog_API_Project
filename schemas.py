from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title:str
    body:str
    author:str
    tags:str
    # published: Optional [bool] = False

class ShowBlog(Blog):
    pass
