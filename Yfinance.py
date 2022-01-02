#!/usr/bin/env python
# coding: utf-8

# In[118]:


import yfinance as yf 
import datetime 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


np.set_printoptions(suppress=True)

MSFT = yf.Ticker('msft')
exp_dates = MSFT.options

exp_dates_sample = exp_dates[:5]

for date in exp_dates_sample:
    options_data = MSFT.option_chain(date)
    calls_data = options_data.calls
    strikes = calls_data['strike']
    imp_vols = calls_data['impliedVolatility']
    
    strikes_arr = np.array(strikes)[np.newaxis].T
    imp_vols_arr = np.array(imp_vols)[np.newaxis].T
    cols = np.hstack((strikes_arr, imp_vols_arr))
    plt.plot(strikes_arr, imp_vols_arr)
plt.legend(exp_dates_sample)


# In[ ]:





# In[ ]:




