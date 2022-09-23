
import sqlite3
from fastapi import FastAPI
from create_db import add_stock, create_connection
from populate_db import stock_symbols
from schema import Symbol
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date
app = FastAPI()
#displays all us stocks
@app.get("/home")
async def home_page():
    create_connection()
    stock = stock_symbols()
    return {"stocks": stock}

@app.post("/myStocks/{symbol}")
async def stock_inventory(symbol:str):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    ticker = yf.Ticker(symbol)
    # today = date.today()
    stock_table = ticker.history(period='max')
    #set index for dataframe
    dates = pd.date_range('18/09/2021', periods= 364)
    df = pd.DataFrame(stock_table, index = dates, columns=['stock_id','Open','High','Low','Close', 'Volume'])
    #add date as column in sql
    df['Date'] = df.index
    symbol_id = cursor.execute('select id from stock where symbol=?', (symbol,))
    row = symbol_id.fetchall()
    #parse 
    foreign_key = (row[0][0])
    df['stock_id']=  foreign_key
    #convert dataframe to sqlite table
    df.to_sql("stock_price", con =conn, if_exists='append', index =False)
    row = cursor.execute('select * from stock where symbol=?', (symbol,))
    row = row.fetchall()
    return {"stock added":list(row)}

    