# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 21:47:39 2022

@author: DFORB
"""

#this was taken from Part Time Larry. The info is useful for setting up my own scripts but the
# Alpaca API has since been updated so this would not work
import requests, json, csv
from datetime import datetime

ALPACA_API_KEY = "YOUR APLACA KEY"
TICKER = 'AAPL'
START_DATE = '2019-01-01'
END_DATE = '2019-12-27'
POLYGON_URL = 'https://api.polygon.io/v2/aggs/ticker/{}/range/1/day/{}/{}?apiKey={}'

r = requests.get(POLYGON_URL.format(TICKER, START_DATE, END_DATE, ALPACA_API_KEY))

data = json.loads(r.content)

print("date,open,high,low,close")

for item in data['results']:
    formatted_date = datetime.fromtimestamp(item['t'] / 1000)
    date_only = formatted_date.strftime('%Y-%m-%d')

    print("{},{},{},{},{}".format(date_only, item['o'], item['h'], item['l'], item['c']))
