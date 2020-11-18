import yfinance as yf
from datetime import datetime

def getStock(ticker):
    stock = yf.Ticker(ticker)
    return stock

