from functools import lru_cache
import json
from fastapi import Depends, HTTPException, BackgroundTasks
from sqlalchemy import create_engine
from stocksymbol import StockSymbol
import yfinance as yf
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.models.models import Stock, StockDetail
from app.database.database import Base, engine, SessionLocal
import concurrent.futures
def get_db():
    db = SessionLocal()

    return db

def fetch_tickers_api():
    api_key = 'cf7959df-216f-461a-a735-0e3fe089d675'  
    ss = StockSymbol(api_key)
    us_ticker_list = ss.get_symbol_list("us")
    symbols = [ stock_dic['symbol']for stock_dic in us_ticker_list]
    return symbols

def add_stock_ticker(ticker_list: list, db:Session):
    #fetch all existing sql stock  tickers  
    ticker_exists = db.query(Stock.ticker).all()

    if ticker_exists is None: 
        tickers_to_added =[ Stock(ticker= symbol) for symbol in ticker_list ]
    else:
        tickers_in_db = [ticker[0] for ticker in ticker_exists]
            
        tickers_to_added =[ Stock(ticker= symbol) for symbol in ticker_list if symbol not in tickers_in_db ]
    db.bulk_save_objects(tickers_to_added)
    db.commit()
    return
def get_stock_info(ticker:Stock.ticker)-> dict:
    if stock_exists(ticker):
        tic = yf.Ticker(ticker)
        dic = tic.info
        return dic
    return {}
def stock_exists(ticker:Stock.ticker)-> bool:
    try:
        # Fetch data for the ticker
        stock = yf.Ticker(ticker)
        
        
        # If the historical data is empty, return False
        if stock.info == None :
            return False
        
        return True
    except Exception as e:
        print(f"An error occurred: {ticker}")
        return False

def update_stock(stock:Stock):  
    db = SessionLocal()
    try:
        stock_dict = yf.Ticker(stock.ticker).info
        if stock_dict:
                stock.company = stock_dict.get("longName")
                stock.industry = stock_dict.get("industry")
                stock.marketCap = stock_dict.get("marketCap", None)
                stock.recommendationMean = stock_dict.get("recommendationMean", 0)
                stock.forwardPE = stock_dict.get("forwardEps", None)
                stock.high = stock_dict.get("dayHigh", None)
                stock.low = stock_dict.get("dayLow", None)
                stock.volume = stock_dict.get("volume")
                stock.currentPrice = stock_dict.get("currentPrice")
                stock.fiftyTwoWeekLow = stock_dict.get("fiftyTwoWeekLow", None)
                stock.fiftyTwoWeekHigh = stock_dict.get("fiftyTwoWeekHigh", None)
        
            
            
    except Exception as e:
        print(f"Error updating stock with ticker {stock.ticker}: {e}")
        return False
def load_tickers_from_file(file_path):
    with open(file_path,) as f:
        data = json.loads(f.read())
    return data["tickers"]

def add_tickers_to_db(tickers, db_session):
    add_stock_ticker(tickers, db_session)
    populate_stock_table(db_session)

def populate_stock_table(db:Session):
   
        stocks = db.query(Stock).all()
        print("concurrent started")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(update_stock, stocks))
        print("concurrency done")  
        db.commit()
        print("db comitted")


def fetch_tickers( session:Session =Depends(get_db)):
    
    session = SessionLocal()
    tickers = session.query(Stock).all()
    
    return tickers

def  filtered_tickers(tickers):

    valid_tickers = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(is_valid_ticker, tickers))

    for idx, result in enumerate(results):
        if result:
            valid_tickers.append(tickers[idx])

    return valid_tickers
def is_valid_ticker(ticker: str) -> bool:
    try:
        stock = yf.Ticker(ticker)
        if stock.info is not None:
            return True
        return False
    except:
        return False


