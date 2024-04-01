


from sqlalchemy import create_engine, desc, func
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
    stock_id = db.query(Stock.id).filter(Stock.ticker ==symbol).first()
    if stock_id:
         stock_id = stock_id[0]
   
   
    stock_history = db.query(StockDetail).filter(StockDetail.stock_id ==stock_id).all()

    return {"stock_history": stock_history}


def fetch_max_change_stocks(db:Session):
    sub = (
        db.query(
            StockDetail,
            func.row_number().over(
                partition_by=StockDetail.stock_id,
                order_by=desc(StockDetail.date)
            ).label('row_number')
        )
        .subquery()
    )

    #   get the last two most recent close elements for each stock_id
    query = (
        db.query(Stock.ticker, sub.c.stock_id, sub.c.date, sub.c.close).join(sub, Stock.id ==sub.c.stock_id)
        .filter(sub.c.row_number <= 2)
        .order_by(sub.c.stock_id, sub.c.date.desc())
    )

    results = query.all()
    print(results)
    results_dict = {}

    for ticker, stock_id, date, close in results:
        if stock_id in results_dict:
              results_dict[stock_id].append([date, close])
        else:
            results_dict[stock_id] =  [[ticker],[date,close]]
            #calculate percent change for close price
    for id in results_dict:
        first_close_price=results_dict[id][1][1]
        second_close_price = results_dict[id][2][1]
        percent_change = (first_close_price-second_close_price)/second_close_price
        results_dict[id].append([percent_change])
    
    trending_stocks_percent_change = {}

    #sort dict by percent change desc

    trending_stocks_percent_change = sorted(results_dict.items(), key = lambda x : x[1][3], reverse=True)

    return {"x": trending_stocks_percent_change}
