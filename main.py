import yfinance as yf
import time
import datetime
from stocks import getStocks
from stocks import Stock
from portfolio import Portfolio

if __name__ == "__main__":
    initial_balance = float(input("Enter balance: ")) # read from file
    user_portfolio = Portfolio(initial_balance)
    counter = 0.0
    trading_time = float(input("How long would you like to trade? (in hrs): "))

    # Get Stocks
    user_portfolio.setWatchStocks(getStocks())
    
    # Perform Trading
    while True:
        if counter <= trading_time:
            user_portfolio.buySell() # Perform trading
            counter += 1 / 60
            time.sleep(60) # Run every min
        else:
            # Sell every stock
            for stock in user_portfolio.getWatchStocks():
                #Sell stock
            # Calculate total return
            print(f"==================== Trading Report for {datetime.datetime.date()}")
            break