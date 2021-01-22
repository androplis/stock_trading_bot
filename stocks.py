import yfinance as yf
import datetime
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

        stock_history = self.getStock().history(period="1d", interval="1m")
        MA_20 = stock_history['Close'].rolling(20).mean() 
        # Look to Buy the stock
        if MA_20[-1] < self.getClose(): # Buy Trigger
            self.shares = amount / self.getClose() # Can buy with existing shares
            self.buy = False
            self.buy_price = self.getClose() # Set Buy Price
            self.sell_lower_limit = self.buy_price - (self.buy_price * .005)  # Set sell thresholds
            self.sell_upper_limit = self.buy_price + (self.buy_price * .0025)

            print(MA_20[-1], " ", stock_history['Close'][-1], "- BUY") # Record buy
            with open("files/buysell-session-history.txt", 'a') as f:
                data = f"{datetime.datetime.now()} BUY {self.getTicker()} {self.getBuyPrice()} {self.getShares()}\n"
                f.write(data)

            return self.getMarketValue()
        else: # WAIT (Temporary)
            print(MA_20[-1], " ", stock_history['Close'][-1], "- WAIT")
            return 0.0

    def sellStock(self, force_sell): # Right now, sells all the shares, eventually will sell temporary amount
        """ Sells (numShares) amount of stock at the last closing price """ 
        # Temporary for sell validation purposes
        stock_history = self.getStock().history(period="1d", interval="1m") #
        MA_20 = stock_history['Close'].rolling(20).mean()  #
        # Look to Sell the stock
        if (self.getClose() >= self.getUpperLimit() or self.getClose() <= self.getLowerLimit()) or force_sell: # Sell Thresholds
            num_shares = self.shares # Get the number of shares before cleared (temporary)
            self.shares = 0
            self.buy = True
            self.sell_price = self.getClose()

            print(MA_20[-1], " ", stock_history['Close'][-1], "- SELL") # Record Sell
            with open("files/buysell-session-history.txt", 'a') as f:
                data = f"{datetime.datetime.now()} SELL {self.getTicker()} {self.getSellPrice()} {num_shares} {(self.getSellPrice() - self.getBuyPrice()) * num_shares}\n"
                f.write(data)

            return num_shares * self.sell_price
        else: # Hold (Temporary)
            print(MA_20[-1], " ", stock_history['Close'][-1], "- HOLD")
            return 0.0

def getStocks():
    stocks = list()
    # Get 5 trending stocks
    URL = 'https://stockbeep.com/trending-stocks'
    driver = webdriver.Chrome('driver/chromedriver')
    driver.get(URL)
    html = driver.page_source
    soup = sp(html, 'html.parser')
    table_rows = soup.find_all('tr', {'role': 'row'})
    for row in table_rows[1:6]:
        ticker = row.a.string
        stock = Stock(ticker)
        stocks.append(stock)

    return stocks
