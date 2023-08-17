from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from mysql.connector import connect


# MySQL Database Configuration
DATABASE_URL = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "",
    "database": "fastapi_db"
}

engine = create_engine(
    f"mysql+mysqlconnector://{DATABASE_URL['user']}:{DATABASE_URL['password']}@{DATABASE_URL['host']}:{DATABASE_URL['port']}/{DATABASE_URL['database']}")

# SQLALCHEMY_DATABASE_URL="mysql://root@localhost:3306/fastapi_db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()