import yfinance as yf
import pandas as pd
ticker = yf.Ticker("GOOG")

df = ticker.history(period="2y")
print(df)
