""""""  		  	   		 	 	 			  		 			     			  	 
"""MC2-P1: Market simulator.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	 	 			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		 	 	 			  		 			     			  	 
All Rights Reserved  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Template code for CS 4646/7646  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	 	 			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		 	 	 			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		 	 	 			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		 	 	 			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	 	 			  		 			     			  	 
or edited.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
We do grant permission to share solutions privately with non-students such  		  	   		 	 	 			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		 	 	 			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	 	 			  		 			     			  	 
GT honor code violation.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
-----do not edit anything above this line---  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Student Name: Wai Kay Kok (replace with your name)  		  	   		 	 	 			  		 			     			  	 
GT User ID: wkok6 (replace with your User ID)  		  	   		 	 	 			  		 			     			  	 
GT ID: 904075476 (replace with your GT ID)  		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
import datetime as dt
import numpy as np  		  	   		 	 	 			  		 			     			  	 	   		 	 	 			  		 			     			  	 
import pandas as pd  		  	   		 	 	 			  		 			     			  	 
from util import get_data		  	   		 	 	 			  		 			     			  	 
from glob import glob	 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def compute_portvals(  		  	   		 	 	 			  		 			     			  	 
    orders_file="./orders/orders.csv",  		  	   		 	 	 			  		 			     			  	 
    start_val=1000000,  		  	   		 	 	 			  		 			     			  	 
    commission=9.95,  		  	   		 	 	 			  		 			     			  	 
    impact=0.005,  		  	   		 	 	 			  		 			     			  	 
):  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    Computes the portfolio values.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
    :param orders_file: Path of the order file or the file object  		  	   		 	 	 			  		 			     			  	 
    :type orders_file: str or file object  		  	   		 	 	 			  		 			     			  	 
    :param start_val: The starting value of the portfolio  		  	   		 	 	 			  		 			     			  	 
    :type start_val: int  		  	   		 	 	 			  		 			     			  	 
    :param commission: The fixed amount in dollars charged for each transaction (both entry and exit)  		  	   		 	 	 			  		 			     			  	 
    :type commission: float  		  	   		 	 	 			  		 			     			  	 
    :param impact: The amount the price moves against the trader compared to the historical data at each transaction  		  	   		 	 	 			  		 			     			  	 
    :type impact: float  		  	   		 	 	 			  		 			     			  	 
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.  		  	   		 	 	 			  		 			     			  	 
    :rtype: pandas.DataFrame  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    # this is the function the autograder will call to test your code  		  	   		 	 	 			  		 			     			  	 
    # NOTE: orders_file may be a string, or it may be a file object. Your  		  	   		 	 	 			  		 			     			  	 
    # code should work correctly with either input  		  	   		 	 	 			  		 			     			  	 
    # TODO: Your code here  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
    orders = pd.read_csv(orders_file, index_col='Date', parse_dates=True, na_values=['nan']) # Read in orders file.
    orders.sort_index(inplace=True) # To ensure the dates are in chronological sequence.
    
    dates = orders.index.unique() # Extracts the dates.
    sd = dates[0]
    ed = dates[-1]
    syms = orders['Symbol'].unique().tolist() # Extracts stock symbols.

    prices = get_data(syms, pd.date_range(sd, ed)) # Read in price data for the stock symbols from the sd and ed.
    prices = prices[syms] # Exclude SPY from the dataframe.
    prices.ffill(inplace=True)  # Forward fill missing values if any.
    prices.bfill(inplace=True)  # Backward fill missing values if any.
    prices['Cash'] = 1.0    # Add a cash column.

    trades = prices.copy()  # Create a dataframe to keep track of trades executed.
    trades.loc[:,:] = 0 # Initialise it to zeros.

    # A for loop to update the trades dataframe based on the orders and prices dataframe
    for d in dates:
        d_orders = orders.loc[[d],:]
        d_orders.reset_index(drop=True, inplace=True)
        for i in range(d_orders.shape[0]):  # This inner loop process multiple orders in a single day.
            if d_orders.loc[i,'Order'].upper() == 'BUY':
                trades.loc[d,d_orders.loc[i,'Symbol']] += d_orders.loc[i,'Shares']
                trades.loc[d,'Cash'] -= prices.loc[d,d_orders.loc[i,'Symbol']]*(1+impact)*d_orders.loc[i,'Shares']
            else:
                trades.loc[d,d_orders.loc[i,'Symbol']] -= d_orders.loc[i,'Shares']
                trades.loc[d,'Cash'] += prices.loc[d,d_orders.loc[i,'Symbol']]*(1-impact)*d_orders.loc[i,'Shares']
    
            trades.loc[d,'Cash'] -= commission

    holdings = trades.copy()    # Create a dataframe to keep track of all holdings.
    holdings.iloc[0,-1] += start_val    # Starting cash holdings take into account starting value.
    holdings = holdings.cumsum()    # Compute cumulative holdings over the trading period.

    portfolio = holdings*prices     # Create a dataframe to keep tracks of daily stock and cash values over the trading period.
    portfolio['Total_value'] = portfolio.sum(axis=1)   # Add a column to keep track of daily portfolio values over the trading period.
    portvals = portfolio[['Total_value']]  # Extract a single column dataframe for porfolio values.

    return portvals		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def test_code():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    Helper function to test code  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    # this is a helper function you can use to test your code  		  	   		 	 	 			  		 			     			  	 
    # note that during autograding his function will not be called.  		  	   		 	 	 			  		 			     			  	 
    # Define input parameters  		  	   		 	 	 			  		 			     			  	 

    folder_path = 'orders'
    files_list = glob(folder_path+'/*.csv')   # To get all files in the folder together.
    file = open('results.txt', 'w')     # Open an output file to which the results are to be written.

    sv = 1000000 

    for f in files_list:
        of = f	 	 	 			  		 			     			  	  		  	   		 	 	 			  		 			     			  	 	  	   		 	 	 			  		 			     			  	                                                              
        # Process orders  		  	   		 	 	 			  		 			     			  	 
        portvals = compute_portvals(orders_file=of, start_val=sv)  		  	   		 	 	 			  		 			     			  	 
        if isinstance(portvals, pd.DataFrame):  		  	   		 	 	 			  		 			     			  	 
            portvals = portvals[portvals.columns[0]]  # just get the first column  		  	   		 	 	 			  		 			     			  	 
        else:  		  	   		 	 	 			  		 			     			  	 
            "warning, code did not return a DataFrame"  		  	   		 	 	 			  		 			     			  	 
        
        start_date = portvals.index[0]
        end_date = portvals.index[-1]
        cum_ret = (portvals.iloc[-1]/portvals.iloc[0])-1
        dr = (portvals/portvals.shift(1)) - 1 
        avg_daily_ret = dr.iloc[1:].mean()
        std_daily_ret = dr.iloc[1:].std()
        final_val = portvals.iloc[-1]
        sharpe_ratio = (avg_daily_ret/std_daily_ret)*np.sqrt(252)

        spx = get_data(['$SPX'], pd.date_range(start_date, end_date))   # To get SPX price data.
        spx = spx['$SPX']   # Exclude SPY from dataframe.
        spx.ffill(inplace=True)
        spx.bfill(inplace=True)

        cum_ret_spx = (spx.iloc[-1]/spx.iloc[0])-1
        dr_spx = (spx/spx.shift(1)) - 1 
        avg_daily_ret_spx = dr_spx.iloc[1:].mean()
        std_daily_ret_spx = dr_spx.iloc[1:].std()
        sharpe_ratio_spx = (avg_daily_ret_spx/std_daily_ret_spx)*np.sqrt(252)	     			  	 
  		  	   		 	 	 			  		 			     			  	 
        # Compare portfolio against $SPX
        print(f, file=file)	  	   		 	 	 			  		 			     			  	 
        print(f"Date Range: {start_date} to {end_date}", file=file)  		  	   		 	 	 			  		 			     			  	  		  	   		 	 	 			  		 			     			  	 
        print(f"Sharpe Ratio of Fund: {sharpe_ratio}", file=file) 
        print(f"Sharpe Ratio of $SPX: {sharpe_ratio_spx}", file=file) 		  	   		 	 	 			  		 			     			  	 		  	   		 	 	 			  		 			     			  	  		  	   		 	 	 			  		 			     			  	 
        print(f"Cumulative Return of Fund: {cum_ret}", file=file)
        print(f"Cumulative Return of $SPX: {cum_ret_spx}", file=file) 	  	   		 	 	 			  		 			     			  	 		  	   		 	 	 			  		 			     			  	   		  	   		 	 	 			  		 			     			  	 
        print(f"Standard Deviation of Fund: {std_daily_ret}", file=file)
        print(f"Standard Deviation of $SPX: {std_daily_ret_spx}", file=file)	  	   		 	 	 			  		 			     			  	  		  	   		 	 	 			  		 			     			  	 		  	   		 	 	 			  		 			     			  	 
        print(f"Average Daily Return of Fund: {avg_daily_ret}", file=file)  	
        print(f"Average Daily Return of $SPX: {avg_daily_ret_spx}", file=file)	  	   		 	 	 			  		 			     			  	  		  	   		 	 	 			  		 			     			  	   		  	   		 	 	 			  		 			     			  	 
        print(f"Final Portfolio Value: {final_val}", file=file)  	
        print('\n-----------------------------------------------------\n', file=file)	  	   		 	 	 			  		 			     			  	 

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

if __name__ == "__main__":  		  	   		 	 	 			  		 			     			  	 
    test_code()  		  	   		 	 	 			  		 			     			  	 
