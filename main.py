from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Blog API."}

@app.get("/posts")
def get_posts():
    return {"Title": "Post1"}

@app.post("/create_post")
def create_post(payload: dict = Body(...)):
    print(payload)
    return payload