import sqlite3
from sqlite3 import Error

from schema import Symbol


def  create_connection():
   
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    cur.execute(""" 
        CREATE TABLE IF NOT EXISTS stock(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            symbol TEXT NOT NULL UNIQUE,
            company TEXT NOT NULL
    
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS stock_price(
            
            stock_id INTEGER,
            date NOT NULL,
            open ,
            high ,
            low ,
            close ,
            volume ,
            FOREIGN KEY (stock_id) REFERENCES stock(id)
        )
    """)
    conn.commit()

def add_stock(symbol:Symbol):
    # conn = sqlite3.connect('app.db')
    # cur = conn.cursor()
    # operation = " insert into stock_price ()"
    pass