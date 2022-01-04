# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 04:11:10 2022

@author: DFORB
"""
# =============================================================================
# this is starting with crypto but will be transferred to equity securities
# Larry uses coinbase but I did not want added clutter in my email so I used
# Alpaca which is less robust but would still help me with this excercise
# the initial strategy from Larry involves using the three green soldiers
# strategy
# its a red candlestick followed by a series of three green ones over a time
# period
# the strategy enters a bracke order at the close price of the third candle and
# has a profit taking price of twice the difference between the close of the
# first
# candle and the close of the third
# the loss price is the closing price of the first candle but
# he has not outlined a real stoploss. an optimal stop is just math based or
# will
# be included and easily implemented in one the libraries that we downloaded
# the bars format Larry uses are also wrong. The updating problem could be fixed
# with some NP array but that will be explored later.
# =============================================================================

import websocket
import json
from keys import *
import dateutil.parser

minutes_processed = {}
minute_candlesticks = []
current_tick = None
previous_tick = None

first_exchange = "CBSE"
second_exchange = "FTX"


def on_open(ws):
    print("opened")
    auth_data = {"action": "auth", "key": key_id, "secret": secret_key}
    ws.send(json.dumps(auth_data))
    channel_data = {"action": "subscribe", "trades": ["BTCUSD"]}
    ws.send(json.dumps(channel_data))


def on_message(ws, message):

    global current_tick, previous_tick

    previous_tick = current_tick
    current_tick = json.loads(message)

    #print("===received tick===")

    # print(current_tick)

    # print("{} @ {}".format(current_tick[0]['c'], current_tick[0]['t']))

    tick_datetime_object = dateutil.parser.parse(current_tick[0]['t'])
    tick_time = tick_datetime_object.strftime("%m/%d/%Y %H:%M")

    if tick_time not in minutes_processed:

        #print("starting new candlestick")
        minutes_processed[tick_time] = True
        print(minutes_processed)

        if len(minute_candlesticks) > 0:
            minute_candlesticks[-1]['Close'] = previous_tick[0]['p']

        minute_candlesticks.append({
            "minute": tick_time,
            "open": current_tick[0]["p"],
            "high": current_tick[0]["p"],
            "low": current_tick[0]["p"]})

        print("=== candlesticks ===")
        print(minute_candlesticks)




    if len(minute_candlesticks) > 0:
        current_candlestick = minute_candlesticks[-1]
        if current_tick[0]["p"] > current_candlestick["high"]:
            current_candlestick["high"] = current_tick[0]["p"]
        if current_tick[0]["p"] < current_candlestick["low"]:
            current_candlestick["low"] = current_tick[0]["p"]


def on_close(ws):
    print("closed connection")


socket = "wss://stream.data.alpaca.markets/v1beta1/crypto?exchanges=CBSE"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()