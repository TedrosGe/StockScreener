from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.endpoints import stocks
from app.database.database import Base, create_tables


app = FastAPI()

app.include_router(stocks.router)
origins = [
    'http://localhost:3000'
]
#add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
create_tables()