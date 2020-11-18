import yfinance as yf
import time
from datetime import datetime
from stocks import getStock

def getMarketPrice(stock):
    """ Returns the last closing price of the given stock"""
    day_history =  stock.history(period="1d", interval="1m")
    return day_history["Close"][-1]

def buySell():
    """ Performs a buy/sell strategy"""
    if buy:
        # Implement buy strategy
        if balance > 0: # Check if there is money to be invested
            if market_price <= stock.info["dayLow"] + .50: # Buy if price reaches (or nears) daily low 
                # Buy
                print("Buy")
            elif market_price >= stock.info["dayHigh"] - .50: # Buy if price reaches (or nears) daily high
                # Buy
                print("Buy")
            else:
                print("Nothing", stock.info["dayLow"])
    else:
        if(market_price >= PROFIT_THRESHHOLD or market_price <= STOP_LOSS_THRESHHOLD):
            # Sell
            print("Sell")
        else:
            print("Hold")

if __name__ == "__main__":
    buy = True
    balance = 1000.00
    stock = getStock("aapl")

    market_price = getMarketPrice(stock)
    PROFIT_THRESHHOLD = 0
    STOP_LOSS_THRESHHOLD = 0

    # Perform Trading
    while True:
        buySell()
        time.sleep(60) # Run every 60 seconds