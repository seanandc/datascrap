# DataScrap

## What is it?
This project is for educational purposes, and not for production use.
Feel free to use at your own risk.

This this a simple stock screener module that scrap yahoo finance for part of S&P500 stocks that has company P/B ratio that is lower than user input.
## Installation
the stock screener modules uses, requests, mock, nose and beautifulsoup

## Getting Started ( Docs )


run setup.py to install all required modules.
Then select your screen value for stock

screen = StockScreen(#)

then select your stock

screen.yahooKeyStats(stock)

if the stock is below the # you selected

