import yfinance as yf
import sqlite3
from stocksymbol import StockSymbol
import yfinance as yf

api_key = 'cf7959df-216f-461a-a735-0e3fe089d675'  
conn = sqlite3.connect('app.db')
cur = conn.cursor()
ss =StockSymbol(api_key)
us_symbol_list = ss.get_symbol_list("us")
print(us_symbol_list)
tic = yf.Ticker('MSFT')
# ^ returns a named tuple of Ticker objects


# print(tic.info['dayHigh'])
# print(tic.info['dayLow'])
# # print(tic.info['volume'])
# print(tic.info['longName'])