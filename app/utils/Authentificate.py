
from datetime import datetime, timedelta, timezone
from typing import Annotated
import bcrypt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models.models import Token, TokenData, User
from passlib.context import CryptContext

from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel, ValidationError

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Authentificate():

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
   
    @staticmethod
    def create_jwt_token(data: dict, expires_delta: timedelta |None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc)+ timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        access_token = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)
        
        return Token(access_token= access_token, token_type= "bearer")
    
    @staticmethod
    def token_expiration():
        token_expiration_time = timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
        return token_expiration_time
    
    
    @staticmethod
    def decode_jwt_token(token):
        creadential_exception = HTTPException(
             status_code= status.HTTP_401_UNAUTHORIZED,
             detail= "invalidate credential",
             headers={"WWW-Authenticate": "Bearer"}
         )
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise creadential_exception
        
        token_data = TokenData(username= username)
        # user = get_user(token_data.username, db)
        return TokenData
    @staticmethod
    
    def hash_password(password: str):
        return Authentificate.pwd_context.hash(password)
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return Authentificate.pwd_context.verify(plain_password,hashed_password)
    
    @staticmethod
    def authenticate_user(username, password, db: Session):
        user = db.query(User).filter(User.username ==username).first()
   
        if not user:
            return False
        
        if not  Authentificate.verify_password(password, user.password):
            return False

        return user
    