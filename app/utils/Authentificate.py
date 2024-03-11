
from datetime import datetime, timedelta, timezone
from typing import Annotated

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

    @staticmethod
    def create_jwt_token(data: dict, expires_delta: timedelta |None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc)+ timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)
    @staticmethod
    def decode_jwt_token(token):
         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
         username = payload.get("sub")
         return username
    @staticmethod
    def token_expiration(expires_delta:timedelta | None =None):
        if expires_delta:
            token_expiration_time = timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
        return token_expiration_time