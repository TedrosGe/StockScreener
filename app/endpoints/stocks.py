from fastapi import APIRouter
from app.services.home import  fetch_tickers, add_tickers
from app.services.lookup import fetch_stock_db, stock_history
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
router = APIRouter()

@router.get("/")
async def root():    
    add_tickers()
    stocks = fetch_tickers()
    return {"stocks":stocks}


@router.get("/lookup/{stock}", tags=["GET"])
async def fetch_stock_details(stock:str):
    stock_history =fetch_stock_db(stock)
    return {"stocks": stock_history}


@router.post("/lookup/{stock}", tags = ["POST"])
async def  stock_details(stock:str):
    stock_data = stock_history(stock)
    return{"stocks:": stock_data}

