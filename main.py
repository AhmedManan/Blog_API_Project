from fastapi import FastAPI, Depends, status, Response, HTTPException
from typing import List
import models, schemas, hashing
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI(
    openapi_prefix="",
    title="Blog API",
    version="1.0.0",
    description="This API is Created by the developer Manan Ahmed Broti. Not for commercial purpose. The Base URL for this API is set to: https://blog-rhhb.onrender.com/",
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

@app.get('/blog', response_model=List[schemas.ShowBlog], tags=['Blogs'])
def all_posts(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.post('/blog', status_code = 201, tags=['Blogs'])
def create_post(request : schemas.Blog, db : Session = Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog/{blog_id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=['Blogs'])
def get_post(blog_id, response : Response, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id== blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Post not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'Details':'Blog post not found!'}
    return blog

@app.put('/blog/{blog_id}', status_code=status.HTTP_202_ACCEPTED, tags=['Blogs'])
def update_post(blog_id, request : schemas.Blog, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id== blog_id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Post with ID={blog_id} not found')
    
    blog.update(request.title,request.body)
    db.commit()
    return 'updated successfully'


@app.delete('/blog/{blog_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Blogs'])
def delete_post(blog_id, db : Session = Depends(get_db)):
        blog = db.query(models.Blog).filter(models.Blog.id== blog_id)

        if not blog.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Post with ID={blog_id} not found')
        
        blog.delete(synchronize_session=False)
        db.commit()
        return {f'Blog post deleted!'}

@app.post('/user', status_code = 201, tags=['User'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # hashed_password = pwd_context.hash(request.password)  # Hash the password

    user_data = request.dict()
    user_data["password"] = hashing.Hash.bcrypt(request.password)

    new_user = models.User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.get('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser, tags=['User'])
def get_post(user_id:int, response : Response, db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id== user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'Details':'Blog post not found!'}
    return user