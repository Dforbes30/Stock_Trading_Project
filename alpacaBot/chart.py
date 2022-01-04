# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 22:36:31 2022

@author: DFORB
"""

import plotly.graph_objects as go
import pandas
import yfinance as yf
import plotly.io as pio
# pio.renderers.default = 'svg'
pio.renderers.default = 'browser'


nio = yf.Ticker("AAPL")

history = nio.history(period="ytd")

df = pandas.DataFrame(history)


input = go.Candlestick(x=df.index, open=df['Open'], high=df['High'],
                       low=df['Low'],
                       close=df['Close'])

figure = go.Figure(data=[input])

figure.layout.xaxis.type = 'category'
figure.show()

# figure.write_html('aapl.html', auto_open=True)
