#Imports
import numpy as np
import pandas as pd
import datetime
import pandas_datareader as web
from math import log, sqrt, pi, exp
from scipy.stats import norm
import yfinance as yf

#Normal Distributions
def d1(S,K,T,r,sigma):
    return(log(S/K)+(r+sigma**2/2.)*T)/(sigma*sqrt(T))
def d2(S,K,T,r,sigma):
    return d1(S,K,T,r,sigma)-sigma*sqrt(T)

#Calculating Call and put prices

def bs_call(S,K,T,r,sigma):
    return S*norm.cdf(d1(S,K,T,r,sigma))-K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))

def bs_put(S,K,T,r,sigma):
    return K*exp(-r*T)-S+bs_call(S,K,T,r,sigma)

# Calculating Premiums
stock = 'SPY'
expiry = '12-16-2022'
strike_price = 370

today = datetime.datetime.today()
one_year_ago = today.replace(year=today.year-1)

df = web.DataReader(stock, 'yahoo', one_year_ago, today)

df = df.sort_values(by="Date")
df = df.dropna()
df = df.assign(close_day_before=df.Close.shift(1))
df['returns'] = ((df.Close - df.close_day_before)/df.close_day_before)

sigma = np.sqrt(252) * df['returns'].std()
one_day = datetime.timedelta(1)
uty = (web.DataReader(
    "^TNX", 'yahoo', today-one_day, today)['Close'].iloc[-1])/100
lcp = df['Close'].iloc[-1]
t = (datetime.datetime.strptime(expiry, "%m-%d-%Y") - datetime.datetime.utcnow()).days / 365

print('The Option Price is: ', bs_call(lcp, strike_price, t, uty, sigma))


#Calculating the Greeks


def call_implied_volatility(Price, S, K, T, r):
    sigma = 0.001
    while sigma < 1:
        Price_implied = S * \
            norm.cdf(d1(S, K, T, r, sigma))-K*exp(-r*T) * \
            norm.cdf(d2(S, K, T, r, sigma))
        if Price-(Price_implied) < 0.001:
            return sigma
        sigma += 0.001
    return "Not Found"

def put_implied_volatility(Price, S, K, T, r):
    sigma = 0.001
    while sigma < 1:
        Price_implied = K*exp(-r*T)-S+bs_call(S, K, T, r, sigma)
        if Price-(Price_implied) < 0.001:
            return sigma
        sigma += 0.001
    return "Not Found"

print("Implied Volatility: " +
      str(100 * call_implied_volatility(bs_call(lcp, strike_price, t, uty, sigma,), lcp, strike_price, t, uty,)) + " %")



#def call_delta(S,K,T,r,sigma):
#    return norm.cdf(d1(S,K,T,r,sigma))
#def call_gamma(S,K,T,r,sigma):
#    return norm.pdf(d1(S,K,T,r,sigma))/(S*sigma*sqrt(T))
#def call_vega(S,K,T,r,sigma):
#    return 0.01*(S*norm.pdf(d1(S,K,T,r,sigma))*sqrt(T))
#def call_theta(S,K,T,r,sigma):
#    return 0.01*(-(S*norm.pdf(d1(S,K,T,r,sigma))*sigma)/(2*sqrt(T)) - r*K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma)))
#def call_rho(S,K,T,r,sigma):
#    return 0.01*(K*T*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma)))
#
#def put_delta(S,K,T,r,sigma):
#    return -norm.cdf(-d1(S,K,T,r,sigma))
#def put_gamma(S,K,T,r,sigma):
#    return norm.pdf(d1(S,K,T,r,sigma))/(S*sigma*sqrt(T))
#def put_vega(S,K,T,r,sigma):
#    return 0.01*(S*norm.pdf(d1(S,K,T,r,sigma))*sqrt(T))
#def put_theta(S,K,T,r,sigma):
#    return 0.01*(-(S*norm.pdf(d1(S,K,T,r,sigma))*sigma)/(2*sqrt(T)) + r*K*exp(-r*T)*norm.cdf(-d2(S,K,T,r,sigma)))
#def put_rho(S,K,T,r,sigma):
#    return 0.01*(-K*T*exp(-r*T)*norm.cdf(-d2(S,K,T,r,sigma)))
