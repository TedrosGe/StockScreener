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

tic = yf.Ticker('AMZN')


# ^ returns a named tuple of Ticker objects
x= tic.history(period="max")
print(x)

