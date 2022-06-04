import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Simple Crypto Price App

Shown are the stock closing price and volume of Bitcoin!
""")
cryptocurrencies = ['BTC-USD', 'ETH-USD', 'XRP-USD','DOGE-USD']
for i in range(4):
    tickerData = yf.Ticker(cryptocurrencies[i])
    tickerDf = tickerData.history(period = '1d', start = '2010-5-31', end = '2020-5-31')
    st.write("The graph of Closing " + cryptocurrencies[i] + " are as follows:")
    st.line_chart(tickerDf.Close)
    st.write("The graph of Volume " + cryptocurrencies[i] + " are as follows:")
    st.line_chart(tickerDf.Volume) 