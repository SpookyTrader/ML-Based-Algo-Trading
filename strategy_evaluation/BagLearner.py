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
from scipy import stats
  		  	   		 	 	 			  		 			     			  	 
class BagLearner():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    This is a Bootstrap Aggregation Learner (BagLearner). You will need to properly implement this class as necessary.  		  	   		 	 	 			  		 			     			  	 

    :param learner (learner): Points to any arbitrary learner class that will be used in the BagLearner
    :type learner: object
    :param kwargs: Keyword arguments that are passed on to the learner’s constructor and they can vary according to the learner
    :type kwargs: dict
    :param bags: The number of learners you should train using Bootstrap Aggregation 
        If boost is true, then you should implement boosting (optional implementation).
    :type bags: int
    :param boost: If boost is true, implement boosting (optional implementation)
    :type boost: bool	 	 			  		 			     			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		 	 	 			  		 			     			  	 
        If verbose = False your code should not generate ANY output. When we test your code, verbose will be False.  		  	   		 	 	 			  		 			     			  	 
    :type verbose: bool	  	   		 	 	 			  		 			     			  	 
    """

    def __init__(self, learner, kwargs={}, bags = 20, boost = False, verbose = False):
        self.learner = learner
        self.kwargs = kwargs
        self.bags = bags
        self.boost = boost
        self.verbose = verbose 			     			  	 
        
    def instantiate_learners(self):  # Function to instantiate learners one-by-one based on the number of bags required.
        learner = [self.learner(**self.kwargs) for i in range(self.bags)]
        self.learner = learner
        return 

    def add_evidence(self, data_x, data_y):  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        Add training data to learner  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
        :param data_x: A set of feature values used to train the learner  		  	   		 	 	 			  		 			     			  	 
        :type data_x: numpy.ndarray  		  	   		 	 	 			  		 			     			  	 
        :param data_y: The value we are attempting to predict given the X data  		  	   		 	 	 			  		 			     			  	 
        :type data_y: numpy.ndarray  		  	   		 	 	 			  		 			     			  	 
        """
        self.instantiate_learners()
        data = np.concatenate((data_x,np.reshape(data_y, (-1, 1))), axis=1)
        for bag in range(self.bags):
            i = np.random.choice(np.arange(data.shape[0]),size=data.shape[0])   # Randomly sample n datapoints from training set of n size with replacement.
            sample =  data[i,:]
            sample_x = sample[:,:-1]
            sample_y = sample[:,-1]
            self.learner[bag].add_evidence(sample_x, sample_y)  # Train learners one-by-one, each with randomly sampled training data.
        return
    
    def author(self):  		  	   		 	 	 			  		 			     			  	 
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

    def query(self, points):  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        Estimate a set of test points given the model we built.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
        :param points: A numpy array with each row corresponding to a specific query.  		  	   		 	 	 			  		 			     			  	 
        :type points: numpy.ndarray  		  	   		 	 	 			  		 			     			  	 
        :return: The predicted result of the input data according to the trained model  		  	   		 	 	 			  		 			     			  	 
        :rtype: numpy.ndarray  		  	   		 	 	 			  		 			     			  	 
        """
        predictions = np.zeros((1,points.shape[0]))
        for l in self.learner:
            predictions = np.append(predictions, l.query(points).reshape(1,-1), axis=0)
        predictions = predictions[1:,:]     # Remove the 1st row of zeros. 
        predictions = np.append(predictions, stats.mode(predictions, axis=0)[0].reshape(1,-1), axis=0) #  Get the mode of n bags of predictions. Majority voting.
        return predictions[-1,:] 		  			  	 
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
# if __name__ == "__main__":  		  	   		 	 	 			  		 			     			  	 
#     print("the secret clue is 'zzyzx'")  		  	   		 	 	 			  		 			     			  	 
