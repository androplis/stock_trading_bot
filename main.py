import yfinance as yf
import time
from stocks import getStock

buy = True
balance = 1000.00

def getStockPrice(stock):
    """ Returns the last closing price of the given stock"""
    day_history =  stock.history(period="1d", interval="1m")
    return day_history["Close"][0]


def buySell():
    stock = getStock("aapl")
    last_close = getStockPrice(stock)
    
    
    if buy:
        # Implement buy strategy
        if balance > 0: # Check if money needs to be invested
    else:
        print("idk")
        # Implement sell strategy


# Perform Trading
while True:
    buySell()
    time.sleep(10) # Run every 10 seconds