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
  		  	   		 	 	 			  		 			     			  	 
def momentum(prices_df, symbol='JPM', period=10, chart=False):
    momentum = prices_df.copy()
    momentum['Momentum'] = prices_df.pct_change(10)*100

    if chart:
        fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, gridspec_kw={'height_ratios': [2, 1]}, figsize=(10, 8))
        ax[0].plot(momentum.index, momentum['Adj Close'].values, label=symbol+' (Adj Close)', color='blue', linewidth=0.8)
        ax[0].set_ylabel('Price($)')
        ax[0].legend()
        ax[1].plot(momentum.index, momentum['Momentum'], label='Momentum', color='green', linewidth=0.8)
        ax[1].fill_between(momentum.index, momentum['Momentum'].values, 0, where=(momentum['Momentum'].values > 0),
                           color='green', alpha=0.7, label='Momentum > 0')
        ax[1].fill_between(momentum.index, momentum['Momentum'].values, 0, where=(momentum['Momentum'].values < 0),
                           color='pink', alpha=0.7, label='Momentum < 0')
        ax[1].axhline(y=0, color='black', linewidth=0.5)
        ax[1].set_xlabel('Date')
        ax[1].xaxis.set_major_locator(md.MonthLocator(interval=2))
        ax[1].set_ylim([-90,90])
        ax[1].set_ylabel('Momentum(%)')
        ax[1].legend()

        intersect1 = momentum[(momentum['Momentum'] > 0) & (momentum['Momentum'].shift(1) <= 0)]
        intersect2 = momentum[(momentum['Momentum'] < 0) & (momentum['Momentum'].shift(1) >= 0)]
        for i in intersect1.index:
            ax[0].annotate(' ', xy =(i,momentum.loc[i,'Adj Close']), xytext=(i,momentum.loc[i,'Adj Close']),
                           arrowprops = dict(facecolor='green', edgecolor='none', headwidth=7, headlength=7))
        for i in intersect2.index:
            ax[0].annotate(' ', xy =(i,momentum.loc[i,'Adj Close']), xytext=(i,momentum.loc[i,'Adj Close']),
                           arrowprops = dict(facecolor='red', edgecolor='none', headwidth=7, headlength=7))
        
        fig.suptitle('Price Action and Momentum Indicator', size=13)
        plt.xticks(rotation=45)
        plt.tight_layout()
        # fig.text(0.5, 0.5, 'wkok6@gatech.edu', color='gray', fontsize=80, ha='center', va='center', alpha=0.5, rotation=35, transform=fig.transFigure)
        plt.savefig('momentum.png')
        plt.close()

    return momentum['Momentum'].values

def commodity_channel(prices_df, symbol='JPM', period=20, constant=0.015, chart=False):
    cci = prices_df.copy()
    cci['Adj High'] = cci['High'] * cci['Adj Close'] / cci['Close']
    cci['Adj Low'] = cci['Low'] * cci['Adj Close'] / cci['Close']
    cci['Average Price'] = (cci['Adj High'] + cci['Adj Low'] + cci['Adj Close']) / 3
    cci['SMA'] = cci['Average Price'].rolling(window=period).mean()
    cci['Mean Deviation'] = cci['Average Price'].rolling(window=period).apply(lambda x: np.mean(np.abs(x - np.mean(x))))
    cci['CCI'] = (cci['Average Price'] - cci['SMA']) / (constant * cci['Mean Deviation'])

    if chart:
        fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, gridspec_kw={'height_ratios': [2, 1]}, figsize=(10, 8))
        ax[0].plot(cci.index, cci['Adj Close'], label=symbol+' (Adj Close)', color='blue', linewidth=0.8)
        ax[0].set_ylabel('Price($)')
        ax[0].legend()
        ax[1].plot(cci.index, cci['CCI'].values, label='Commodity Channel Index', color='green', linewidth=0.8)
        ax[1].axhline(y=0, color='black', linewidth=0.5)
        ax[1].axhline(y=100, color='red', linewidth=0.5)
        ax[1].axhline(y=-100, color='red', linewidth=0.5)
        ax[1].fill_between(cci.index, cci['CCI'].values, 100, where=(cci['CCI'].values > 100),
                           color='green', alpha=0.7, label='Overbought')
        ax[1].fill_between(cci.index, cci['CCI'].values, -100, where=(cci['CCI'].values < -100),
                           color='pink', alpha=1, label='Oversold')
        ax[1].set_xlabel('Date')
        ax[1].xaxis.set_major_locator(md.MonthLocator(interval=2))
        ax[1].set_ylim([-500,500])
        ax[1].set_ylabel('CCI')
        ax[1].legend(fontsize=10)
        fig.suptitle('Price Action and Commodity Channel Index', size=13)
        plt.xticks(rotation=45)
        plt.tight_layout()
        # fig.text(0.5, 0.5, 'wkok6@gatech.edu', color='gray', fontsize=80, ha='center', va='center', alpha=0.5, rotation=35, transform=fig.transFigure)
        plt.savefig('cci.png')
        plt.close()
    
    return cci['CCI'].values

