import yfinance as yf
import time
import datetime
import os
from stocks import getStocks
from stocks import Stock
from portfolio import Portfolio

def getBalance():
    """ Opens trading-history file and returns the last balance if it exists"""
    if os.path.exists('files/trading-history.txt'):
        initial_balance = 0.0
        with open("files/trading-history.txt", 'r') as f:
            file_size = os.path.getsize("files/trading-history.txt")
            if file_size != 0:
                for line in f:
                    pass
                initial_balance = float(line.split()[3])
            else:
                initial_balance = float(input("Enter a balance to begin trading: "))
    else:
        initial_balance = float(input("Enter a balance to begin trading: "))

    return initial_balance

def displayReport(trade_history):
    """ Displays a report given a list of buy/sell"""
    stock_history = dict()
    if len(trade_history) > 0:
        for action in trade_history:
            buysell = action.split()
            if stock_history.get(buysell[3]) != None:   
                if buysell[2] == 'BUY':
                    stock_history[buysell[3]][0] += 1
                else:
                    stock_history[buysell[3]][1] += 1
                    stock_history[buysell[3]][2] += float(buysell[6])
            else:
                if buysell[2] == 'BUY':
                    stock_history[buysell[3]] = [1,0,0]
                else:
                    stock_history[buysell[3]] =  [0,1,float(buysell[6])]

    print("Stock:   Buys   Sells   Total Return")
    for k, v in stock_history.items():
        print(f"{k}:      {v[0]}       {v[1]}        {v[2] : .2f}")



if __name__ == "__main__":
    initial_balance = getBalance()
    user_portfolio = Portfolio(initial_balance) 
    print("Balance:", initial_balance) #
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
            print(f"\n==================== Trading Report for {datetime.date.today()}")
            print(f"\nTotal Return: ${total_return : .2f}\n")
            trading_history = list()
            with open("files/buysell-session-history.txt", 'r') as f:
                for line in f:
                    trading_history.append(line)
            displayReport(trading_history)
            
            # Save balance and trading activity
            with open("files/trading-history.txt", 'a') as f:
                f.write(f"{datetime.datetime.now()} {total_return} {str(user_portfolio.getBalance())}\n") # Write balance to file
            # Clear session history
            open('files/buysell-session-history.txt', 'w').close()
            break