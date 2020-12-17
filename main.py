import yfinance as yf
import time
import datetime
from stocks import getStocks
from stocks import Stock
from portfolio import Portfolio

if __name__ == "__main__":
    #initial_balance = float(input("Enter balance: "))
    initial_balance = 0.0
    with open("day-trading-history.txt", 'r') as f:
        contents = f.read()
        if contents != "" and len(contents) < 1:
            initial_balance += float(contents) # read in previous balance
        else:
            initial_balance += float(input('No balance. Add money to trade?'))
    user_portfolio = Portfolio(initial_balance) # Create porfolio
    print(initial_balance) #
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

            # Save report?
            # save_report = input("Would you like to save the report (y/n): ")
            # if save_report == 'y' or save_report == 'Y':
            #     file_name = input("Enter the file name: ")
            #     with open(f"/trading-reports/{file_name}", "w") as f:
            #         for line in trading_history:
            #             f.write(line)

            # Delete file contents and save balance 
            with open("day-trading-history.txt", 'w') as f:
                f.write(str(user_portfolio.getBalance()) + "\n") # Write balance to file
            break