def percent_B(prices_df, symbol='JPM', period=20, std_dev=2, chart=False):
    pB = prices_df.copy()
    pB['SMA'] = pB["Adj Close"].rolling(window=period).mean()
    pB['MStd_Dev'] = pB["Adj Close"].rolling(window=period).std()
    pB['Upper Band'] = pB['SMA'] + (pB['MStd_Dev'] * std_dev)
    pB['Lower Band'] = pB['SMA'] - (pB['MStd_Dev'] * std_dev)
    pB['%B'] = (pB["Adj Close"] - pB['Lower Band']) / (pB['Upper Band'] - pB['Lower Band']) * 100

    if chart:
        fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, gridspec_kw={'height_ratios': [2, 1]}, figsize=(10, 8))
        ax[0].plot(pB.index, pB['Adj Close'].values, label=symbol+' (Adj Close)', color='blue', linewidth=0.8)
        ax[0].plot(pB.index, pB['SMA'].values, label='SMA', color='red', linestyle='--', linewidth=0.8)
        ax[0].plot(pB.index, pB['Upper Band'].values, label='Upper Band', color='brown', linewidth=0.8)
        ax[0].plot(pB.index, pB['Lower Band'].values, label='Lower Band', color='purple', linewidth=0.8)
        ax[0].set_ylabel('Price($)')
        ax[0].legend()
        ax[1].plot(pB.index, pB['%B'].values, label='%B', color='green', linewidth=0.8)
        ax[1].axhline(y=0, color='purple', linewidth=0.8)
        ax[1].axhline(y=50, color='red', linestyle='--', linewidth=0.8)
        ax[1].axhline(y=100, color='brown', linewidth=0.8)
        ax[1].fill_between(pB.index, pB['%B'].values, 100, where=(pB['%B'].values > 100),
                           color='green', alpha=0.7, label='Overbought')
        ax[1].fill_between(pB.index, pB['%B'].values, 0, where=(pB['%B'].values < 0),
                           color='pink', alpha=1, label='Oversold')
        ax[1].set_xlabel('Date')
        ax[1].xaxis.set_major_locator(md.MonthLocator(interval=2))
        ax[1].set_ylim([-50,200])
        ax[1].set_ylabel('%B')
        ax[1].legend(fontsize=10)
        fig.suptitle('Stock Price and %B Indicator', size=13)
        plt.xticks(rotation=45)
        plt.tight_layout()
        # fig.text(0.5, 0.5, 'wkok6@gatech.edu', color='gray', fontsize=80, ha='center', va='center', alpha=0.5, rotation=35, transform=fig.transFigure)
        plt.savefig('%B.png')
        plt.close()
    
    return pB['%B'].values

def percentage_price_osc(prices_df, symbol='JPM', period1=12, period2=26, chart=False):
    ppo = prices_df.copy()
    ppo['ema1'] = ppo["Adj Close"].ewm(span=period1, adjust=False).mean()
    ppo['ema2'] = ppo["Adj Close"].ewm(span=period2, adjust=False).mean()
    ppo['%price_osc'] = ((ppo['ema1']-ppo['ema2'])/ppo['ema2'])*100

    if chart:
        fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, gridspec_kw={'height_ratios': [2, 1]}, figsize=(10, 8))
        ax[0].plot(ppo.index, ppo["Adj Close"].values, label=symbol+" (Adj Close)", color='blue', linewidth=0.8)
        ax[0].set_ylabel('Price($)')
        ax[0].legend()
        ax[1].plot(ppo.index, ppo['%price_osc'], label='Percentage Price Oscillator', color='green', linewidth=0.8)
        ax[1].axhline(y=0, color='black', linewidth=0.5)
        ax[1].fill_between(ppo.index, ppo['%price_osc'].values, 0, where=(ppo['%price_osc'].values > 0),
                           color='green', alpha=0.7, label='Fast EMA/Slow EMA > 0')
        ax[1].fill_between(ppo.index, ppo['%price_osc'].values, 0, where=(ppo['%price_osc'].values < 0),
                           color='pink', alpha=0.7, label='Fast EMA/Slow EMA < 0')
        ax[1].set_xlabel('Date')
        ax[1].set_ylim([-10,10])
        ax[1].xaxis.set_major_locator(md.MonthLocator(interval=2))
        ax[1].set_ylabel('Percentage Price Oscillator(%)')
        ax[1].legend()

        intersect1 = ppo[(ppo['%price_osc'] > 0) & (ppo['%price_osc'].shift(1) <= 0)]
        intersect2 = ppo[(ppo['%price_osc'] < 0) & (ppo['%price_osc'].shift(1) >= 0)]
        for i in intersect1.index:
            ax[0].annotate(' ', xy =(i,ppo.loc[i,'Adj Close']), xytext=(i,ppo.loc[i,'Adj Close']), 
                           arrowprops = dict(facecolor='green', edgecolor='none', headwidth=7, headlength=7))
        for i in intersect2.index:
            ax[0].annotate(' ', xy =(i,ppo.loc[i,'Adj Close']), xytext=(i,ppo.loc[i,'Adj Close']), 
                           arrowprops = dict(facecolor='red', edgecolor='none', headwidth=7, headlength=7))
        
        fig.suptitle('Price Action and Percentage Price Oscillator', size=13)
        plt.xticks(rotation=45)
        plt.tight_layout()
        # fig.text(0.5, 0.5, 'wkok6@gatech.edu', color='gray', fontsize=80, ha='center', va='center', alpha=0.5, rotation=35, transform=fig.transFigure)
        plt.savefig('percentage-price.png')
        plt.close()

    return ppo['%price_osc'].values

