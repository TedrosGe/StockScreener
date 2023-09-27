
from fastapi import APIRouter, Depends, BackgroundTasks
from app.database.database import SessionLocal
from app.services.home import  add_stock_ticker, fetch_tickers, fetch_tickers_api, filtered_tickers, get_db, populate_stock_table
from app.services.stocks import fetch_stock_db, populate_stock_detail_table
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
import time
import csv
import json


router = APIRouter()

@router.post("/initialise-database")
async def initialize_database(db:Session() =Depends(get_db)):
    # #fetch and filter valid tickers
    # ticker_list = fetch_tickers_api()
    # valid_tickers = filtered_tickers(ticker_list)
    # with open("app/database/tickers.json",) as f:
    #     data= json.loads(f.read())
    # valid_tickers = data["tickers"]
    # add_stock_ticker(valid_tickers, db)
    # #populate table stock
    # populate_stock_table(db)
    # populate table stock_details for all tickers
    start = time.time()

    populate_stock_detail_table(db)
    stop = time.time()
    execution_time = stop-start
    print(execution_time)
    return{"Tables Stock and Stock_detail": execution_time}

@router.get("/")
async def root(db: Session= Depends(get_db)):
      stocks = fetch_tickers()
      return stocks
@router.post("/")
async def home(background_tasks: BackgroundTasks, db:Session() =Depends(get_db)):  

     
    return {"status":"stocks"}


@router.get("/home/{stock}", tags=["GET"])
async def fetch_stock_details(stock:str):
    pass


@router.post("/home/{stock}", tags = ["POST"])
async def  stock_details(stock:str):
  pass

