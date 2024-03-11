
from sqlalchemy.orm import Session
from fastapi import Depends
import yfinance
from app.database.database import SessionLocal
from app.models.models import Stock
from app.services.home import get_db


class DailyStockUpdater:

    def __init__(self,API_key, ticker_list ) -> None:
        self.API_key = API_key
        self.ticker_list = ticker_list

    def fetch_stock_data(self, db:Session = Depends(get_db)):
        db_tickers_id = db.query(Stock.ticker).all()
        tickers_id = [id[0] for id in db_tickers_id]
        return tickers_id
    
    def update_single_stock_data(self,  stock:Stock, db:Session = Depends(get_db)):

            try:
                stock_update = self.get_today_stock_info(stock[0])
                stock.company =stock_update.get["longName"]
                stock.industry = stock_update.get["industry"]
                stock.marketCap = stock_update.get["marketCap"]
                stock.recommendationMean= stock_update.get["recommendationMean"]
                stock.forwardPE = stock_update.get["forwardPE"]
                stock.high = stock_update.get["high"]
                stock.low = stock_update.get["low"]
                stock.volume = stock_update.get["volume"]
                stock.currentPrice = stock_update.get["currentPrice"]
                stock.fiftyTwoWeekLow = stock_update.get["fiftyTwoWeekLow"]
                stock.fiftyTwoWeekHigh = stock_update.get["fiftyTwoWeekHigh"]
            except Exception as e:
                print(f"Error updating stock with ticker {stock[0].ticker}: {e}")
                


    def get_today_stock_info(tic):
        stock = yfinance.Ticker(tic)
        stock_dict = stock.info
        selected_info = {
        'longName' : stock_dict.get("longName"),
        'industry' : stock_dict.get("industry"),
        'marketCap' : stock_dict.get("marketCap", None),
        'recommendationMean' :stock_dict.get("recommendationMean", 0),
        'forwardPE' :stock_dict.get("forwardEps", None),
        'high' : stock_dict.get("dayHigh", None),
        'low' : stock_dict.get("dayLow", None),
        'volume' : stock_dict.get("volume"),
        'currentPrice' : stock_dict.get("currentPrice"),
        'fiftyTwoWeekLow'  : stock_dict.get("fiftyTwoWeekLow", None),
        'fiftyTwoWeekHigh' : stock_dict.get("fiftyTwoWeekHigh", None)
        }
        return selected_info

        
    def process_scheduled_updates(self, ):
        pass


    