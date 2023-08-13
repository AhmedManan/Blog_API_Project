from fastapi import FastAPI
from typing import Optional
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class post(BaseModel):
    title: str
    content: str
    published: bool =True

@app.get("/")
async def root():
    return {"message": "Welcome to the Blog API. Developed By MAnan Ahmed Broti. Website: AhmedManan.com"}

@app.get("/blog")
def index(limit = 10, published: bool=True, sort: Optional[str]= None):
    if published:
        return {f'{limit} published posts'}
    else:
        return {f'{limit} posts'}
    
class Blog(BaseModel):
    title:str
    body:str
    published: Optional [bool]
    
@app.post("/blog")
def index(request: Blog):
    return {f'Blog is created'}


@app.get("/blog/unpublished")
def show():
    # fetch blog where id = id
    return {'post': 'all unpublished blogs'}

@app.get("/blog/{id}")
def show(id:int):
    # fetch blog where id = id
    return {'post': id}


@app.get("/blog/{id}/comments")
def comments(id):
    # fetch comments where blog id = id
    return {'ok'}