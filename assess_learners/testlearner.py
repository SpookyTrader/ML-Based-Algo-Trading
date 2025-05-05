""""""  		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 
Test a learner.  (c) 2015 Tucker Balch  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
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
"""  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
import math  		  	   		 	 	 			  		 			     			  	 
import sys
import time	  	   		 	 	 			  		 			     			  	 		  	   		 	 	 			  		 			     			  	 
import numpy as np
import matplotlib.pyplot as plt		  	   		 	 	 			  		 			     			  	   	   		 	 	 			  		 			     			  	 
import DTLearner as dt
import RTLearner as rt 	  
import BagLearner as bl
import InsaneLearner as it 
import LinRegLearner as lr	 			  		 			     			  	 

def gtid():
    return 904075476 

def train_test_split(data, train_size):
    train_rows = int(train_size * data.shape[0])
    idx = np.random.permutation(data.shape[0])
    train = data[idx[:train_rows],:]
    test = data[idx[train_rows:],:]
    train_x = train[:,:-1]
    train_y = train[:,-1]
    test_x = test[:,:-1]
    test_y = test[:,-1]
    return train_x, train_y, test_x, test_y

def experiment1(data, train_size, leafs):
    rmse_in = np.zeros((10,50))
    rmse_out = np.zeros((10,50))
    for r in range(10):
        train_x, train_y, test_x, test_y = train_test_split(data, 0.6)
        for i in leafs:
            learner = dt.DTLearner(leaf_size = i, verbose = False)
            learner.add_evidence(train_x, train_y)
            pred_y = learner.query(train_x)
            rmse_in[r,i-1] = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
            pred_y = learner.query(test_x)
            rmse_out[r,i-1] = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])

    rmse_in = np.append(rmse_in, np.mean(rmse_in, axis=0).reshape(1,-1), axis=0)
    rmse_out = np.append(rmse_out, np.mean(rmse_out, axis=0).reshape(1,-1), axis=0)
    return rmse_in, rmse_out

def experiment2(data, train_size, leafs):
    rmse_in = np.zeros((10,50))
    rmse_out = np.zeros((10,50))
    for r in range(10):
        train_x, train_y, test_x, test_y = train_test_split(data, 0.6)
        for i in range(leafs.shape[0]):
            learner = bl.BagLearner(dt.DTLearner, {'leaf_size':i}, bags=20)
            learner.add_evidence(train_x, train_y)
            pred_y = learner.query(train_x)
            rmse_in[r,i] = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
            pred_y = learner.query(test_x)
            rmse_out[r,i] = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
    
    rmse_in = np.append(rmse_in, np.mean(rmse_in, axis=0).reshape(1,-1), axis=0)
    rmse_out = np.append(rmse_out, np.mean(rmse_out, axis=0).reshape(1,-1), axis=0)
    return rmse_in, rmse_out

def experiment3(data, train_size, leafs):
    mae_dt = np.zeros((10,50))
    mae_rt = np.zeros((10,50))
    
    for r in range(10):
        train_x, train_y, test_x, test_y = train_test_split(data, 0.6)
        for i in leafs:
            learner = dt.DTLearner(leaf_size = i, verbose = False)
            learner.add_evidence(train_x, train_y)
            pred_y = learner.query(test_x)
            mae_dt[r,i-1] = np.mean(np.abs(test_y - pred_y))

            learner = rt.RTLearner(leaf_size = i, verbose = False)
            learner.add_evidence(train_x, train_y)
            pred_y = learner.query(test_x)
            mae_rt[r,i-1] = np.mean(np.abs(test_y - pred_y))

    mae_dt = np.append(mae_dt, np.mean(mae_dt, axis=0).reshape(1,-1), axis=0)
    mae_rt = np.append(mae_rt, np.mean(mae_rt, axis=0).reshape(1,-1), axis=0)

    time_dt = np.zeros((10,50))
    time_rt = np.zeros((10,50))

    for r in range(10):
        train_x, train_y, test_x, test_y = train_test_split(data, 0.6)
        for i in leafs:
            start = time.time()
            learner = dt.DTLearner(leaf_size=i, verbose=False)
            learner.add_evidence(train_x, train_y)
            end = time.time()
            time_dt[r,i-1] = end - start

            start = time.time()
            learner = rt.RTLearner(leaf_size=i, verbose=False)
            learner.add_evidence(train_x, train_y)
            end = time.time()
            time_rt[r,i-1] = end - start
            
    time_dt = np.append(time_dt, np.mean(time_dt, axis=0).reshape(1,-1), axis=0)
    time_rt = np.append(time_rt, np.mean(time_rt, axis=0).reshape(1,-1), axis=0)

    return mae_dt, mae_rt, time_dt, time_rt

def plot_chart(x, y1, y2, title, xlabel, ylabel, ylim, color1, color2, legend1, legend2, chart_name):
    plt.plot(x, y1, color=color1, label=legend1)
    plt.plot(x, y2, color=color2, label=legend2)
    plt.title(title)
    plt.xlabel(xlabel) 
    plt.ylabel(ylabel)
    plt.ylim(ylim)
    # plt.gca().invert_xaxis()
    # plt.text(0.5, 0.5, 'wkok6@gatech.edu', fontsize=40, color='gray', ha='center', va='center', alpha=0.5, rotation=35, transform=plt.gca().transAxes)
    plt.legend()
    plt.savefig(chart_name)
    plt.close()

if __name__ == "__main__":  		  	   		 	 	 			  		 			     			  	 
    if len(sys.argv) != 2:  		  	   		 	 	 			  		 			     			  	 
        print("Usage: python testlearner.py <filename>")  		  	   		 	 	 			  		 			     			  	 
        sys.exit(1)
    if sys.argv[1] == "Data/Istanbul.csv":  	   		 	 	 			  		 			     			  	 
        inf = open(sys.argv[1])  	# Read file that needs skipping header and 1st column.		  		 			     			  	 
        data = np.array([list(map(float, s.strip().split(",")[1:])) for s in inf.readlines()[1:]]) # Skip 1st column and row.
    else:
        inf = open(sys.argv[1]) # Read file that doesn't need to skip header and 1st column.
        data = np.array([list(map(float, s.strip().split(","))) for s in inf.readlines()])  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
    np.random.seed(gtid())
    
    # Experiment 1:
    leafs = np.arange(1,51)
    rmse_in_dt, rmse_out_dt = experiment1(data, 0.6, leafs)
    
    # Chart
    plot_chart(leafs, 
               rmse_in_dt[10,:], 
               rmse_out_dt[10,:], 
               "Effect of Leaf Size on Overfitting", 
               "Leaf Size", 
               "Average RMSE",
               [0, 0.009],
               'green', 
               'blue',
                'In-Sample',
                'Out-Sample',
               'experiment1.png' )

    
    # Experiment 2
    rmse_in_bg10, rmse_out_bg10 = experiment2(data, 0.6, leafs)

    # Chart1
    plot_chart(leafs, 
               rmse_in_bg10[10,:], 
               rmse_out_bg10[10,:], 
               "Effect of Bagging on Overfitting of DTLearner\n(In-Sample Vs Out-Sample)", 
               "Leaf Size", 
               "Average RMSE",
               [0, 0.009],
               'green', 
               'blue',
                'In-Sample',
                'Out-Sample',
               'experiment2.1.png' )

    # Chart2
    plot_chart(leafs, 
               rmse_out_bg10[10,:], 
               rmse_out_dt[10,:], 
               "Effect of Bagging on Overfitting of DTLearner\n(Bagging Vs No Bagging)", 
               "Leaf Size", 
               "Average RMSE",
               [0, 0.009],
               'blue', 
               'red',
                'Out-Sample (20 Bags)',
                'Out-Sample (0 Bag)',
               'experiment2.2.png' )

    # Experiment 3
    mae_dt, mae_rt, time_dt, time_rt = experiment3(data, 0.6, leafs)

    # Chart 1
    plot_chart(leafs, 
               mae_dt[10,:], 
               mae_rt[10,:], 
               "Prediction Performance (Decision Vs Random Tree)", 
               "Leaf Size", 
               "Average MAE",
               [0, 0.009],
               'blue', 
               'red',
                'Decision Tree',
                'Random Tree',
               'experiment3.1.png' )

    # Chart 2
    plot_chart(leafs, 
               time_dt[10,:], 
               time_rt[10,:], 
               "Training Speed (Decision Vs Random Tree)", 
               "Leaf Size", 
               "Time (seconds)",
               [0, 0.04],
               'blue', 
               'red',
                'Decision Tree',
                'Random Tree',
               'experiment3.2.png' )  	   		 	 	 			  		 			     			  	 
