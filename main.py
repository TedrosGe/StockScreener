
import sqlite3
from fastapi import FastAPI
from create_db import add_stock, create_connection
from populate_db import stock_symbols
from schema import Symbol
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta
import jinja2
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from stocksymbol import StockSymbol
import helperFunctions as hF
app = FastAPI()
templates = Jinja2Templates(directory="templates")


#displays all us stocks
@app.get("/home")
async def home_page(request:Request ):
    create_connection()
    
   
    user_input = request.query_params.get("filter", False)
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    
        
    #fix sql query  
    if user_input =="intraday_highs":
        #fetch highest stock prices
        operation = '''
        select *from ( 
        select   symbol, id,max(close) from stock_price
        join stock on stock.id = stock_price.stock_id
        )
        where date = ?
        '''
        cursor.execute(operation, (date.today().isoformat(),))
        stocks = cursor.fetchall()
    else:
        #fetch all stocks
        cursor.execute(""" select id, symbol, company from stock ORDER BY symbol""")
        stocks= cursor.fetchall()

    return  templates.TemplateResponse("home.html", {"request": request, "stocks":stocks})

@app.get("/{symbol}")
async def fetch_stock_history(symbol:str, request:Request):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    #check if symbol exists in DB
    sql_sel = 'select symbol from stock where id = ? '
    symbol_id= cursor.execute(sql_sel, (symbol,))
    row = symbol_id.fetchall()
    ticker = yf.Ticker(symbol)
    today = (date.today())
    time_dif = timedelta(365)
    stock_table = ticker.history(period='max')
    #set index for dataframe
    dates = pd.date_range(today - time_dif , periods= 365)
    df = pd.DataFrame(stock_table, index = dates, columns=['stock_id','Open','High','Low','Close', 'Volume'])
    #add date as column in sql
    df['Date'] = df.index
    df.sort_index(ascending=False)
    symbol_id = cursor.execute('select id from stock where symbol=?', (symbol,))
    row = symbol_id.fetchall()
    #parse 
    foreign_key = row[0][0]
    df['stock_id']=  foreign_key
    #convert dataframe to sqlite table
    df.to_sql("stock_price", con =conn, if_exists='append', index =False)
    row = cursor.execute('select * from stock where symbol=?', (symbol,))
    row = row.fetchall()
    #get the stock id
    operation1 = 'select id from stock where symbol = ? '
    row = cursor.execute(operation1,(symbol,))
    row = row.fetchall()
    stock_id = row[0][0]
    if stock_id is None:
        raise TypeError("stock has to be added to inventory ")
    operation2 = "select *from stock_price where stock_id = ? "
    row = cursor.execute(operation2, (stock_id,))
    stock_table = row.fetchall()
    stock_table =list(stock_table)
    pd_table = pd.DataFrame(stock_table, columns= ['stock_id','date','open', 'high','low', 'close','volume'])
    #set data to y/m/d format
    pd_table["date"] = pd_table["date"].str[0:11]
    pd_table = pd_table.sort_values(by=['date'], ascending= False)
    stock_history = pd_table.to_dict(orient='records')

    # get trading exchange platform from api
    ex_platform = hF.get_exchange(symbol)
    
    return  templates.TemplateResponse("stock_history.html", {"request": request, "stocks":stock_history, "stock_symbol": symbol, "exchange_platform": ex_platform})
    



@app.post("/{symbol}")
async def add_stock(symbol:str):
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
    row = cursor.execute('select * from stock where symbol=? order by open', (symbol,))
    row = row.fetchall()
    return {"stock added":list(row)}