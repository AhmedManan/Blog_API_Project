from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class user(Base):
    __tablename__='users'

    id = Column(Integer, primary_key = True, index=True)
    username = Column(String(50))

