# Technical Indicators
A Python-based collection of technical indicators for financial analysis. Whether you're a trader, analyst, or developer, this repository will be a powerful tool to enhance your market insights. 
<br />

## 1. MACD - Moving Average Convergence Divergence

MACD is a momentum indicator calculated by taking the difference of two set moving averages of a specific asset price. Usually, we use a fast-length 12 month MA and a slow-length 26 month MA. <br /><br />
This technical indicator uses the MACD line to calculate another moving average, depicted by the <strong>signal line</strong>. If the MACD line cuts the signal line from below, it indicates a bullish period; if the signal line is cut from above, a bearish period is represented. This is often referred to as the 'crossover strategy'. In the graphs below, the **orange line** is the **signal line**, and the **blue line** is the **MACD line**. <br /> <br />
The first graph (AMZN, Jan-Apr 2023) demonstrates a correct prediction made by our MACD indicator. The signal line being cut from above, centered upon by the dotted line, demonstrates a bearish period. In this case, this indicator represents a valid analysis, as we see stock fall by 25% over a prolonged period of time. <br /><br />
<div align="center" border="black">
  <img src="https://github.com/danielxu04/technical-indicators/assets/106186118/f0db1590-b67a-4e73-a351-921552c48834" width="65%" height="550px" />
</div>


<br /><br />
In this second graph (AMZN, Nov-Feb 2022-2023) the MACD line cuts the signal line from below (indicated by the intersection of the dotted lines), where we see an abrupt increase in stock price, but it would not be classified as a bullish period due to its short duration. Subsequently, after 0.5 weeks, we observe in the visualization that the MACD line cuts the signal line from above, resulting in a bearish period. 
<br /><br />
<div align="center" border="black">
  <img src="https://github.com/danielxu04/technical-indicators/assets/106186118/dd456618-2e69-49c4-8a0f-ec1bacbd27d4" width="65%" height="550px" />
</div>
<br /><br />
Due to its reputation for giving false positives - especially during a sideways market - this indicator is typically used in conjunction with other indicators. It is also noteworthy that MACD is a lagging indicator, meaning that it trails behind price action. Thus, it can confirm trends, but is by no means a predictive indicator.


