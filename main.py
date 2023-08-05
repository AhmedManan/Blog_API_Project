from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Blog API."}

@app.get("/posts")
def get_posts():
    return {"Title": "Post1"}