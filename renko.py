# --------------------------------------------------------
# Author: Daniel Xu
# Date: 07/19/2023
# Description: A program that converts candlestick data into Renko Chart data
#   for AMZN, GOOG, AAPL
# --------------------------------------------------------

# Import libraries
import yfinance as yf
from stocktrends import Renko

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


def renko(df, hourly_df):
    temp = df.copy()
    temp.drop('Close', axis=1, inplace=True)
    temp.reset_index(inplace=True)
    temp.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
    renko_df = Renko(temp)
    renko_df.brick_size = 3 * round(average_true_range(hourly_df, 120).iloc[-1], 0)
    r = renko_df.get_ohlc_data()
    return r

# Download historical data for various stocks
tickers = ['AMZN', 'AAPL', 'GOOG']
stock_data = {}
hourly_data = {}
renko_data = {}

for t in tickers:
    data = yf.download(t, period='1mo', interval='5m') # 5 minute candles
    data.dropna(how='any', inplace=True)
    stock_data[t] = data
    data = yf.download(t, period='1y', interval='1h') # 5 minute candles
    data.dropna(how='any', inplace=True)
    hourly_data[t] = data
    
for s in stock_data:
    renko_data[s] = renko(stock_data[s], hourly_data[s])