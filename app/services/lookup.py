
from sqlalchemy import create_engine
from stocksymbol import StockSymbol
import yfinance as yf
import pandas as pd
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from app.models.models import Stock, StockDetail
from app.database.database import Base, engine, SessionLocal

def stock_history(symbol):
    
    df,symbol = fetch_stock_api(symbol)
    df_to_sql(df,symbol)
    
    return {"stock": {symbol}}

def fetch_stock_api(symbol):
    with SessionLocal() as session:
        stock = session.query(Stock).first()
        
        records = []
    
        tick= yf.Ticker(symbol)
        df = tick.history(period="1y")
        df.index = pd.to_datetime(df.index)
        df.index = df.index.date
        
    return df, symbol

def df_to_sql(df: pd.DataFrame, symbol):
    session= SessionLocal()
    stocks = session.query(Stock).filter(Stock.ticker ==symbol).first()
    if not stocks:
         session.close()
         raise ValueError(f"no stock found")
    records = []
    for index, row in df.iterrows():
            
            stock_detail = StockDetail( stock_id = stocks.id,
                                       date = str(index),
                                       close = row["Close"],      
                                       open = row [ "Open"], 
                                       high = row["High"],
                                       low = row["Low"],
                                       volume = row["Volume"]
                                       )
            
            records.append(stock_detail)
        
            
    session.bulk_save_objects(records)
    session.commit()
    session.close()


def fetch_stock_db(symbol):
    session = SessionLocal()
    id = session.query(Stock.id).filter(Stock.ticker ==symbol)
    stock_history = session.query(StockDetail).filter(StockDetail.stock_id ==id).all()
 
    return stock_history