def price_sma(prices_df, symbol='JPM', period=20, chart=False):
    pr_sma = prices_df.copy()
    pr_sma['SMA'] = pr_sma["Adj Close"].rolling(window=period).mean()
    pr_sma['Price-SMA Ratio'] = pr_sma['Adj Close'] / pr_sma['SMA']

    if chart:
        fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, gridspec_kw={'height_ratios': [2, 1]}, figsize=(10, 8))
        ax[0].plot(pr_sma.index, pr_sma['Adj Close'].values, label=symbol+' (Adj Close)', color='blue', linewidth=0.8)
        ax[0].plot(pr_sma.index, pr_sma['SMA'].values, label=str(period)+' SMA', color='red', linewidth=0.8)
        ax[0].set_ylabel('Price($)')
        ax[0].legend()
        ax[1].plot(pr_sma.index,  pr_sma['Price-SMA Ratio'].values, label='Price-SMA Ratio', color='blue', linewidth=0.8)
        ax[1].fill_between(pr_sma.index, pr_sma['Price-SMA Ratio'].values, 1, where=(pr_sma['Price-SMA Ratio'].values > 1),
                           color='green', alpha=0.7, label='Above SMA')
        ax[1].fill_between(pr_sma.index, pr_sma['Price-SMA Ratio'].values, 1, where=(pr_sma['Price-SMA Ratio'].values < 1), 
                           color='pink', alpha=0.7, label='Below SMA')
        ax[1].axhline(y=1, color='black', linewidth=0.5)
        ax[1].set_xlabel('Date')
        ax[1].xaxis.set_major_locator(md.MonthLocator(interval=2))
        # ax[1].set_ylim([-0.5,1.5])
        ax[1].set_ylabel('Price-SMA Ratio')
        ax[1].legend()

        intersect1 = pr_sma[(pr_sma['Adj Close'] > pr_sma['SMA']) & (pr_sma['Adj Close'].shift(1) <= pr_sma['SMA'].shift(1))]
        intersect2 = pr_sma[(pr_sma['Adj Close'] < pr_sma['SMA']) & (pr_sma['Adj Close'].shift(1) >= pr_sma['SMA'].shift(1))]
        for i in intersect1.index:
            ax[0].annotate(' ', xy =(i,pr_sma.loc[i,'SMA']), xytext=(i,pr_sma.loc[i,'SMA']),
                           arrowprops = dict(facecolor='green', edgecolor='none', headwidth=6, headlength=6))
        for i in intersect2.index:
            ax[0].annotate(' ', xy =(i,pr_sma.loc[i,'SMA']), xytext=(i,pr_sma.loc[i,'SMA']),
                           arrowprops = dict(facecolor='red', edgecolor='none', headwidth=6, headlength=6))
        
        fig.suptitle('Price Action & Price-SMA Ratio Indicator', size=13)
        plt.xticks(rotation=45)
        plt.tight_layout()
        # fig.text(0.5, 0.5, 'wkok6@gatech.edu', color='gray', fontsize=80, ha='center', va='center', alpha=0.5, rotation=35, transform=fig.transFigure)
        plt.savefig('price-sma.png')
        plt.close()
    
    return pr_sma['Price-SMA Ratio'].values
  		  	   		 	 	 			  		 			     			  	 
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
	  	   		 	 	 			  		 			     			  	 
