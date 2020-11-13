import requests

url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=WOKV6XE67340LADZ"
r = requests.get(url)

result_dict = r.json()
items = result_dict['Time Series (5min)']
