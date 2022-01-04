# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 21:47:00 2022

@author: DFORB
"""

import yfinance as yf

nio = yf.Ticker("NIO")

history = nio.history(period = "max")

print(history)