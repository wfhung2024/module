#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import scipy.stats as scs
import statsmodels.api as sm
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime as dt
get_ipython().run_line_magic('matplotlib', 'inline')
pd.options.mode.chained_assignment = None # default='warn'
import warnings
warnings.simplefilter('ignore')
import yfinance as yf

def stat(df):
    u = df.mean()
    s = df.std()
    n = df.count()
    return print('t-ratio:', round(u/(s/np.sqrt(n)),2))


# In[ ]:


def trans(keyvar):
    url='https://raw.githubusercontent.com/wfhung2024/data/main/RET.csv'
    df = pd.read_csv(url)
    keydf = df.pivot(index='time',columns='firm',values=keyvar)
    keydf.index = pd.to_datetime((keydf.index*100+1).astype(str))
    keydf.index = pd.date_range(keydf.index[0],periods=len(keydf),freq='M')
    return keydf

def sr(x):
    return x.mean()*12**0.5/x.std()
