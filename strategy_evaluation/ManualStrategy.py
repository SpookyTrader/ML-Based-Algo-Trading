""""""  		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	   	   		 	 	 			  		 			     			  	 	  	   		 	 	 			  		 			     			  	 
Student Name: Wai Kay Kok (replace with your name)  		  	   		 	 	 			  		 			     			  	 
GT User ID: wkok6 (replace with your User ID)  		  	   		 	 	 			  		 			     			  	 
GT ID: 904075476 (replace with your GT ID)   		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
import datetime as dt  		  	   		 	 	 			  		 			     			  	 
import random  		  	   		 	 	 			  		 			     			  	 
import numpy as np		  	   		 	 	 			  		 			     			  	 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as md  		  	   		 	 	 			  		 			     			  	 
from util import get_data  		  	   		 	 	 			  		 			     			  	 
import indicators as idr	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
class ManualStrategy(object):  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    A Manual Strategy based on human-devised rules from technical indicators.  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		 	 	 			  		 			     			  	 
        If verbose = False your code should not generate ANY output.  		  	   		 	 	 			  		 			     			  	 
    :type verbose: bool  		  	   		 	 	 			  		 			     			  	 
    :param impact: The market impact of each transaction, defaults to 0.0  		  	   		 	 	 			  		 			     			  	 
    :type impact: float  		  	   		 	 	 			  		 			     			  	 
    :param commission: The commission amount charged, defaults to 0.0  		  	   		 	 	 			  		 			     			  	 
    :type commission: float  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 

    def __init__(self, verbose=False, impact=0.0, commission=0.0):  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        Constructor method  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        self.verbose = verbose  		  	   		 	 	 			  		 			     			  	 
        self.impact = impact  		  	   		 	 	 			  		 			     			  	 
        self.commission = commission
        self.N = 31	   		 	 	 			  		 			     			  	 

