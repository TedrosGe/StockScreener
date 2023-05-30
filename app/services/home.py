from sqlalchemy import create_engine
from stocksymbol import StockSymbol
import yfinance as yf
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

from app.models.models import Stock, StockDetail
from app.database.database import Base, engine, SessionLocal

def add_tickers():
    session = SessionLocal()
    api_key = 'cf7959df-216f-461a-a735-0e3fe089d675'  
    ss = StockSymbol(api_key)
    us_ticker_list = ss.get_symbol_list("us")
    for i in us_ticker_list:
       
        ticker = Stock(ticker= i["symbol"], company =i["longName"])

        session.add(ticker)
    session.commit()
 
    session.close()
    return

def fetch_tickers( ):
    session = SessionLocal()
    tickers = session.query(Stock).filter(Stock.id).all
    return tickers