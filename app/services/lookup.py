
from sqlalchemy import create_engine
from stocksymbol import StockSymbol
import yfinance as yf
import pandas as pd
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from app.models.models import Stock, StockDetail
from app.database.database import Base, engine, SessionLocal

def stock_history():
    with SessionLocal() as session:
        stock = session.query(Stock).first()
        
        records = []
    
        tick= yf.Ticker("TSLA")
        df = tick.history(period="1y")
        df.index = pd.to_datetime(df.index)
        df.index = df.index.date
        
        for index, row in df.iterrows():
            stock_detail = StockDetail(stock_id= stock.id,
                                       date = str(index),
                                       close = row["Close"], 
                                       open = row [ "Open"], 
                                       high = row["High"],
                                       low = row["Low"] )
            
            records.append(stock_detail)
        print(records)
            
    session.bulk_save_objects(records)
    session.commit()
    session.close()
    
    return { "stock_details":records}