"""  		  	   		 	 	 			  		 			     			  	 
Student Name: Wai Kay Kok (replace with your name)  		  	   		 	 	 			  		 			     			  	 
GT User ID: wkok6 (replace with your User ID)  		  	   		 	 	 			  		 			     			  	 
GT ID: 904075476 (replace with your GT ID)  		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
import datetime as dt
import numpy as np  		  	   		 	 	 			  		 			     			  	 	   		 	 	 			  		 			     			  	 
import pandas as pd  		  	   		 	 	 			  		 			     			  	 
from util import get_data		  	   		 	 	 			  		 			     			  	  	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def compute_portvals(trades, start_val = 100000, commission = 0.0, impact = 0.0):
    
    dates = trades.index.unique()
    sd = dates[0]
    ed = dates[-1]
    syms = trades.columns.tolist()

    prices = get_data(syms, pd.date_range(sd, ed))
    prices = prices[syms]
    prices.ffill(inplace=True) 
    prices.bfill(inplace=True)
    prices['Cash'] = 1.0

    trades['Cash'] = 0.0

    for d in dates:
        for sym in syms:
            if trades.loc[d,sym] > 0:
                trades.loc[d,'Cash'] -= prices.loc[d,sym]*(1+impact)*trades.loc[d,sym]
            elif trades.loc[d,sym] < 0:
                trades.loc[d,'Cash'] -= prices.loc[d,sym]*(1-impact)*trades.loc[d,sym]
            trades.loc[d,'Cash'] -= commission

    holdings = trades.copy()
    holdings.iloc[0,-1] += start_val
    holdings = holdings.cumsum()

    portfolio = holdings*prices
    portfolio ['Total_value'] = portfolio.sum(axis=1)
    portvals = portfolio [['Total_value']]

    return portvals	     			  	 
  		  	   		 	 	 			  		 			     			  	 
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
	  	   		 	 	 			  		 			     			  	 
