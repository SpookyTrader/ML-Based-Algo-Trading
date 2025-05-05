"""  		  	   		 	 	 			  		 			     			  	 
Student Name: Wai Kay Kok (replace with your name)  		  	   		 	 	 			  		 			     			  	 
GT User ID: wkok6 (replace with your User ID)  		  	   		 	 	 			  		 			     			  	 
GT ID: 904075476 (replace with your GT ID)  		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
import datetime as dt
import numpy as np  		  	   		 	 	 			  		 			     			  	 	   		 	 	 			  		 			     			  	 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as md	  	   		 	 	 			  		 			     			  	 
from util import get_data
import TheoreticallyOptimalStrategy as tos
import marketsimcode as msc
import indicators as idr 	 			  		 			     			  	  	 	 			  		 			     			  	 
 	   		 	 	 			  		 			     			  	 
def benchmark(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000):  # Function for getting benchmark(buy and hold) portfolio value.
    if type(symbol) != list:
        symbol = [symbol]
    prices = get_data(symbol, pd.date_range(sd, ed))
    prices = prices[symbol]
    prices.ffill(inplace=True) 
    prices.bfill(inplace=True)

    trades = prices.copy()
    trades.iloc[:,:] = 0
    trades.iloc[0,:] = 1000
    trades['Cash'] = -trades * prices

    holdings = trades.copy()
    holdings.iloc[0,-1] += sv
    holdings = holdings.cumsum()

    prices['Cash'] = 1.0
    portfolio = holdings * prices
    portfolio['Total_value'] = portfolio.sum(axis=1)
    portvals = portfolio[['Total_value']]
    
    return portvals

def compute_metrics(portvals):  # Function for getting portfolio's metrics.
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

def plot_chart(x, y1, y2, title, xlabel, ylabel, ylim, color1, color2, legend1, legend2, chart_name): # Function for plotting chart (used only for TOS part). 
    plt.plot(x, y1, color=color1, label=legend1, linewidth=0.8)
    plt.plot(x, y2, color=color2, label=legend2, linewidth=0.8)
    plt.title(title)
    plt.xlabel(xlabel) 
    plt.ylabel(ylabel)
    plt.ylim(ylim)
    plt.gca().xaxis.set_major_locator(md.MonthLocator(interval=2))
    plt.xticks(rotation=90)
    plt.grid(True)
    # plt.text(0.5, 0.5, 'wkok6@gatech.edu', fontsize=50, color='gray', ha='center', va='center', alpha=0.5, rotation=35, transform=plt.gca().transAxes)
    plt.legend()
    plt.savefig(chart_name, bbox_inches='tight')
    plt.close()

# Function that wraps the get_data function in util.py to fetch stock data from mutiple columns.
def get_stocks_data(symbol='JPM', sd = dt.datetime(2008, 1, 1), ed = dt.datetime(2009,12,31), cols="Adj Close"):
    if type(symbol) != list:
        symbol = [symbol]
    if type(cols) != list:
        cols = [cols]
    for c in cols:
        if cols.index(c)==0:
            prices = get_data(symbols=symbol, dates=pd.date_range(sd, ed), colname=c)
            prices = prices[symbol]
        else:
            df = get_data(symbols=symbol, dates=pd.date_range(sd, ed), colname=c)
            df = df[symbol]
            prices = pd.concat([prices, df], axis=1)
        
    prices.ffill(inplace=True) 
    prices.bfill(inplace=True)

    prices.columns = cols

    return prices

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

# Part 1: Theoretical Optimal Stratregy.

    trades = tos.testPolicy(symbol = "JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000)
    portvals = msc.compute_portvals(trades, start_val = 100000, commission = 0.0, impact = 0.0)
    metrics = compute_metrics(portvals)
    portvals_bmk = benchmark(symbol = "JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000)
    metrics_bmk = compute_metrics(portvals_bmk)
    results = pd.DataFrame([metrics, metrics_bmk], 
             index=['Theoretically Optimal Strategy','Benchmark'],
             columns=['Cumulative Return','Mean Daily Return','Std Dev of Daily Return','Final Value','Sharpe Ratio']).T
    results.to_csv('tos_vs_benchmark.csv')

    portvals = portvals/portvals.iloc[0]
    portvals = portvals.iloc[:,0]
    portvals_bmk = portvals_bmk/portvals_bmk.iloc[0]
    portvals_bmk = portvals_bmk.iloc[:,0]
    plot_chart(portvals.index, portvals.values, portvals_bmk.values, 'Theoretically Optimal Strategy vs Benchmark', 'Date', 
               'Normalized Price', [0,7], 'red', 'purple', 'Theoretically Optimal Portfolio', 'Benchmark','TOS.png')

# Part 2: Technical Indicators

    prices = get_stocks_data() # Get stock prices for computing all indicators, except CCI.
    prices_cci = get_stocks_data(cols=['High','Low','Close','Adj Close'])   # Get stock prices for computing CCI.

    momentum = idr.momentum(prices_df=prices, chart=True)
    cci = idr.commodity_channel(prices_df=prices_cci, chart=True)
    pB = idr.percent_B(prices_df=prices, chart=True)
    ppo = idr.percentage_price_osc(prices_df=prices, chart=True)
    pr_sma = idr.price_sma(prices_df=prices, chart=True)