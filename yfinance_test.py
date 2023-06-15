from datetime import date
from email.policy import strict
import string
import yfinance as yf
import sqlite3
from stocksymbol import StockSymbol
import yfinance as yf
import pandas as pd
import numpy as np

tic = yf.Ticker('GOOG')


# ^ returns a named tuple of Ticker objects
x= tic.history(period="1y")
print(x)

