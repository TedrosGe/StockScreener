from datetime import date
from email.policy import strict
import string
import yfinance as yf
import sqlite3
from stocksymbol import StockSymbol
import yfinance as yf
import pandas as pd
import numpy as np
api_key = 'cf7959df-216f-461a-a735-0e3fe089d675'  
conn = sqlite3.connect('app.db')
cur = conn.cursor()
ss =StockSymbol(api_key)
us_symbol_list = ss.get_symbol_list("us")
# print(us_symbol_list)
tic = yf.Ticker('MSFT')
# ^ returns a named tuple of Ticker objects
x= tic.history(period="max")
ticker = yf.Ticker("GOOG")
    # today = date.today()
stock_table = ticker.history(period='max')
dates = pd.date_range('18/09/2021', periods= 364)

df = pd.DataFrame(stock_table, index = dates, columns=['stock_id','Open','High','Low','Close', 'Volume'])
df['Date'] = df.index

symbol_id = cur.execute('select id from stock where symbol=?', ('GOOG',))
row = symbol_id.fetchall()
foreign_key = (row[0][0])
df['stock_id']=  foreign_key
#convert dataframe to sqlite table
# df.to_sql("stock_price", con =conn, if_exists='append', index =False)

row = cur.execute('select * from stock_price where stock_id=?', (foreign_key,))
row = row.fetchall()
# sql_to_pd=pd.read_sql("select stock_id, date, open, high, low, close, volume from stock_price where stock_id =? ")
