# --------------------------------------------------------
# Author: Daniel Xu
# Date: 07/17/2023
# Description: A program that computes Relative Strength Index technical indicator
#   for various stocks
# RSI Algorithm:
#   change = Sum(Previous Close - Current Close)
#   gain = change >= 0 ? change : 0
#   loss = change < 0 ? change * -1 : 0
#   avgGain = rma(gain, 14)
#   avgLoss = rma(loss, 14)
#       rma is an exponential moving average with alpha = 1/length
#   rs = avgGain / avgLoss
#   rsi = 100 - (100 / (1 + rs))
# --------------------------------------------------------

# Import libraries
import yfinance as yf
import numpy as np

def relative_strength_index(df, length):
    temp = df.copy()
    temp['Change'] = temp['Adj Close'] - temp['Adj Close'].shift(1)
    temp['Gain'] = np.where(temp['Change'] >= 0, temp['Change'], 0)
    temp['Loss'] = np.where(temp['Change'] < 0, -1 * temp['Change'], 0)
    temp['Average Gain'] = temp['Gain'].ewm(alpha=1/length, min_periods=length).mean()
    temp['Average Loss'] = temp['Loss'].ewm(alpha=1/length, min_periods=length).mean()
    temp['Relative Strength'] = temp['Average Gain'] / temp['Average Loss']
    temp['RSI'] = 100 - 100/(1 + temp['Relative Strength'])
    
    return temp['RSI']
    

# Download historical data for various stocks
tickers = ['AMZN', 'AAPL', 'GOOG']
stock_data = {}

for t in tickers:
    data = yf.download(t, period='1mo', interval='5m') # 5 minute candles
    data.dropna(how='any', inplace=True)
    stock_data[t] = data

for s in stock_data:
    stock_data[s]['RSI'] = relative_strength_index(stock_data[s], 14)