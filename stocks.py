import yfinance as yf

def getStock(ticker):
    stock = yf.Ticker(ticker)
    return stock

