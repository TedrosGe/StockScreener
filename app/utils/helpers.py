
from sqlalchemy.orm import Session
from fastapi import Depends
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
    
    def update_stock_date(self, tickers_id):
        


    def process_scheduled_updates(self):
        pass


    