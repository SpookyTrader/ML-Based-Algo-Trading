""""""  		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
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
import random  		  	   		 	 	 			  		 			     			  	 
import numpy as np		  	   		 	 	 			  		 			     			  	 
import pandas as pd  		  	   		 	 	 			  		 			     			  	 
from util import get_data  		  	   		 	 	 			  		 			     			  	 
import indicators as idr
import RTLearner as rt 	  
import BagLearner as bl	  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
class StrategyLearner(object):  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    A strategy learner that can learn a trading policy using the same indicators used in ManualStrategy.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
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
        self.learner = bl.BagLearner(rt.RTLearner, {'leaf_size':17}, bags=30)  		  	   		 	 	 			  		 			     			  	 

# Function for getting multiple columns of stock data, such as High, Low etc. It wraps the get_data function from util.py in it.
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
        """  		  	   		 	 	 			  		 			     			  	 
        Trains your strategy learner over a given time frame.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
        :param symbol: The stock symbol to train on  		  	   		 	 	 			  		 			     			  	 
        :type symbol: str  		  	   		 	 	 			  		 			     			  	 
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	 	 			  		 			     			  	 
        :type sd: datetime  		  	   		 	 	 			  		 			     			  	 
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	 	 			  		 			     			  	 
        :type ed: datetime  		  	   		 	 	 			  		 			     			  	 
        :param sv: The starting value of the portfolio  		  	   		 	 	 			  		 			     			  	 
        :type sv: int  		  	   		 	 	 			  		 			     			  	 
        """

        prices = self.__get_stocks_data(symbol=symbol, sd = sd, ed = ed)
        pr_sma = idr.price_sma(prices_df=prices)
        boll = idr.percent_B(prices_df=prices)
        ppo = idr.percentage_price_osc(prices_df=prices)

        df = pd.concat([prices, pr_sma, boll, ppo], axis=1)
        df.dropna(inplace=True)
        df['Class'] = 0

        df['Adj Close'] = df['Adj Close'].pct_change(self.N)
        df['Adj Close'] = df['Adj Close'].shift(-self.N)
        df.dropna(inplace=True)
        df['Class'] = df['Adj Close'].apply(lambda x: 1 if x>(2*self.impact) else (-1 if x<-(2*self.impact) else 0))

        train_x = np.array(df.drop("Adj Close", axis=1).iloc[:,:-1])
        train_y = np.array(df.drop("Adj Close", axis=1).iloc[:,-1])

        self.learner.add_evidence(train_x, train_y)

        return	 			     			  	 
         		  		 			     			  	 	  	   		 	 	 			  		 			     			  	 
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

        test_x = np.array(df.drop("Adj Close", axis=1))
        
        pred_y = self.learner.query(test_x)

        df['Predicted'] = pred_y.astype(int)
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
        return "wkok6"  		  	   		 	 	 			  		 			     			  	 

    def study_group(self):
        """
        :return: A comma separated string of GT_Name of each member of your study group.
        # Example: "gburdell3, jdoe77, tbalch7" or "gburdell3" if a single individual working alone.
        :rtype: str
        """
        return "wkok6" 

# if __name__ == "__main__":  		  	   		 	 	 			  		 			     			  	 
#     print("One does not simply think up a strategy")  		  	   		 	 	 			  		 			     			  	 
