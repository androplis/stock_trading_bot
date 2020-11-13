import yfinance as yf

def test():
    msft = yf.Ticker("MSFT")
    print(msft.info['open'])

if __name__ == "__main__":
    test()