


from sqlalchemy import create_engine
from stocksymbol import StockSymbol
from sqlalchemy.orm import Session
from pydantic import BaseModel
import yfinance as yf
import pandas as pd
from app.models.models import Stock, StockDetail
from app.database.database import Base, engine, SessionLocal
import concurrent.futures
def populate_stock_detail_table(db:Session):
   
        stock = db.query(Stock).all()
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(update_stock_detail, stock,db))
       
  


     
def update_stock_detail(stock:Stock, db:Session()):   # type: ignore
   
    df = fetch_stock_api(stock.ticker)
    df_to_sql(df,stock.ticker)
    
    return {"stock_detail updated": {stock.ticker}}

def fetch_stock_api(symbol):
    with SessionLocal() as session:
       
        tick= yf.Ticker(symbol)
        df = tick.history(period="1y")
        df.index = pd.to_datetime(df.index)
        df.index = df.index.date
    return df

def df_to_sql(df: pd.DataFrame, symbol):
    session= SessionLocal()
    #fetch stock to update
    stocks = session.query(Stock).filter(Stock.ticker ==symbol).first()
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


def fetch_stock_db(symbol,db:Session):
  
    stock = db.query(Stock).filter(Stock.ticker ==symbol).first()
    
    return stock


def fetch_stock_history(symbol,db:Session):
    sql_query = db.query(StockDetail).join(Stock, StockDetail = Stock.id).filter(Stock.ticker ==symbol).all()

    return sql_query