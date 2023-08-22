from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    author = Column(String)
    tags = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)  # Fixed typo here
    password = Column(String)
    user_type = Column(String)  # Renamed "type" to "user_type"
    status = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())