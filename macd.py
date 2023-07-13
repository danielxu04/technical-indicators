# --------------------------------------------------------
# Author: Daniel Xu
# Date: 07/12/2023
# Description: A program that exemplifies the technical indicator of Moving Average
#   Convergence Divergence using Python and Yahoo Finance
# --------------------------------------------------------

# Import libraries
import yfinance as yf
import matplotlib.pyplot as plt

# ADD_MACD_COLUMNS - adds columns to DataFrame df regarding MACD. Takes in 3 more 
#   parameters, moving average spans for slow, fast, and signal.
def add_macd_columns(df, slow, fast, signal):
    df_copy = df.copy()
    df_copy['Fast MA'] = df_copy['Adj Close'].ewm(span=fast, min_periods=fast).mean()
    df_copy['Slow MA'] = df_copy['Adj Close'].ewm(span=slow, min_periods=slow).mean()
    df_copy['MACD'] = df_copy['Fast MA'] - df_copy['Slow MA']
    df_copy['Signal'] = df_copy['MACD'].ewm(span=signal, min_periods=signal).mean()

    return df_copy.loc[:,['MACD', 'Signal']]

# Download historical data for various stocks
tickers = ['AMZN', 'AAPL', 'GOOG']
stock_data = {}

for t in tickers:
    data = yf.download(t, period='1mo', interval='15m') # 15 minute candles
    data.dropna(how='any', inplace=True)
    stock_data[t] = data
    
    
for stock in stock_data:
    stock_data[stock][['MACD', 'Signal']] = add_macd_columns(stock_data[stock], 26, 12, 9)