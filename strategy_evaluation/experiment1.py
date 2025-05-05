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
import ManualStrategy as mstg
import StrategyLearner as sl
import marketsimcode as msc
import indicators as idr 	 			  		 			     			  	  	 	 			  		 			     			  	 

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

def plot_chart(x, y1, y2, y3, title, xlabel, ylabel, ylim, chart_name): # Function for producing charts.
    plt.plot(x, y1, color='red', linewidth=0.8)
    plt.plot(x, y2, color='blue', linewidth=0.8)
    plt.plot(x, y3, color='purple', linewidth=0.8)
    plt.title(title)
    plt.xlabel(xlabel) 
    plt.ylabel(ylabel)
    plt.ylim(ylim)
    plt.gca().xaxis.set_major_locator(md.MonthLocator(interval=2))
    plt.xticks(rotation=90)
    plt.grid(False)
    # plt.text(0.5, 0.5, 'wkok6@gatech.edu', fontsize=50, color='gray', ha='center', va='center', alpha=0.5, rotation=35, transform=plt.gca().transAxes)
    plt.legend(['Manual Strategy','Strategy Learner','Benchmark'])
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
	  	   		 	 	 			  		 			     			  	 
def run_experiment():   # Function for running experiment 1.
    
    ms = mstg.ManualStrategy(impact=0.005, commission=9.95)
    learner = sl.StrategyLearner(impact=0.005, commission=9.95)
    learner.add_evidence(symbol='JPM', sd = dt.datetime(2008, 1, 1), ed = dt.datetime(2009,12,31), sv=100000)
    
    trades_m_in = ms.testPolicy(symbol = "JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000)
    trades_m_out = ms.testPolicy(symbol = "JPM", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000)
    trades_sl_in = learner.testPolicy(symbol='JPM', sd = dt.datetime(2008, 1, 1), ed = dt.datetime(2009,12,31), sv=100000)
    trades_sl_out = learner.testPolicy(symbol='JPM', sd = dt.datetime(2010, 1, 1), ed = dt.datetime(2011,12,31), sv=100000)
    
    portvals_m_in = msc.compute_portvals(trades_m_in, start_val = 100000, commission = 9.95, impact = 0.005)
    portvals_m_out = msc.compute_portvals(trades_m_out, start_val = 100000, commission = 9.95, impact = 0.005)
    portvals_sl_in = msc.compute_portvals(trades_sl_in, start_val = 100000, commission = 9.95, impact = 0.005)
    portvals_sl_out = msc.compute_portvals(trades_sl_out, start_val = 100000, commission = 9.95, impact = 0.005)
    portvals_bmk_in = benchmark(symbol = "JPM", sd=trades_m_in.index[0], ed=trades_m_in.index[-1], sv = 100000, commission = 9.95, impact = 0.005)
    portvals_bmk_out = benchmark(symbol = "JPM", sd=trades_m_out.index[0], ed=trades_m_out.index[-1], sv = 100000, commission = 9.95, impact = 0.005)
    
    metrics_m_in = compute_metrics(portvals_m_in)
    metrics_m_out = compute_metrics(portvals_m_out)
    metrics_sl_in = compute_metrics(portvals_sl_in)
    metrics_sl_out = compute_metrics(portvals_sl_out)
    metrics_bmk_in = compute_metrics(portvals_bmk_in)
    metrics_bmk_out = compute_metrics(portvals_bmk_out)

    results = pd.DataFrame([metrics_m_in, metrics_sl_in, metrics_bmk_in, metrics_m_out, metrics_sl_out, metrics_bmk_out], 
                            index=['Manual Strategy (In-Sample)', 'Strategy Learner (In-Sample)', 'Benchmark (In-Sample)', 
                                    'Manual Strategy (Out-Sample)', 'Strategy Learner (Out-Sample)', 'Benchmark (Out-Sample)'], 
                            columns=['Cumulative Return','Mean Daily Return','Std Dev of Daily Return','Final Value','Sharpe Ratio']).T
    results.to_csv('expt1_metrics.csv')

    portvals_m_in = portvals_m_in/portvals_m_in.iloc[0]
    portvals_m_out = portvals_m_out/portvals_m_out.iloc[0]
    portvals_sl_in = portvals_sl_in/portvals_sl_in.iloc[0]
    portvals_sl_out = portvals_sl_out/portvals_sl_out.iloc[0]
    portvals_bmk_in = portvals_bmk_in/portvals_bmk_in.iloc[0]
    portvals_bmk_out = portvals_bmk_out/portvals_bmk_out.iloc[0]

    plot_chart(portvals_m_in.index, portvals_m_in.values, portvals_sl_in.values, portvals_bmk_in.values, 
               'Manual Rule-Based vs ML-Based Strategies (In-Sample)', 'Date', 'Normalized Price', [0.6,1.5],'expt1.1.png')
    plot_chart(portvals_m_out.index, portvals_m_out.values, portvals_sl_out.values, portvals_bmk_out.values, 
               'Manual Rule-Based vs ML-Based Strategies (Out-Sample)', 'Date', 'Normalized Price', [0.8,1.2],'expt1.2.png')
   