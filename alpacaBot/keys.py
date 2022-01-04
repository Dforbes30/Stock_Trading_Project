#!/usr/bin/env python
# coding: utf-8
#this is supposed to hold api keys and enpoints since the secret key is meant to be kept secret
#thear clearly needs to be a file split to handle the additional enpoints and parameters
#but this file will hold all of it for now

paper_endpoint = "https://paper-api.alpaca.markets"
data_endpoint = "https://data.alpaca.markets/v1"
key_id = "PKN4EHMYG5PG89HR9M3Q"
secret_key = "bP7j04BL6NTVdCCKJbkV4E9qvl5udMTvp9dYbmj0"

tickers = ["Q.SPY"]
symbol = 'SPY'

#{"action": "auth", "key": "PKN4EHMYG5PG89HR9M3Q", "secret": "bP7j04BL6NTVdCCKJbkV4E9qvl5udMTvp9dYbmj0"}

#{"action": "authenticate","data": {"key_id": "PKN4EHMYG5PG89HR9M3Q", "secret_key": "bP7j04BL6NTVdCCKJbkV4E9qvl5udMTvp9dYbmj0"}}