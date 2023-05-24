from sqlalchemy import create_engine
from stocksymbol import StockSymbol
import yfinance as yf
from app.models import Base, Stock, stockDetail
from sqlalchemy.orm import sessionmaker

db_path = "/home/teddy/Documents/StockScreener/app/database/database_file.db"
engine = create_engine("sqlite:///" + db_path)
Session = sessionmaker(bind=engine)
session = Session()

def add_tickers():
    api_key = 'cf7959df-216f-461a-a735-0e3fe089d675'  
    ss = StockSymbol(api_key)
    us_ticker_list = ss.get_symbol_list("us")
    for i in us_ticker_list:
        ticker = Stock(id= i["symbol"], company =i["longName"])
        session.add(ticker)
        session.commit()

    session.close()

def fetch_tickers( stock):
   tickers = session.query(Stock).filter(Stock.ticker).all
   return tickers