import yfinance as yf
from datetime import datetime

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.shares = 0
        self.sell_upper_limit = 0.0
        self.sell_lower_limit = 0.0
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

    def getUpperLimit(self):
        return self.sell_upper_limit

    def getLowerLimit(self):
        return self.sell_lower_limit

    # Buy / Sell
    def buyStock(self, amount):
        """ Buys (numShares) amount of stock at the last closing price """
        if amount > self.getClose():
            self.shares = amount / self.getClose()
            self.buy = False
            self.sell_lower_limit = self.getClose() - (self.getClose() * .01)
            self.sell_upper_limit = self.getClose() + (self.getClose() * .005)

        return self.shares

    def sellStock(self, amount):
        """ Sells (numShares) amount of stock at the last closing price """
        self.shares = 0
        self.buy = True

def getStocks(tickers):
    # Select which stocks with web-scraping...

    stocks = list()
    for ticker in tickers:
        stock = Stock(ticker)
        stocks.append(stock)

    return stocks
