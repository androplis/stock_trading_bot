import yfinance as yf
import time
import datetime
from stocks import getStocks
from stocks import Stock

class Portfolio:
    """ Investor's portfolio, contains a balance and a set of watch stocks """
    def __init__(self, balance):
        self.balance = balance
        self.watch_stocks = list()

    # Mutators
    def setWatchStocks(self, stocks):
        self.watch_stocks = stocks

    # Accessors
    def getBalance(self):
        return self.balance

    def getWatchStocks(self):
        return self.watch_stocks

    def setBalance(self, amount):
        self.balance = amount

    def buySell(self):
        """ Looks at each stock and determines whether to buy or sell """
        for stock in self.watch_stocks:
            stock_history = stock.getStock().history(period="1d", interval="1m")
            MA_20 = stock_history['Close'].rolling(20).mean() 
            if stock.buy: 
                # Look to Buy the stock
                if MA_20[-1] < stock.getClose(): # Buy Trigger
                    print(MA_20[-1], " ", stock_history['Close'][-1], "- BUY")
                    if stock.buyStock(self.balance): # balance / 5
                        # write buy data to files
                        self.balance -= stock.getBuyPrice()
                        print(f"{datetime.datetime.now()} | BUY | {stock.getTicker()} | ${stock.getBuyPrice()} | {stock.getShares()}")
                else: # Wait
                    print(MA_20[-1], " ", stock_history['Close'][-1], "- WAIT")
                    continue
            else: 
                # Look to Sell the stock
                if stock.getClose() >= stock.getUpperLimit() or stock.getClose() <= stock.getLowerLimit(): # Sell Thresholds
                    num_shares = stock.sellStock()
                    self.balance += stock.getSellPrice()
                    print(MA_20[-1], " ", stock_history['Close'][-1], "- SELL")
                    print(f"{datetime.datetime.now()} | SELL | {stock.getTicker()} | ${stock.getSellPrice()} | {num_shares}")
                else: # Hold
                    print(MA_20[-1], " ", stock_history['Close'][-1], "- HOLD")

if __name__ == "__main__":
    balance = float(input("Enter balance: "))
    user_portfolio = Portfolio(balance)

    # Get Stocks
    user_portfolio.setWatchStocks(getStocks(['TGTX']))

    # Perform Trading
    while True:
        user_portfolio.buySell()
        time.sleep(60) # Run every 60 seconds