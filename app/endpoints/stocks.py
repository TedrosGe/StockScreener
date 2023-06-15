from fastapi import APIRouter
from app.services.home import  fetch_tickers, add_tickers
from app.services.lookup import stock_history
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

@router.get("/lookup")
async def trending_tickers():
    add_tickers()
    stocks = fetch_tickers()
    return {"stocks":stocks}

@router.get("/lookup/stock")
async def  stock_details():
    x = stock_history()
    return{"stocks:": x}