# Function that get multiple columns of stock data, such as High, Low etc. It wraps the get_data from util.py in it.
    def __get_stocks_data(self, symbol='JPM', sd = dt.datetime(2008, 1, 1), ed = dt.datetime(2009,12,31), cols="Adj Close"):
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
    
    def __positioning(self, df, N): # Function that determines position sizing.
        trade_idx = []
        for i in range(df.shape[0]):
            position = df.loc[:df.index[i],'Trade'].cumsum().iloc[-1]
            if df.loc[df.index[i],'Predicted'] == 1:
                if position > 0:
                    continue
                elif position < 0:
                    if i >= trade_idx[0] + N:
                        df.loc[df.index[i],'Trade'] = 2000
                        trade_idx.pop(0)
                        trade_idx.append(i)
                else:
                    df.loc[df.index[i],'Trade'] = 1000
                    trade_idx.append(i)
            
            elif df.loc[df.index[i],'Predicted'] == -1:
                if position < 0:
                    continue
                elif position > 0:
                    if i >= trade_idx[0] + N:
                        df.loc[df.index[i],'Trade'] = -2000
                        trade_idx.pop(0)
                        trade_idx.append(i)
                else:
                    df.loc[df.index[i],'Trade'] = -1000
                    trade_idx.append(i)
        
        trades = df[['Trade']].copy()
        return trades

    def add_evidence(  		  	   		 	 	 			  		 			     			  	 
        self,  		  	   		 	 	 			  		 			     			  	 
        symbol="IBM",  		  	   		 	 	 			  		 			     			  	 
        sd=dt.datetime(2008, 1, 1),  		  	   		 	 	 			  		 			     			  	 
        ed=dt.datetime(2009, 1, 1),  		  	   		 	 	 			  		 			     			  	 
        sv=100000,  		  	   		 	 	 			  		 			     			  	 
    ):  		  	   		 	 	 			  		 			     			  	 
        pass	 			     			  	 
         		  		 			     			  	 	  	   		 	 	 			  		 			     			  	 
    def testPolicy(  		  	   		 	 	 			  		 			     			  	 
        self,  		  	   		 	 	 			  		 			     			  	 
        symbol="IBM",  		  	   		 	 	 			  		 			     			  	 
        sd=dt.datetime(2009, 1, 1),  		  	   		 	 	 			  		 			     			  	 
        ed=dt.datetime(2010, 1, 1),  		  	   		 	 	 			  		 			     			  	 
        sv=100000,  		  	   		 	 	 			  		 			     			  	 
    ):  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        Tests your learner using data outside of the training data  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
        :param symbol: The stock symbol that you trained on on  		  	   		 	 	 			  		 			     			  	 
        :type symbol: str  		  	   		 	 	 			  		 			     			  	 
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	 	 			  		 			     			  	 
        :type sd: datetime  		  	   		 	 	 			  		 			     			  	 
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	 	 			  		 			     			  	 
        :type ed: datetime  		  	   		 	 	 			  		 			     			  	 
        :param sv: The starting value of the portfolio  		  	   		 	 	 			  		 			     			  	 
        :type sv: int  		  	   		 	 	 			  		 			     			  	 
        :return: A DataFrame with values representing trades for each day. Legal values are +1000.0 indicating  		  	   		 	 	 			  		 			     			  	 
            a BUY of 1000 shares, -1000.0 indicating a SELL of 1000 shares, and 0.0 indicating NOTHING.  		  	   		 	 	 			  		 			     			  	 
            Values of +2000 and -2000 for trades are also legal when switching from long to short or short to  		  	   		 	 	 			  		 			     			  	 
            long so long as net holdings are constrained to -1000, 0, and 1000.  		  	   		 	 	 			  		 			     			  	 
        :rtype: pandas.DataFrame  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 

        prices = self.__get_stocks_data(symbol=symbol, sd = sd, ed = ed)
        pr_sma = idr.price_sma(prices_df=prices)
        boll = idr.percent_B(prices_df=prices)
        ppo = idr.percentage_price_osc(prices_df=prices)

        df = pd.concat([prices, pr_sma, boll, ppo], axis=1)
        df.dropna(inplace=True)
        df['Predicted'] = 0

        for d in df.index:  # Trading rules of the Manual Strategy using 3 indicators in combination.
            if df.loc[d,'%price_osc'] < 0:
                if (df.loc[d,'Price-SMA Ratio'] <= 0.90) and (df.loc[d,'%B'] <= 10):
                    df.loc[d,'Predicted'] = 1
                elif (df.loc[d,'Price-SMA Ratio'] > 1.02)  and (df.loc[d,'%B'] >= 50):
                    df.loc[d,'Predicted'] = -1
            elif df.loc[d,'%price_osc'] > 0:
                if (df.loc[d,'Price-SMA Ratio'] >= 1.1) and (df.loc[d,'%B'] >= 90):
                    df.loc[d,'Predicted'] = -1
                elif (df.loc[d,'Price-SMA Ratio'] < 0.98) and (df.loc[d,'%B'] <= 50):
                    df.loc[d,'Predicted'] = 1
        
        df['Trade'] = 0
        trades = self.__positioning(df, self.N)
        trades.columns = [symbol]
        trades = trades.shift(1)
        trades.dropna(inplace=True)
 	 			  		 			     			  	 
        if self.verbose:
            print(type(trades))  		  	   		 	 	 			  		 			     			  	 
            print(trades)  		  	   		 	 	 			  		 			     			  	  		  	   		 	 	 			  		 			     			  	 
            print(prices)  		  	   		 	 	 			  		 			     			  	 
        
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

# if __name__ == "__main__":  		  	   		 	 	 			  		 			     			  	 
#     print("One does not simply think up a strategy") 

# This function generate chart for the Manual Strategy. It is NOT part of the Manual Strategy class object.	 	 			  		 			     			  	 
def plot_chart(x, y1, y2, long, short, title, xlabel, ylabel, ylim, chart_name): # Function for plotting chart (used only for TOS part). 
    plt.plot(x, y1, color='red', linewidth=0.8, label='Manual Strategy')
    plt.plot(x, y2, color='purple', linewidth=0.8, label='Benchmark')
    plt.axvline(x=long[0], color='blue', linewidth=0.5, label='Long')
    for l in long[1:]:
        plt.axvline(x=l, color='blue', linewidth=0.5)
    plt.axvline(x=short[0], color='black', linewidth=0.5, label='Short')
    for s in short[1:]:
        plt.axvline(x=s, color='black', linewidth=0.5)
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
