"""  		  	   		 	 	 			  		 			     			  	 
Student Name: Wai Kay Kok (replace with your name)  		  	   		 	 	 			  		 			     			  	 
GT User ID: wkok6 (replace with your User ID)  		  	   		 	 	 			  		 			     			  	 
GT ID: 904075476 (replace with your GT ID)  		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
import datetime as dt
import numpy as np  		  	   		 	 	 			  		 			     			  	 	   		 	 	 			  		 			     			  	 
import pandas as pd  		  	   		 	 	 			  		 			     			  	 
import matplotlib.pyplot as plt
import matplotlib.dates as md  	   		 	 	 			  		 			     			  	  	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def momentum(prices_df, symbol='JPM', period=10):   # This indicator not used.
    momentum = prices_df.copy()
    momentum['Momentum'] = prices_df.pct_change(10)*100

    return momentum['Momentum']

def commodity_channel(prices_df, symbol='JPM', period=20, constant=0.015): # This indicator not used.
    cci = prices_df.copy()
    cci['Adj High'] = cci['High'] * cci['Adj Close'] / cci['Close']
    cci['Adj Low'] = cci['Low'] * cci['Adj Close'] / cci['Close']
    cci['Average Price'] = (cci['Adj High'] + cci['Adj Low'] + cci['Adj Close']) / 3
    cci['SMA'] = cci['Average Price'].rolling(window=period).mean()
    cci['Mean Deviation'] = cci['Average Price'].rolling(window=period).apply(lambda x: np.mean(np.abs(x - np.mean(x))))
    cci['CCI'] = (cci['Average Price'] - cci['SMA']) / (constant * cci['Mean Deviation'])
    
    return cci['CCI']

def percent_B(prices_df, symbol='JPM', period=20, std_dev=2):
    pB = prices_df.copy()
    pB['SMA'] = pB["Adj Close"].rolling(window=period).mean()
    pB['MStd_Dev'] = pB["Adj Close"].rolling(window=period).std()
    pB['Upper Band'] = pB['SMA'] + (pB['MStd_Dev'] * std_dev)
    pB['Lower Band'] = pB['SMA'] - (pB['MStd_Dev'] * std_dev)
    pB['%B'] = (pB["Adj Close"] - pB['Lower Band']) / (pB['Upper Band'] - pB['Lower Band']) * 100
    
    return pB['%B']

def percentage_price_osc(prices_df, symbol='JPM', period1=12, period2=26):
    ppo = prices_df.copy()
    ppo['ema1'] = ppo["Adj Close"].ewm(span=period1, adjust=False).mean()
    ppo['ema2'] = ppo["Adj Close"].ewm(span=period2, adjust=False).mean()
    ppo['%price_osc'] = ((ppo['ema1']-ppo['ema2'])/ppo['ema2'])*100

    return ppo['%price_osc']

def price_sma(prices_df, symbol='JPM', period=20):
    pr_sma = prices_df.copy()
    pr_sma['SMA'] = pr_sma["Adj Close"].rolling(window=period).mean()
    pr_sma['Price-SMA Ratio'] = pr_sma['Adj Close'] / pr_sma['SMA']

    return pr_sma['Price-SMA Ratio']
  		  	   		 	 	 			  		 			     			  	 
def author():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    :return: The GT username of the student  		  	   		 	 	 			  		 			     			  	 
    :rtype: str  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    return "wkok6"  # Change this to your user ID  		  	   		 	 	 			  		 			     			  	 

def study_group(self):
    """
    :return: A comma separated string of GT_Name of each member of your study group.
    # Example: "gburdell3, jdoe77, tbalch7" or "gburdell3" if a single individual working alone.
    :rtype: str
    """
    return "wkok6"  		  	   		 
	  	   		 	 	 			  		 			     			  	 
