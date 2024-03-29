

from fastapi import Depends
from sqlalchemy.orm import Session, sessionmaker
from app.models.models import User, UserIn, UserOut
from app.database.database import Base, engine, SessionLocal
from app.services.home import get_db
from app.utils.Authentificate import Authentificate



class UserManager:

    def create_user( user: UserIn, db: Session): # type: ignore
        encoded_password= Authentificate.hash_password(user.password)
        print("hashed_password:",encoded_password)
        new_user = User(username = user.username, email = user.email, password = encoded_password)
        db.add(new_user)
        db.commit()
        print("new user added")
       
        return { "user": user}
    
    def get_user(username, db:Session):
        user = db.query(UserIn).filter(UserIn.username ==username).first()



        return UserOut(username= user.username, email = user.email)