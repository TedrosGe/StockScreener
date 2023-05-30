from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
curr_path = os.path.abspath(os.getcwd()).join("/database/database.db")

SQLALCHEMY_DATABASE_URL = "sqlite:///app/database/database.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_tables():
    print("sqlite:///"+curr_path)
    Base.metadata.create_all(bind = engine)
    