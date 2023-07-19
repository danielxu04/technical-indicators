# --------------------------------------------------------
# Author: Daniel Xu
# Date: 07/14/2023
# Description: A program that computes Average Directional Index technical indicator
#   for various stocks
# ADI Calculation:
#   Up Movement = Current High - Previous High
#   Down Movement = Previous Low - Current Low
#   +DM = Up Movement > Down Movement  && Up Movement > 0 ? +DM = Up Movement : +DM = 0
#   -DM = Down Movement > Up Movement  && Down Movement > 0 ? -DM = Down Movement : -DM = 0
#   +DI = 100 * EMA(+DM / ATR)
#   -DI = 100 * EMA(-DM / ATR)
#   ADX = 100 * EMA(abs[(+DI - -DI) / (+DI + -DI)])
# --------------------------------------------------------

# Import libraries
import yfinance as yf
import numpy as np

# AVERAGE_TRUE_RANGE - returns the ATR column of the DataFrame
def average_true_range(df, window):
    df_copy = df.copy()
    df_copy['High-Low'] = df_copy['High'] - df_copy['Low']
    df_copy['High-PC'] = df_copy['High'] - df['Adj Close'].shift(1) # shift to PREVIOUS close
    df_copy['Low-PC'] = df_copy['Low'] - df['Adj Close'].shift(1)
    df_copy['True Range'] = df_copy[['High-Low', 'High-PC', 'Low-PC']].max(axis=1, skipna=False)
    
    # Using 'com' instead of 'span' will get us closer to yfinance's Exponential Moving Average
    #   'span' is closer to TradingView's algorithm for EMA
    df_copy['ATR'] = df_copy['True Range'].ewm(span=window, min_periods=window).mean()
    
    return df_copy['ATR']

# AVERAGE_DIRECTIONAL_INDEX - returns the ADX column of specified DF
def average_directional_index(df, window):
    temp = df.copy()
    temp['UpMove'] = temp['High'] - temp['High'].shift(1)
    temp['DownMove'] = temp['Low'].shift(1) - temp['Low']
    temp['+DM'] = np.where((temp['UpMove'] > temp['DownMove']) & (temp['UpMove'] > 0), temp['UpMove'], 0)
    temp['-DM'] = np.where((temp['DownMove'] > temp['UpMove']) & (temp['DownMove'] > 0), temp['DownMove'], 0)
    temp['ATR'] = average_true_range(temp, 14)
    temp['+DI'] = 100 * (temp['+DM'] / temp['ATR']).ewm(com=window, min_periods=window).mean()
    temp['-DI'] = 100 * (temp['-DM'] / temp['ATR']).ewm(com=window, min_periods=window).mean()
    temp['ADX'] = 100 * abs((temp['+DI'] - temp['-DI']) / (temp['+DI'] + temp['-DI'])).ewm(com=window, min_periods=window).mean()

    return temp['ADX']

# Download historical data for various stocks
tickers = ['AMZN', 'AAPL', 'GOOG']
stock_data = {}

for t in tickers:
    data = yf.download(t, period='1mo', interval='5m') # 5 minute candles
    data.dropna(how='any', inplace=True)
    stock_data[t] = data
    
for s in stock_data:
    stock_data[s]['ADX'] = average_directional_index(stock_data[s], 20)