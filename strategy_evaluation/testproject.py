"""  		  	   		 	 	 			  		 			     			  	 
Student Name: Wai Kay Kok (replace with your name)  		  	   		 	 	 			  		 			     			  	 
GT User ID: wkok6 (replace with your User ID)  		  	   		 	 	 			  		 			     			  	 
GT ID: 904075476 (replace with your GT ID)  		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 

import datetime as dt 		  	   		 	 	 			  		 			     			  	 
import numpy as np
import pandas as pd
import ManualStrategy as mstg
import marketsimcode as msc
import experiment1 as expt1
import experiment2 as expt2	 
from util import get_data			 	  		 			     			  	  	 	 			  		 			     			  	 

# Function for generating benchmark portfolio values.
def benchmark(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000, commission = 0.0, impact = 0.0):
    if type(symbol) != list:
        symbol = [symbol]
    prices = get_data(symbol, pd.date_range(sd, ed))
    prices = prices[symbol]
    prices.ffill(inplace=True) 
    prices.bfill(inplace=True)

    trades = prices.copy()
    trades.iloc[:,:] = 0
    trades.iloc[0,:] = 1000
    trades['Cash'] = -trades * prices * (1+impact)
    trades['Cash'] -= commission

    holdings = trades.copy()
    holdings.iloc[0,-1] += sv
    holdings = holdings.cumsum()

    prices['Cash'] = 1.0
    portfolio = holdings * prices
    portfolio['Total_value'] = portfolio.sum(axis=1)
    portvals = portfolio[['Total_value']]
    
    return portvals

def compute_metrics(portvals):  # Function for getting performance metrics.
    portvals = portvals/portvals.iloc[0]
    portvals = portvals.iloc[:,0]
    
    cr = (portvals.iloc[-1]/portvals.iloc[0])-1
    cr = np.round(cr, 6)
    dr = (portvals/portvals.shift(1)) - 1
    adr = dr.iloc[1:].mean()
    adr = np.round(adr, 6)
    sddr = dr.iloc[1:].std()
    sddr = np.round(sddr, 6)
    final_val = portvals.iloc[-1]
    final_val = np.round(final_val, 6)
    sharpe = (adr/sddr)*np.sqrt(252)
    sharpe = np.round(sharpe, 6)
    
    return [cr, adr, sddr, final_val, sharpe]

def author():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    :return: The GT username of the student  		  	   		 	 	 			  		 			     			  	 
    :rtype: str  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    return "wkok6"   		  	   		 	 	 			  		 			     			  	 

def study_group(self):
    """
    :return: A comma separated string of GT_Name of each member of your study group.
    # Example: "gburdell3, jdoe77, tbalch7" or "gburdell3" if a single individual working alone.
    :rtype: str
    """
    return "wkok6"  		  	   		 
	  	   		 	 	 			  		 			     			  	 
if __name__ == "__main__":
    
    np.random.seed(904075476)

# Manual Stratregy.
    ms = mstg.ManualStrategy(impact=0.005, commission=9.95)
    
    trades_in = ms.testPolicy(symbol = "JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000)
    trades_out = ms.testPolicy(symbol = "JPM", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000)
    
    portvals_in = msc.compute_portvals(trades_in, start_val = 100000, commission = 9.95, impact = 0.005)
    portvals_out = msc.compute_portvals(trades_out, start_val = 100000, commission = 9.95, impact = 0.005)
    
    portvals_bmk_in = benchmark(symbol = "JPM", sd=trades_in.index[0], ed=trades_in.index[-1], sv = 100000, commission = 9.95, impact = 0.005)
    portvals_bmk_out = benchmark(symbol = "JPM", sd=trades_out.index[0], ed=trades_out.index[-1], sv = 100000, commission = 9.95, impact = 0.005)
    
    metrics_in = compute_metrics(portvals_in)
    metrics_out = compute_metrics(portvals_out)
    metrics_bmk_in = compute_metrics(portvals_bmk_in)
    metrics_bmk_out = compute_metrics(portvals_bmk_out)

    results = pd.DataFrame([metrics_in, metrics_bmk_in, metrics_out, metrics_bmk_out], 
                           index=['Manual Strategy (In-Sample)', 'Benchmark (In-Sample)', 'Manual Strategy (Out-Sample)','Benchmark (Out-Sample)'], 
                           columns=['Cumulative Return','Mean Daily Return','Std Dev of Daily Return','Final Value','Sharpe Ratio']).T
    results.to_csv('manual_metrics.csv')

    portvals_in = portvals_in/portvals_in.iloc[0]
    portvals_out = portvals_out/portvals_out.iloc[0]
    portvals_bmk_in = portvals_bmk_in/portvals_bmk_in.iloc[0]
    portvals_bmk_out = portvals_bmk_out/portvals_bmk_out.iloc[0]

    portvals_trades_in = pd.concat([portvals_in, trades_in], axis=1)
    portvals_trades_out = pd.concat([portvals_out, trades_out], axis=1)
    long_entries_in = portvals_trades_in[portvals_trades_in.iloc[:,1]>0].index
    short_entries_in = portvals_trades_in[portvals_trades_in.iloc[:,1]<0].index
    long_entries_out = portvals_trades_out[portvals_trades_out.iloc[:,1]>0].index
    short_entries_out = portvals_trades_out[portvals_trades_out.iloc[:,1]<0].index
    
    mstg.plot_chart(portvals_in.index, portvals_in.iloc[:,0].values, portvals_bmk_in.iloc[:,0].values, long_entries_in, short_entries_in, 
            'Manual Strategy vs Benchmark (In-Sample)', 'Date', 'Normalized Price', [0.6,1.4], 'manual.1.png')
    mstg.plot_chart(portvals_out.index, portvals_out.iloc[:,0].values, portvals_bmk_out.iloc[:,0].values, long_entries_out, short_entries_out, 
            'Manual Strategy vs Benchmark (Out-Sample)', 'Date', 'Normalized Price', [0.8,1.1], 'manual.2.png')
    
# Experiment 1
    expt1.run_experiment()

# Experiment 2
    expt2.run_experiment(impact_values = [0,0.02,0.05,0.07])

   