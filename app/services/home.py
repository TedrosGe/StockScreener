from functools import lru_cache
from fastapi import Depends, HTTPException, BackgroundTasks
from sqlalchemy import create_engine
from stocksymbol import StockSymbol
import yfinance as yf
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.models.models import Stock, StockDetail
from app.database.database import Base, engine, SessionLocal

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

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
         
def populate_stock_table(db:Session):

        records = []
        stocks = [ stock[0] for stock in db.query(Stock).all()]
        for stock in stocks:
            stock_dict = get_stock_info(stock)
            new_stock = Stock()
            new_stock.ticker = stock_dict.get('symbol')
            new_stock.company = stock_dict.get("longName")
            new_stock.industry = stock_dict.get("industry"),
            new_stock.marketCap = stock_dict.get("marketCap",None),
            new_stock.recommendationMean = stock_dict.get("recommendationMean",0),
            new_stock.forwardPE =  stock_dict.get("forwardEps",None),
            new_stock.high = stock_dict.get("dayHigh",None),
            new_stock.low = stock_dict.get( "dayLow",None),
            new_stock.volume = stock_dict.get("volume"),
            new_stock.currentPrice = stock_dict.get("currentPrice"),
            new_stock.fiftyTwoWeekLow = stock_dict.get("fiftyTwoWeekLow",None),
            new_stock.fiftyTwoWeekHigh = stock_dict.get("fiftyTwoWeekHigh",None)
                            
            records.append(new_stock)
            stock_dict = {}   
            

        db.bulk_save_objects(records)    
        db.commit()    
        db.close()

        return
def get_stock_info(ticker:str)-> dict:
     tic = yf.Ticker(ticker)
     dic = tic.info
     return dic


def fetch_tickers( session:Session =Depends(get_db)):
    
    session = SessionLocal()
    tickers = session.query(Stock).all()
    
    return tickers

