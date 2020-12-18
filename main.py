import yfinance as yf
import time
import datetime
import os
from stocks import getStocks
from stocks import Stock
from portfolio import Portfolio

if __name__ == "__main__":
    # Get starting balance
    initial_balance = 0.0
    with open("day-trading-history.txt", 'r') as f:
        file_size = os.path.getsize("day-trading-history.txt")
        if file_size != 0:
            for line in f:
                pass
            initial_balance = line.split()[3]
        else:
            initial_balance = float(input("Enter a balance to begin trading: "))
    user_portfolio = Portfolio(initial_balance) # Create porfolio
    print(initial_balance) #
    # Set timers
    counter = 0.0
    trading_time = float(input("How long would you like to trade? (in hrs): "))

    # Get Stocks
    user_portfolio.setWatchStocks(getStocks())
    
    # Perform Trading
    while True:
        if counter <= trading_time:
            user_portfolio.buySell() # Perform trading
            print("Balance: ", user_portfolio.getBalance())
            counter += 1 / 60
            time.sleep(60) # Run every min
        else: # Closing tasks
            # Sell remaining stocks and update balance
            for stock in user_portfolio.getWatchStocks():
                if stock.buy == False:
                    user_portfolio.setBalance(user_portfolio.getBalance() + stock.sellStock(True))
            total_return = user_portfolio.getBalance() - initial_balance

            # Display Report 
            print(f"==================== Trading Report for {datetime.date.today()}")
            print(f"\nTotal Return: {total_return}\n")
            trading_history = list()
            with open("day-trading-history.txt", 'r') as f:
                for line in f:
                    # Make report more pleasurable
                    trading_history.append(line)
                    print(line)

            # Save balance and trading activity
            with open("day-trading-history.txt", 'a') as f:
                f.write(f"{datetime.datetime.now()} {total_return} {str(user_portfolio.getBalance())}") # Write balance to file
            break