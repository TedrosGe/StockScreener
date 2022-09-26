
import sqlite3
from fastapi import FastAPI
from create_db import add_stock, create_connection
from populate_db import stock_symbols
from schema import Symbol
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import jinja2
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app = FastAPI()


templates = Jinja2Templates(directory="templates")


#displays all us stocks
@app.get("/home")
async def home_page(request:Request):
    create_connection()
    stock = stock_symbols()
    return  templates.TemplateResponse("home.html", {"request": request, "stocks":stock})

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

@app.get("/myStocks/{symbol}")
async def stock_perf_graph(symbol:str, request:Request):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    #get the stock id
    operation1 = 'select id from stock where symbol = ? '
    row = cursor.execute(operation1,(symbol,))
    row = row.fetchall()
    stock_id = row[0][0]
    operation2 = "select *from stock_price where stock_id = ? "
    row = cursor.execute(operation2, (stock_id,))
    stock_table = row.fetchall()
    stock_table =list(stock_table)
    
    pd_table = pd.DataFrame(stock_table, columns= ['stock_id','date','open', 'high','low', 'close','volume'])
    #set data to y/m/d format
    pd_table["date"] = pd_table["date"].str[0:11]
    #index date
    # pd_table = pd_table.set_index('date')
    #get rid of none values
    
    x = pd_table.to_dict(orient='records')
    #graph stock performance



    
    return  templates.TemplateResponse("index.html", {"request": request, "stocks":x})
