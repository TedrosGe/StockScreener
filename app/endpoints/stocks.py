from fastapi import APIRouter
from app.services.home import add_tickers, fetch_tickers
router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

@router.get("/home")
async def display_stocks():
    add_tickers()
    stocks = fetch_tickers()
    

    return {"message": stocks}
