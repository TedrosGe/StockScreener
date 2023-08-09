from fastapi import APIRouter, Depends, BackgroundTasks
from app.services.home import  add_stock_ticker, fetch_tickers, fetch_tickers_api, get_db, populate_stock_table
from app.services.lookup import fetch_stock_db, stock_history
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
router = APIRouter()

@router.get("/")
async def root(db: Session =Depends(get_db)):  
    ticker_list = fetch_tickers_api()
    add_stock_ticker(ticker_list, db)
    populate_stock_table(db)  
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

