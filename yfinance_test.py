from datetime import date
from email.policy import strict
import string
import yfinance as yf
import sqlite3
from stocksymbol import StockSymbol
import yfinance as yf
import pandas as pd
import numpy as np
import csv
import json
import yfinance
from app.database.database import SessionLocal
import yfinance as yf

google = yf.Ticker("GOOG")
hist = google.history(period="5d")

# Convert datetime index to string format with only date part
hist.index = pd.to_datetime(hist.index)

hist.index = hist.index.date
print(hist)