import numpy as np
import pandas as pd
import streamlit as st
import base64
import requests
import xlsxwriter
import math
import requests
import json 
import time
# from secrets import IEX_CLOUD_API_TOKEN
#GET /ref-data/cryptos/symbols

# st.write("""
# # Simple Crypto Price App

# Shown are the stock closing price and volume of Bitcoin!
# """)
# symbol = 'AAPL'
iex_api_key = 'api_key'
api_url = f'https://cloud.iexapis.com/stable/crypto/btcusd/price/quote?token={iex_api_key}'
# list = ['BTC']
data = requests.get(api_url).json()

print (data)