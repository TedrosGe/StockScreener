import sqlite3
from urllib import response

from stocksymbol import StockSymbol
import yfinance as yf
def stock_symbols():
    api_key = 'cf7959df-216f-461a-a735-0e3fe089d675'  
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    ss =StockSymbol(api_key)
    us_symbol_list = ss.get_symbol_list("us")
    count =0 
    for i in us_symbol_list:
        # ticker= yf.Ticker("{}".format(i["symbol"]))
        # print(ticker)
        try: 

            cur.execute(" insert into stock (symbol, company) values (?, ?)", (i["symbol"],i["longName"]) )
        except Exception as e:
            # print(i["symbol"])
            # print(e)
            continue
    conn.commit()
    operation = " select* FROM stock"
    sql_sel = cur.execute(operation)
    rows = sql_sel.fetchall()
    # print(rows)
    return rows

#add stocks to portfolio
def add_stock(id:int):
    #fetch stock symbol from stock db
    
    pass
