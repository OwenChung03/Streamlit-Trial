import numpy as np
import pandas as pd
import streamlit as st
import base64
import requests
import math
import requests
import json 
import time
# from secrets import IEX_CLOUD_API_TOKEN
#GET /ref-data/cryptos/symbols
IEX_CLOUD_API_TOKEN = "pk_8e2a036135224e6986bdcc0151e51f2d"
base_url = 'https://cloud.iexapis.com/v1'

st.write("""
# Simple Crypto Price App

Shown are the current price and volume of Bitcoin!
""")
st.subheader("All Cryptos information allow for selection")
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950, 2020))))
end_point = '/ref-data/crypto/symbols'
api_url = f'{base_url}{end_point}?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()
df = pd.DataFrame(data=data)
st.write(df)
st.write("Current Price")
list = ['btcusd', 'ethusd', 'avaxusdt', 'usdcusdt']
for i in range(4):
    symbol = list[i]
    end_point = f'/crypto/{symbol}/price'
    api_url = f'{base_url}{end_point}?token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(api_url).json()
    df = pd.DataFrame(data=data, index = [0])
    st.write(df)

st.write("Current Booking Information")
for i in range(4):
    symbol = list[i]
    end_point = f'/crypto/{symbol}/quote'
    api_url = f'{base_url}{end_point}?token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(api_url).json()
    df = pd.DataFrame(data=data, index = [0])
    st.write(df)