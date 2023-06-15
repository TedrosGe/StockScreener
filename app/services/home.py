from functools import lru_cache
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
    session = SessionLocal()

    try:
        for i in us_ticker_list:
            
            symbol = session.query(Stock).filter(Stock.ticker==i["symbol"]).first()
            if symbol:
                break
            ticker = Stock(ticker= i["symbol"], company =i["longName"])
            
            session.add(ticker)
        

    except Exception as e:
        print("error",e)
    finally:
        session.commit()    
        session.close()

    return

def fetch_tickers( ):
    session = SessionLocal()
    tickers = session.query(Stock).all()
    
    return tickers
