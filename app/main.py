from fastapi import FastAPI
from sqlalchemy import Engine
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.endpoints import stocks
from app.database.database import Base, create_tables


app = FastAPI()

app.include_router(stocks.router)

create_tables()