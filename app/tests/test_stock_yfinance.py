import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import yfinance

raw_data = yfinance.download (tickers = "^GSPC", start = "1994-01-07", 
                              end = "2019-09-01", interval = "1d")

print(raw_data)