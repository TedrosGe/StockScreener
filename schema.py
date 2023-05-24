from fastapi import FastAPI
from pydantic import BaseModel


class Symbol(BaseModel):
    id: str
