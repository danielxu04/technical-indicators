# Technical Indicators
A Python-based collection of technical indicators for financial analysis. Whether you're a trader, analyst, or developer, this repository will be a powerful tool to enhance your market insights. 
<br /><br />

## 1. MACD - Moving Average Convergence Divergence

MACD, short for Moving Average Convergence Divergence, is a momentum indicator which calculates the disrepancy between two distinct moving averages of a particular asset's price. Typically, a fast-length 12-period moving average and a slow-length 26-period moving average are utilized in this calculation. <br /><br />
This technical indicator further utilizes the MACD line to derive another moving average known as the <strong>signal line</strong>, which operates on a 9-period basis. By observing the interaction between the MACD line and the signal line, one can discern bullish and bearish periods. This is often referred to as the 'crossover strategy'. If the MACD line cuts the signal line from below, it indicates a bullish period; if the signal line is cut from above, a bearish period is represented.  In the graphical representations provided, the **signal line** is denoted by the distinctive **orange line**, while the **MACD line** is represented by the **blue line**. <br /> <br />
The initial graph, focusing on the timeframe of January to April 2023 for the AMZN stock, exemplifies a successful prediction made by our MACD indicator. The bearish period is indicated by the signal line being crossed from above, which is visually highlighted by the dotted lines. In this particular case, the MACD indicator effectively elucidates the prevailing market trend, revealing a substantial and prolonged decline in the stock price.<br /><br />
<div align="center" border="black">
  <img src="https://github.com/danielxu04/technical-indicators/assets/106186118/43eaafa3-d3f7-4f6e-9ebe-1ed6d9edb3ef" width="75%" height="550px" />
</div>


<br /><br />
In the subsequent graph, which spans from November 2022 to February 2023 for the AMZN stock, we observe the MACD line intersecting the signal line from below, as illustrated by the intersection of dotted lines. This occurence coincides with a sudden surge in the stock price. Despite this sharp increase, it is not categorized as a bullish period due to its limited duration.
We proceed to observe the MACD line crossing the signal line from above, indicating the onset of a bearish period. This downward crossover signifies a shift in market sentiment and predicts a subsequent decline in stock price. 
<br /><br />
<div align="center" border="black">
  <img src="https://github.com/danielxu04/technical-indicators/assets/106186118/dd456618-2e69-49c4-8a0f-ec1bacbd27d4" width="75%" height="550px" />
</div>
<br /><br />
Due to its reputation for giving false positives - especially during a sideways market - this indicator is typically used in conjunction with other indicators. It is also noteworthy that MACD is a lagging indicator, meaning that it trails behind price action. Thus, it can confirm trends, but is by no means a predictive indicator.<br /><br />

## 2. ATR - Average True Range

ATR is a volatility based indicator. ATR focuses on total price movement, and helps visualize how volatile the market is as it moves. Specifically, ATR takes into account price movements in each period by considering:<br />
- High/Low difference of each period
- High/Previous Close difference
- Low/Previous Close difference
<br />
Also, ATR is most commonly associated with a 9 period, with the choice of either simple MA or exponential MA.
<br /><br />
By analyzing the price chart of GOOG stock from November 2022 to July 2023 using 1-day candlesticks, we observe the ATR graph, which showcases the greatest daily price range between the highest and lowest points. As seen at the intersection of dotted lines, the most volatile day in this period has a $5.15 USD high/low difference on February 9, 2023. This instance represents an exceptional case, but it underscores the significance of the ATR graph in accessing periods of heightened volatility. Employing the ATR graph enables investors to gauge market volatility, providing valuable insights for both short-term and long-term investment strategies, thereby enhancing their adaptability and effectiveness.
<br /><br />
<div align="center" border="black">
  <img src="https://github.com/danielxu04/technical-indicators/assets/106186118/f72cd6d2-cd30-4637-b064-d5d87b78c0dc" width="95%" height="550px" />
</div>
<br /><br />
Note that the ATR technical indicator is usually combined with other volitility indicators, such as the Bollinger Bands indicator, an indicator that approaches the notion of market volatility from a different angle.<br /><br /> 

