

from fastapi import Depends
from sqlalchemy.orm import Session, sessionmaker
from app.models.models import User, UserIn, UserOut
from app.database.database import Base, engine, SessionLocal
from app.services.home import get_db


class UserManager:

    def create_user( user: UserIn, db: Session): # type: ignore
        user.hash_password()
        new_user = User(username = user.username, email = user.email, password = user.password)
        db.add(new_user)
        db.commit()
        print("new user added")
       
        return { "user": user}