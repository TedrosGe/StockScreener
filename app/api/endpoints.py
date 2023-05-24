from fastapi import APIRouter
from models.models import Stock

from services import add_tickers
from services import fetch_tickers

router = APIRouter()

@router.get("/")
def read_root():
    stock =Stock()
    tickers= fetch_tickers(stock)
    print(tickers)
    return { "text":tickers}