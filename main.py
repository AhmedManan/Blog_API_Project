from fastapi import FastAPI, Depends, status, Response, HTTPException
from typing import List
import models, schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI(
    openapi_prefix="",
    title="Blog API",
    version="1.0.0",
    description="This API is Created for testing, by the developer. Not for commercial purpose. Thank you!",
)
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", status_code=status.HTTP_200_OK)
async def credits():
    return {"message": "Welcome to the Blog API. Developed By MAnan Ahmed Broti. Website: AhmedManan.com"}

@app.get('/blog', response_model=List[schemas.ShowBlog])
def all_posts(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.post('/blog', status_code = 201)
def create_post(request : schemas.Blog, db : Session = Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog/{blog_id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_post(blog_id, response : Response, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id== blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Post not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'Details':'Blog post not found!'}
    return blog

@app.put('/blog/{blog_id}', status_code=status.HTTP_202_ACCEPTED)
def update_post(blog_id, request : schemas.Blog, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id== blog_id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Post with ID={blog_id} not found')
    
    blog.update(request.title,request.body)
    db.commit()
    return 'updated successfully'


@app.delete('/blog/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(blog_id, db : Session = Depends(get_db)):
        blog = db.query(models.Blog).filter(models.Blog.id== blog_id)

        if not blog.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Post with ID={blog_id} not found')
        
        blog.delete(synchronize_session=False)
        db.commit()
        return {f'Blog post deleted!'}

@app.post('/user')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(**request.dict())  # Use the constructor to create a new instance
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user