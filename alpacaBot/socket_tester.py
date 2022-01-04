# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 18:45:19 2022

@author: DFORB
"""
import websocket
import json
from keys import *


def on_open(ws):
    print("opened")
    auth_data = {
        "action": "authenticate",
        "data": {
            "key_id": key_id,
            "secret_key": secret_key}
        }
    ws.send(json.dumps(auth_data))

    channel_data = {"action": "listen",
                    "data": {"streams": [tickers]}}
    ws.send(json.dumps(channel_data))


def on_message(ws, message):
    print("received a message")
    print(message)


def on_close(ws):
    print("closed connection")


socket = "wss://data.alpaca.markets/stream"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()
