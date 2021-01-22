# Stock Trading Bot

## Description
This bot implements a simple trading algorithim and tracks the performace of the algorithim through a fake cash balance. The bot reads in real-time-stock data using the [yfinance](https://pypi.org/project/yfinance/) python library. 
Each time the script is run, the program uses a [chrome-web-driver](https://chromedriver.chromium.org/downloads) and selenium to scrap the top 5 trending stocks according to [stockbeep](https://stockbeep.com/trending-stocks).
Stockbeep is a stock scanner that provides stock information for "informational use" only. They cannot be liable for any financial loss. 

## Requirements
- [Python3](https://www.python.org/download/releases/3.0/)
- [yfinance](https://pypi.org/project/yfinance/)
- [chrome-web-driver](https://chromedriver.chromium.org/downloads)
- [selenium](https://selenium-python.readthedocs.io/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)

## Usage
This program runs through a command line and stores information in local files. Use the command `python3 main.py` to begin the script. You will then be prompted 
for the duration of trading window. The intial balance will be displayed and trading will begin. Every minute the algorithim is run and any buys/sells are displayed. 
At the end of the trading window, the total return and trading history are displayed, and the results are saved to the local files. 

## License 
MIT License

Copyright (c) 2021 Andrew Biddle

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
