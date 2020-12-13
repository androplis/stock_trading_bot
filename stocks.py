import yfinance as yf
from datetime import datetime

class Stock:
    def __init__(self):
        self.ticker = ''

    def getStock(self):
        """ Returns a stock object """
        return yf.Ticker(self.ticker)

    def getClose(self):
        """ Returns the last closing price of the stock """
        dayHistory = self.getStock().history(period="1d", interval="1m")
        return dayHistory["Close"][-1]

