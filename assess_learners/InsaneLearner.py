""""""  		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 
A simple wrapper for linear regression.  (c) 2015 Tucker Balch  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
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
import numpy as np
import BagLearner as bl
import LinRegLearner as lr	   		 	 	 			  		 			     			  	 	 	 	 			  		 			     			  	 
class InsaneLearner():
    def __init__(self, verbose = False):
        self.learner = [bl.BagLearner(learner=lr.LinRegLearner, kwargs={}, bags = 20, boost = False, verbose = False) for i in range(20)]
        self.verbose = verbose    
    def add_evidence(self, data_x, data_y):
        for l in self.learner:
            l.add_evidence(data_x, data_y)   
    def query(self,data_x):
        predictions = np.zeros((1,data_x.shape[0]))
        for l in self.learner:
            predictions = np.append(predictions, l.query(data_x).reshape(1,-1), axis=0)
        predictions = predictions[1:,:]
        predictions = np.append(predictions, np.mean(predictions, axis=0).reshape(1,-1), axis=0)
        return predictions[-1,:]
    def author(self):  		  	   		 	 	 			  		 			     			  	 	  	   		 	 	 			  		 			     			  	 
        return "wkok6"  # replace tb34 with your Georgia Tech username
  	   		 	 	 			  		 			     			  	 
