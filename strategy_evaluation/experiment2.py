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
import StrategyLearner as sl
import marketsimcode as msc
import indicators as idr 	 			  		 			     			  	  	 	 			  		 			     			  	 

# Function for generating benchmark portforlio values.  		 	 	 			  		 			     			  	 
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

def plot_lines(data, title, xlabel, ylabel, ylim, legend, chart_name):  # Function for producing line chart.
    y1, y2, y3, y4 = data
    x = y1.index
    y1 = y1.iloc[:,0].values
    y2 = y2.iloc[:,0].values
    y3 = y3.iloc[:,0].values
    y4 = y4.iloc[:,0].values
    plt.plot(x, y1, color='red', linewidth=0.8, label='Impact = '+str(legend[0]))
    plt.plot(x, y2, color='blue', linewidth=0.8, label='Impact = '+str(legend[1]))
    plt.plot(x, y3, color='purple', linewidth=0.8, label='Impact = '+str(legend[2]))
    plt.plot(x, y4, color='green', linewidth=0.8, label='Impact = '+str(legend[3]))
    plt.title(title)
    plt.xlabel(xlabel) 
    plt.ylabel(ylabel)
    plt.ylim(ylim)
    plt.gca().xaxis.set_major_locator(md.MonthLocator(interval=2))
    plt.xticks(rotation=90)
    plt.grid(False)
    # plt.text(0.5, 0.5, 'wkok6@gatech.edu', fontsize=50, color='gray', ha='center', va='center', alpha=0.5, rotation=35, transform=plt.gca().transAxes)
    plt.legend()
    plt.savefig(chart_name, bbox_inches='tight')
    plt.close()

def plot_bars(x, y, titles, ylabels, chart_name):   # Function for producing bar charts.
    fig, ax = plt.subplots(2, 2, figsize=(6, 6))

    ax[0,0].bar(x, y[0], color='green')
    ax[0,0].set_title(titles[0])
    ax[0,0].set_xlabel('Impact')
    ax[0,0].set_ylabel(ylabels[0])
    
    ax[0,1].bar(x, y[1], color='brown')
    ax[0,1].set_title(titles[1])
    ax[0,1].set_xlabel('Impact')
    ax[0,1].set_ylabel(ylabels[1])
    
    ax[1,0].bar(x, y[2], color='orange')
    ax[1,0].set_title(titles[2])
    ax[1,0].set_xlabel('Impact')
    ax[1,0].set_ylabel(ylabels[2])
    
    ax[1,1].bar(x, y[3], color='magenta')
    ax[1,1].set_title(titles[3])
    ax[1,1].set_xlabel('Impact')
    ax[1,1].set_ylabel(ylabels[3])
    # fig.text(0.5, 0.5, 'wkok6@gatech.edu', color='gray', fontsize=50, ha='center', va='center', alpha=0.5, rotation=35, transform=fig.transFigure)
    fig.suptitle('Effect of Impact on Various Trade and Performance Metrics', fontsize=13)
    plt.tight_layout()
    plt.savefig(chart_name, bbox_inches='tight')
    plt.close()

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
	  	   		 	 	 			  		 			     			  	 
def run_experiment(impact_values = [0,0,0,0]):  # Function for running experiment 2.

    impact_values = impact_values
    trades = []
    portvals = []
    metrics = []

    for v in impact_values:
        learner = sl.StrategyLearner(impact=v, commission=0)
        learner.add_evidence(symbol='JPM', sd = dt.datetime(2008, 1, 1), ed = dt.datetime(2009,12,31), sv=100000)
        df1 = learner.testPolicy(symbol='JPM', sd = dt.datetime(2008, 1, 1), ed = dt.datetime(2009,12,31), sv=100000)
        trades.append((df1.iloc[:,0]!=0).sum())
        df2 = msc.compute_portvals(df1, start_val = 100000, commission = 0, impact = v)
        df2 = df2/df2.iloc[0]
        portvals.append(df2)
        df3 = compute_metrics(df2)
        metrics.append(df3)
    
    results = pd.DataFrame(metrics, index=impact_values, 
                           columns=['Cumulative Return','Mean Daily Return','Std Dev of Daily Return','Final Value','Sharpe Ratio']).T
    results.to_csv('expt2_metrics.csv')

    metrics = np.array(metrics, dtype=float)
    adr = metrics[:,1]
    sddr = metrics[:,2]
    sharpe = metrics[:,-1]

    x = [str(i) for i in impact_values]
    y = [trades, adr, sddr, sharpe]
    titles = ['Total Trade Numbers','Average Daily Returns','Std Dev of Daily Return','Sharpe Ratios']
    ylabels = ['Total Trades','Average Daily Return','Std Dev of Daily Return','Sharpe']

    plot_lines(portvals, 'Effect of Impact on Portfolio Cumulative Return', 'Date', 'Normalized Price', [0.7,1.4], impact_values, 'expt2.1.png')
    plot_bars(x, y, titles, ylabels, 'expt2.2.png')
