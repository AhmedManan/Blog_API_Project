from fastapi import FastAPI, status
import models
from database import engine
from files.routers import blog, user, authentication



app = FastAPI(
    openapi_prefix="",
    title="Blog API",
    version="1.0.0",
    description="This API is Created by the developer Manan Ahmed Broti. Not for commercial purpose. The Base URL for this API is set to: https://blog-rhhb.onrender.com/",
)
models.Base.metadata.create_all(bind=engine)
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


@app.get("/", status_code=status.HTTP_200_OK)
async def credits():
    return {"message": "Welcome to the Blog API. Developed By Manan Ahmed Broti. Website: www.AhmedManan.com"}

