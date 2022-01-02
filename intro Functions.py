#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import import_ipynb
import keys
import alpaca_trade_api as tradeapi
import time


# In[4]:


secret_key = keys.secret_key
ID = keys.key_id
endpoint = keys.endpoint



if __name__ == '__main__':
    api = tradeapi.REST(ID,secret_key,endpoint)
    account = api.get_account()
    
    # Check if our account is restricted from trading.
    if account.trading_blocked:
        print('Account is currently restricted from trading.')
    # Check how much money we can use to open new positions.
    print('${} is available as buying power.'.format(account.buying_power))

    """
    With the Alpaca API, you can check on your daily profit or loss by
    comparing your current balance to yesterday's balance.
    """

    # Check our current balance vs. our balance at the last market close
    balance_change = float(account.equity) - float(account.last_equity)
    print(f'Today\'s portfolio balance change: ${balance_change}')
    
    # Get a list of all active assets.
    active_assets = api.list_assets(status='active')
    
    # Filter the assets down to just those on NASDAQ.
    nasdaq_assets = [a for a in active_assets if a.exchange == 'NASDAQ']
    #print(nasdaq_assets)
    
    
    # Check if AAPL is tradable on the Alpaca platform.
    aapl_asset = api.get_asset('AAPL')
    if aapl_asset.tradable:
        print('We can trade AAPL.')
        
        
    clock = api.get_clock()
    print('The market is {}'.format('open.' if clock.is_open else 'closed.'))

    # Check when the market was open on Dec. 1, 2018
    date = '2018-12-01'
    calendar = api.get_calendar(start=date, end=date)[0]
    print('The market opened at {} and closed at {} on {}.'.format(
        calendar.open,
        calendar.close,
        date
    ))
    # Get daily price data for AAPL over the last 5 trading days.
    barset = api.get_barset('AAPL', 'day', limit=5)
    aapl_bars = barset['AAPL']

    # See how much AAPL moved in that timeframe.
    week_open = aapl_bars[0].o
    week_close = aapl_bars[-1].c
    percent_change = (week_close - week_open) / week_open * 100
    print('AAPL moved {}% over the last 5 days'.format(percent_change))
    
    
    # Submit a market order to buy 1 share of Apple at market price
    api.submit_order(
        symbol='AAPL',
        qty=1,
        side='buy',
        type='market',
        time_in_force='gtc'
    )

    # Submit a limit order to attempt to sell 1 share of AMD at a
    # particular price ($20.50) when the market opens
#     api.submit_order(
#         symbol='AMD',
#         qty=1,
#         side='sell',
#         type='limit',
#         time_in_force='opg',
#         limit_price=20.50
#     )

# The security we'll be shorting
    symbol = 'TSLA'

    # Submit a market order to open a short position of one share
    order = api.submit_order(symbol, 1, 'sell', 'market', 'day')
    print("Market order submitted.")

    # Submit a limit order to attempt to grow our short position
    # First, get an up-to-date price for our symbol
    symbol_bars = api.get_barset(symbol, 'minute', 1).df.iloc[0]
    symbol_price = symbol_bars[symbol]['close']
    # Submit an order for one share at that price
    order = api.submit_order(symbol, 1, 'sell', 'limit', 'day', symbol_price)
    print("Limit order submitted.")

    # Wait a second for our orders to fill...
    print('Waiting...')
    time.sleep(1)

    # Check on our position
    position = api.get_position(symbol)
    if int(position.qty) < 0:
        print(f'Short position open for {symbol}')
    # Submit a market order and assign it a Client Order ID.
    api.submit_order(
        symbol='AAPL',
        qty=1,
        side='buy',
        type='market',
        time_in_force='gtc',
        client_order_id='my_first_order'
    )

    # Get our order using its Client Order ID.
    my_order = api.get_order_by_client_order_id('my_first_order')
    print('Got order #{}'.format(my_order.id))


# In[ ]:





# In[ ]:




