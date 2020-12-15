import yfinance as yf
from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup as sp 

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.shares = 0
        self.sell_upper_limit = 0.0
        self.sell_lower_limit = 0.0
        self.buy = True
        self.buy_price = 0.0
        self.sell_price = 0.0

    # Accessors
    def getStock(self):
        """ Returns a stock object """
        return yf.Ticker(self.ticker)

    def getTicker(self):
        return self.ticker

    def getShares(self):
        return self.shares

    def getBuyPrice(self):
        return self.buy_price

    def getSellPrice(self):
        return self.sell_price

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
            self.shares = amount / self.getClose() # Can buy with existing shares
            self.buy = False
            self.buy_price = self.getClose()
            self.sell_lower_limit = self.buy_price - (self.buy_price * .005)
            self.sell_upper_limit = self.buy_price + (self.buy_price * .0025)
            return True
        else:
            print("Could not purchase stocks.")
            return False
        # return self.shares

    def sellStock(self): # Sells certain numShares...
        """ Sells (numShares) amount of stock at the last closing price """
        num_shares = self.shares # Get the number of shares before cleared (temporary)
        self.shares = 0
        self.buy = True
        self.sell_price = self.getClose()
        return num_shares


def getStocks():
    stocks = list()
    # Get 5 trending stocks
    URL = 'https://stockbeep.com/trending-stocks'
    driver = webdriver.Chrome('/Users/andrewbiddle/Desktop/chromedriver')
    driver.get(URL)
    html = driver.page_source
    soup = sp(html, 'html.parser')
    table_rows = soup.find_all('tr', {'role': 'row'})
    for row in table_rows[1:6]:
        ticker = row.a.string
        stock = Stock(ticker)
        stocks.append(stock)

    return stocks
