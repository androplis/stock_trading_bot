import yfinance as yf
import time
from datetime import datetime
import stocks

class Portfolio:
    """ Investor's portfolio, contains a balance and a set of watch stocks """
    def __int__(self, balance):
        self.balance = balance
        self.watch_stocks = list()

    def getBalance(self):
        return self.balance

    def setBalance(self, amount):
        self.balance = amount

    def buySell(self):
        """ Looks at each stock and determines whether to buy or sell """
        # For stock in stocks
        # Implement Stratey 

if __name__ == "__main__":

    # Perform Trading
    while True:
        # Buy / # Sell
        time.sleep(60) # Run every 60 seconds