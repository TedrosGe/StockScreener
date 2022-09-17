from fastapi import FastAPI
from create_db import create_connection
from populate_db import stock_symbols
from schema import Symbol
app = FastAPI()
#displays all us stocks
@app.get("/home")
def home_page():
    create_connection()
    stock = stock_symbols()
    return {"stocks": stock}

@app.post("/myStocks/{symbol}")
def add_stock(symbol:str):
    pass