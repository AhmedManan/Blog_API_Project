from fastapi import APIRouter
import database, schemas, models, oauth2
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUserDetails)
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUserDetails)
def get_user(id:int,db: Session = Depends(get_db)):
    return user.show(id,db)

@router.get("/user/info")
def user_info():
    pass
