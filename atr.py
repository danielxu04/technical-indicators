# --------------------------------------------------------
# Author: Daniel Xu
# Date: 07/13/2023
# Description: A program that illustrates the technical indicator of Average
#   True Range using Python and Yahoo Finance
# --------------------------------------------------------

# Import libraries
import yfinance as yf

# GET_ATR_COLUMN - adds columns to DataFrame df regarding ATR. Takes in a window
#   variable used to calculate Rolling Average'
def get_atr_column(df, window):
    df_copy = df.copy()
    df_copy['High-Low'] = df_copy['High'] - df_copy['Low']
    df_copy['High-PC'] = df_copy['High'] - df['Adj Close'].shift(1) # shift to PREVIOUS close
    df_copy['Low-PC'] = df_copy['Low'] - df['Adj Close'].shift(1)
    df_copy['True Range'] = df_copy[['High-Low', 'High-PC', 'Low-PC']].max(axis=1, skipna=False)
    
    # Using 'com' instead of 'span' will get us closer to yfinance's Exponential Moving Average
    #   'span' is closer to TradingView's algorithm for EMA
    df_copy['ATR'] = df_copy['True Range'].ewm(span=window, min_periods=window).mean()
    
    return df_copy['ATR']

# Download historical data for various stocks
tickers = ['AMZN', 'AAPL', 'GOOG']
stock_data = {}

for t in tickers:
    data = yf.download(t, period='1mo', interval='15m') # 15 minute candles
    data.dropna(how='any', inplace=True)
    stock_data[t] = data
    
# Apply the ATR column function to each stock
for s in stock_data:
    stock_data[s]['ATR'] = get_atr_column(stock_data[s], 14)
    