from datetime import datetime

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
            if stock.buy:
                if self.balance / len(self.watch_stocks) > 0: # Check if there is money to be invested
                    self.balance -= stock.buyStock(self.balance / len([stock for stock in self.watch_stocks if stock.buy]))
            else: 
                self.balance += stock.sellStock(False)
