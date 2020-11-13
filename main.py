import yfinance as yf
import time
import schedule
from stocks import getStock

buy = True

def buySell():
    stock = getStock("aapl")
    print("Test")
    # If buy

    # If Sell

# Run every monday-friday from 9:00-4:00
schedule.every(10).seconds.do(buySell)

# Infinite loop
while True:
    schedule.run_pending()
    time.sleep(10) # Run every min