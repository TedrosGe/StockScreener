
import bcrypt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models.models import User

def authenticate_user(username, password, db:Session):
    user = db.query(User).filter(User.username ==username).first()
   
    if not user:
        return False
    
    if not  bcrypt.checkpw(password.encode('utf-8') ,user.password ):
        return False

    return user

def hash_password(password: str):
    hashed_password = password.encode('utf-8')
    
    return hashed_password
