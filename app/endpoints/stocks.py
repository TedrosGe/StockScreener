import csv
import json
from fastapi import APIRouter, Depends, BackgroundTasks
from app.services.home import  add_stock_ticker, fetch_tickers, fetch_tickers_api, filtered_tickers, get_db, populate_stock_table

from app.services.lookup import fetch_stock_db, stock_history
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
router = APIRouter()

@router.get("/")
async def root(db: Session= Depends(get_db)):
      stocks = fetch_tickers()
      return stocks
@router.post("/home")
async def home(background_tasks: BackgroundTasks, db:Session() =Depends(get_db)):  
    # ticker_list = fetch_tickers_api()
    # valid_tickers = filtered_tickers(ticker_list)
    
    with open("app/database/tickers.json",) as f:
        data= json.loads(f.read())
    valid_tickers = data["tickers"]
    add_stock_ticker(valid_tickers, db)

    populate_stock_table(db)
     
    stocks = fetch_tickers()
     
    return {"status":stocks}


@router.get("/lookup/{stock}", tags=["GET"])
async def fetch_stock_details(stock:str):
    stock_history = fetch_stock_db(stock)
    return {"stocks": stock_history}


@router.post("/lookup/{stock}", tags = ["POST"])
async def  stock_details(stock:str):
    stock_data = stock_history(stock)
    return{"stocks:": stock_data}