## 3. Bollinger Bands

Bollinger Bands is another volatility indicator, which comprise of two lines that are typically plotted 2 standard deviations away (+, -) from a 20-period simple moving average line. However, it's important to note that the values for standard deviations and the period can vary and are not always fixed at 2 and 20, respectively. From a visual perspective, the bands widen during periods of heightened volatility and contract when volatility decreases. <br /><br />
As previously mentioned in the ATR section, Bollinger Bands are commonly used in conjunction with ATR and other volatility-based indicators. Each indicator offers a distinct viewpoint on volatility, complementing one another in the analysis. <br /><br />
In the candlestick plot provided, which displays AAPL stock from September 2022 to July 2023 with daily candlesticks, we can observe the effectiveness of Bollinger Bands (depicted by the blue lines). During periods of increased volatility, the bands expand, indicating wider price fluctuations. Conversely, the bands contract and become narrower during phases of reduced volatility. Note that the orange line in the middle represents the 20-period moving average of the stock price. 
<br /> <br />
<div align="center" border="black">
  <img src="https://github.com/danielxu04/technical-indicators/assets/106186118/6ff518da-a5e2-48f8-b04e-c9698d7702ce" width="95%" height="550px" />
</div>
<br /><br />

## 4. RSI - Relative Strength Index

RSI is a momentum oscillator that measures the speed and change of price movements. The RSI value is expressed on a scale from 0-100; values below 30 indicate that the asset is oversold, whereas values above 70 correlate to assets reaching overbought territory. <br /><br />
The RSI indicator helps traders and analysists identify potential trend reversals and assess the underlying strength/velocity of price movements. When the RSI surpasses the overbought threshold of 70, it suggests that the asset may be overvalued, and a price correction or trend reversal could occur. Conversely, when the RSI falls below the oversold threshold of 30, it indicates that the asset may be undervalued, potentially leading to a price recovery or trend reversal. <br /><br />
The following formula illustrates the typical RSI calculation method: <br />
```math
 RSI \space (step \space one) = 100 - \left[ 100 \over {1 + {{Ave \space Gain} \over {Ave \space Loss}}} \right]
\space \space \space RSI \space (step \space two) = 100 - \left[ 100 \over {1 + {{Previous \space Ave \space Gain * 13 + Current \space Gain} \over {Previous \space Ave \space Loss * 13 + Current \space Loss}}} \right]
```
<br />
Presented below is a monthly chart spanning June-July 2023, illustrating the price movements of the MSFT stock, with an accompanying RSI graph. While no instances are observed where the RSI surpasses the 70 threshold, there are notable time intervals where the RSI dips below 30. During these periods, a significant decline in the stock price becomes apparent, and can be observed. 
<br /> <br />
<div align="center" border="black">
  <img src="https://github.com/danielxu04/technical-indicators/assets/106186118/10327439-0a99-4dff-8047-c25890cc2c48" width="95%" height="550px" />
</div>
<br /><br />

## 5. ADX - Average Directional Index

ADX is an indicator that aims to measure the strength of a trend. Similar to the RSI, its values range from 0-100, and strength is quantified as per the intervals listed below:
- **0-25** : Absent/weak trend
- **25-50** : Strong trend
- **50-75** : Very strong trend
- **75-100** : Extremely strong trend
<br />
ADX is represented by positive values as it is a non-directional indicator. The ADX value does not provide any information regarding the trend direction, but rather focuses solely on meausring the strength of the trend. Its calculation involves determining the positive and negative directional movements by comparing successive highs and lows, and then obtaining the smoothed average fo the differences between them. <br /><br />
Here is a visualization of GOOG stock prices and its ADX graph for June-July 2023. Intuitively, a higher ADX correlates to a stronger and steeper trend, regardless of direction. In this graph, the highest ADX value is 54; very rarely, will there be a value in the 75-100 range.<br /><br />
<div align="center" border="black">
  <img src="https://github.com/danielxu04/technical-indicators/assets/106186118/216c50ba-db59-4724-b682-393b2f01214b" width="95%" height="550px" />
</div>
<br /><br />


