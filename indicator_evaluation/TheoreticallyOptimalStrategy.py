"""  		  	   		 	 	 			  		 			     			  	 
Student Name: Wai Kay Kok (replace with your name)  		  	   		 	 	 			  		 			     			  	 
GT User ID: wkok6 (replace with your User ID)  		  	   		 	 	 			  		 			     			  	 
GT ID: 904075476 (replace with your GT ID)  		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
import datetime as dt
import numpy as np  		  	   		 	 	 			  		 			     			  	 	   		 	 	 			  		 			     			  	 
import pandas as pd  		  	   		 	 	 			  		 			     			  	 
from util import get_data		  	   		 	 	 			  		 			     			  	  	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def testPolicy(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000):
    if type(symbol) != list:
        symbol = [symbol]
    prices = get_data(symbol, pd.date_range(sd, ed))
    prices = prices[symbol]
    prices.ffill(inplace=True) 
    prices.bfill(inplace=True)

    daily_return = (prices/prices.shift(1))-1
    daily_return = daily_return.shift(-1)

    strategy = daily_return.copy()
    for c in daily_return.columns:
        strategy[c] = daily_return[c].apply(lambda x: 'BUY' if x>0 else ('SELL' if x<0 else 'NO ACTION'))

    trades = daily_return.copy()
    trades.loc[:,:] = 0

    for sym in daily_return.columns:
        for d in daily_return.index:
            position = trades.loc[:d,sym].cumsum().iloc[-1]
            if strategy.loc[d,sym] == 'BUY':
                if position >= 1000:
                    continue
                elif position < 0:
                    trades.loc[d,sym] = 2000
                else:
                    trades.loc[d,sym] = 1000
            elif strategy.loc[d,sym] == 'SELL':
                if position <= -1000:
                    continue
                elif position > 0:
                    trades.loc[d,sym] = -2000
                else:
                    trades.loc[d,sym] = -1000
    return trades
  		  	   		 	 	 			  		 			     			  	 
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
	  	   		 	 	 			  		 			     			  	 
