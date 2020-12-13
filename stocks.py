import yfinance as yf
from datetime import datetime

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.shares = 0
        self.buy = True

    # Accessors
    def getStock(self):
        """ Returns a stock object """
        return yf.Ticker(self.ticker)

    def getClose(self):
        """ Returns the last closing price of the stock """
        dayHistory = self.getStock().history(period="1d", interval="1m")
        return dayHistory["Close"][-1]

    def getMarketValue(self):
        """ Returns the market value of the stock shares owned"""
        return self.getClose() * self.shares

    # Buy / Sell
    def buyStock(self, numShares):
        """ Buys (numShares) amount of stock at the last closing price """
        self.shares = numShares
        self.buy = False

    def sellStock(self, numShares):
        """ Sells (numShares) amount of stock at the last closing price """
        self.shares = numShares
        self.buy = True

def getStock(tickers):
    # Select which stocks with web-scraping...

    stocks = list()
    for ticker in tickers:
        stock = Stock(ticker)
        stocks.append(stock)

    return stocks
