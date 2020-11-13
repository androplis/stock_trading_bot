import yfinance as yf

aapl = yf.Ticker("aapl")
aaplHistory = aapl.history(period="1d", interval="1m")

print(aaplHistory['Close'])