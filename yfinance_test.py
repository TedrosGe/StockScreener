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

from app.database.database import SessionLocal
s = "tedros"
hashed_password = s.encode('utf-8')
    
print ((hashed_password))
