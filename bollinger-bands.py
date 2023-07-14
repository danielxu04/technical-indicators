# --------------------------------------------------------
# Author: Daniel Xu
# Date: 07/13/2023
# Description: A program that illustrates the technical indicator of Bollinger
#   Bands using Python and Yahoo Finance
# BB Calculation:
#   - 20 Day Simple MA
#   - 20 Day Simple MA + (Standard Deviation x 2)
#   - 20 Day Simple MA - (Standard Deviation x 2)
# --------------------------------------------------------

# Import libraries
import yfinance as yf

def bollinger_bands(df, window):
    temp = df.copy()
    temp['Middle Band'] = temp['Adj Close'].rolling(window).mean()
    # 0 degrees of freedom, as we want to calculate SD of sample, not population
    temp['Upper Band'] = temp['Middle Band'] + (2 * temp['Adj Close'].rolling(window).std(ddof=0))
    temp['Lower Band'] = temp['Middle Band'] - (2 * temp['Adj Close'].rolling(window).std(ddof=0))
    temp['Width'] = temp['Upper Band'] - temp['Lower Band']
    
    return temp[['Middle Band', 'Upper Band', 'Lower Band', 'Width']]

# Download historical data for various stocks
tickers = ['AMZN', 'AAPL', 'GOOG']
stock_data = {}

for t in tickers:
    data = yf.download(t, period='1mo', interval='15m') # 15 minute candles
    data.dropna(how='any', inplace=True)
    stock_data[t] = data
    
for s in stock_data:
    stock_data[s][['Middle Band', 'Upper Band', 'Lower Band', 'Width']] = bollinger_bands(stock_data[s], 14)