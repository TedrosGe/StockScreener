import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import yfinance as yf

msft = yf.Ticker("MSFT")
hist = msft.history(period="1mo")
# get all stock info
x = msft.info
for i in x:
    print(i)