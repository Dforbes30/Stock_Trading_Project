# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 21:47:01 2022

@author: DFORB
"""
# =============================================================================
# We will create an actual IEX account later
# For now this is just the code taken from Part Time Larry so we
# know what to do when it comes time to compare API formats.
# =============================================================================
import requests
import json
import csv

Token = ''
symbol = 'AAPL'

URL = 'https://sandbox.iexapis.com/stable/stock/{}/ytd?token={}'.format(symbol,Token)

r = requests.get(URL)

json_data = json.loads(r.content)

csv_file = open('stock.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['date', 'open', 'high', 'low', 'close'])

for item in json_data:
    print(item)
    csv_writer.writerow([item['date'], item['open'], item['high'], item['low'], item['close']])

csv_file.close()
