""""""  		  	   		 	 	 			  		 			     			  	 
"""Assess a betting strategy.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
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
  		  	   		 	 	 			  		 			     			  	 
Student Name: Wai Kay Kok  		  	   		 	 	 			  		 			     			  	 
GT User ID: wkok6  		  	   		 	 	 			  		 			     			  	 
GT ID: 904075476		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker 		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def author():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    :return: The GT username of the student  		  	   		 	 	 			  		 			     			  	 
    :rtype: str  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    return "wkok6"  # replace tb34 with your Georgia Tech username.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def study_group():
    """
    :return: A comma separated string of GT_Name of each member of your study group. 
    # Example: "gburdell3, jdoe77, tbalch7" or "gburdell3" if a single individual working alone.
    :rtype: str
    """
    return "wkok6"


def gtid():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    :return: The GT ID of the student  		  	   		 	 	 			  		 			     			  	 
    :rtype: int  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    return 904075476  # replace with your GT ID number  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def get_spin_result(win_prob):  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
    :param win_prob: The probability of winning  		  	   		 	 	 			  		 			     			  	 
    :type win_prob: float  		  	   		 	 	 			  		 			     			  	 
    :return: The result of the spin.  		  	   		 	 	 			  		 			     			  	 
    :rtype: bool  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    result = False  		  	   		 	 	 			  		 			     			  	 
    if np.random.random() <= win_prob:  		  	   		 	 	 			  		 			     			  	 
        result = True  		  	   		 	 	 			  		 			     			  	 
    return result  		  	   		 	 	 			  		 			     			  	 

def experiment1(win_prob):
    winnings = np.zeros((1000,1001)) # Array for storing results of experiment.   
    for epi in range(0,1000):
        episode_winnings = 0
        spin = 1
        while episode_winnings < 80:
            won = False
            bet_amount = 1
            while not won:
                won = get_spin_result(win_prob)
                if won == True:
                    episode_winnings = episode_winnings + bet_amount
                else:
                    episode_winnings = episode_winnings - bet_amount
                    bet_amount = bet_amount * 2
                winnings[epi,spin] = episode_winnings
                spin+=1
        winnings[epi, spin:] = episode_winnings

# Convert array to dataframe and compute mean, median, standard deviation, upper and lower bounds.        
    winnings = pd.DataFrame(winnings, index=[f'Episode {i+1}' for i in range(1000)])
    winnings = winnings.T
    winnings['Mean'] = winnings.mean(axis=1)
    winnings['StdDev'] = winnings.iloc[:,:-1].std(axis=1)
    winnings['Mean+1SD'] = winnings['Mean'] + winnings['StdDev']
    winnings['Mean-1SD'] = winnings['Mean'] - winnings['StdDev']
    winnings['Median'] = winnings.iloc[:,:-4].median(axis=1)
    winnings['Median+1SD'] = winnings['Median'] + winnings['StdDev']
    winnings['Median-1SD'] = winnings['Median'] - winnings['StdDev']

    winnings.to_csv('Expt1_Winnings.csv', index=False)
    
    return winnings

def experiment2(win_prob):
    winnings = np.zeros((1000,1001)) # Array for storing results of experiment.
    for epi in range(0,1000):
        episode_winnings = 0
        spin = 1
        while -256 < episode_winnings < 80:
            won = False
            bet_amount = 1
            while not won:
                won = get_spin_result(win_prob)
                if won == True:
                    episode_winnings += bet_amount
                else:
                    episode_winnings -= bet_amount
                    if (episode_winnings+256) > 0:
                        bet_amount = min(bet_amount*2, episode_winnings+256)
                    else:
                        winnings[epi,spin] = episode_winnings
                        break
                winnings[epi,spin] = episode_winnings
                spin+=1
        winnings[epi, spin:] = episode_winnings
 
# Convert array to dataframe and compute mean, median, standard deviation, upper and lower bounds  
    winnings = pd.DataFrame(winnings, index=[f'Episode {i+1}' for i in range(1000)])
    winnings = winnings.T
    winnings['Mean'] = winnings.mean(axis=1)
    winnings['StdDev'] = winnings.iloc[:,:-1].std(axis=1)
    winnings['Mean+1SD'] = winnings['Mean'] + winnings['StdDev']
    winnings['Mean-1SD'] = winnings['Mean'] - winnings['StdDev']
    winnings['Median'] = winnings.iloc[:,:-4].median(axis=1)
    winnings['Median+1SD'] = winnings['Median'] + winnings['StdDev']
    winnings['Median-1SD'] = winnings['Median'] - winnings['StdDev']

    winnings.to_csv('Expt2_Winnings.csv', index=False)
    
    return winnings

def plot_chart(data, title, y_label):
    ax = data.plot(fontsize=18, figsize=(20,10))
    ax.set_title(title, fontsize=20)
    ax.set_xlabel('Spin', fontsize=20)
    ax.set_ylabel(y_label, fontsize=20)
    ax.set_xlim([0,300])
    ax.set_ylim([-256,100])
    ax.xaxis.set_major_locator(ticker.MultipleLocator(base=10)) 
    ax.yaxis.set_major_locator(ticker.MultipleLocator(base=10))
    plt.legend(fontsize = 18)
    plt.savefig(title[:5]+'.png')
    plt.close()

    return None
  		  	   		 	 	 			  		 			     			  	 
def test_code():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    Method to test your code  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    win_prob = 0.4737 # Winning probability of an American roulette wheel with '0' and '00', total 38 slots.
    np.random.seed(gtid())
    expt1 = experiment1(win_prob)
    expt2 = experiment2(win_prob)
    plot_chart(expt1.iloc[:,:10], 'Fig 1: Cumulative Winnings for 10 Episodes.', 'Winnings($)')
    plot_chart(expt1.loc[:,['Mean','Mean+1SD','Mean-1SD']], 'Fig 2: Average and Variability of Winning in Each Spin.', 'Winnings($)')
    plot_chart(expt1.loc[:,['Median','Median+1SD','Median-1SD']], 'Fig 3: Median and Variability of Winning in Each Spin.', 'Winnings($)')
    plot_chart(expt2.loc[:,['Mean','Mean+1SD','Mean-1SD']], 'Fig 4: Average and Variability of Winning in Each Spin (with Limited Money).', 'Winnings($)')
    plot_chart(expt2.loc[:,['Median','Median+1SD','Median-1SD']], 'Fig 5: Median and Variability of Winning in Each Spin (with Limited Money).', 'Winnings($)')

    return None		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
if __name__ == "__main__":  		  	   		 	 	 			  		 			     			  	 
    test_code()  		  	   		 	 	 			  		 			     			  	 
