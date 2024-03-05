
from fastapi import APIRouter, Depends, BackgroundTasks
from app.database.database import SessionLocal
from app.models.models import Stock, User, UserOut,UserIn
from app.services.home import  add_stock_ticker, fetch_tickers, fetch_tickers_api, filtered_tickers, get_db, load_tickers_from_file, populate_stock_table
from app.services.stocks import fetch_stock_db, fetch_stock_history, populate_stock_detail_table
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
import time
import csv
import json

from app.services.user import UserManager


router = APIRouter()

@router.post("/initialise-database")
async def initialize_database(db:Session() =Depends(get_db)): # type: ignore
    #fetch filtered, valid tickers
    
    valid_tickers = load_tickers_from_file("app/database/tickers.json")
    add_stock_ticker(valid_tickers, db)
    #populate table stock
    populate_stock_table(db)
    start = time.time()
    populate_stock_detail_table(db)


    return{"stocks": "populated"}

@router.get("/home/{symbol}")
async def root(symbol: str, db = Depends(get_db)):
    stock = fetch_stock_db(symbol, db)
 
    return { "stocks": stock}

@router.post("/history/{symbol}")
async def home(symbol: str, background_tasks: BackgroundTasks, db:Session() =Depends(get_db)):   # type: ignore
    stockHistory =  fetch_stock_history(symbol, db)
    return {"status":stockHistory}


# @router.post("/home/{stock}", tags = ["POST"])
# async def  stock_details(stock:str):
#   pass


@router.post("/users/", response_model = UserOut)
async def create_user(user:UserIn, db: Session = Depends(get_db)) -> any:
    new_user = UserManager.create_user(user, db)

    return { "new_user": new_user}

