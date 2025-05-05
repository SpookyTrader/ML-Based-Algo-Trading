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
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
class RTLearner():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    This is a Random Tree Learner (RTLearner). You will need to properly implement this class as necessary.  		  	   		 	 	 			  		 			     			  	 

    :param leaf_size: Is the maximum number of samples to be aggregated at a leaf.
    :type leaf_size: int  	   		 	 	 			  		 			     			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		 	 	 			  		 			     			  	 
        If verbose = False your code should not generate ANY output. When we test your code, verbose will be False.  		  	   		 	 	 			  		 			     			  	 
    :type verbose: bool  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    def __init__(self, leaf_size = 1, verbose=False):  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        Constructor method  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        self.leaf_size = leaf_size
        self.verbose = verbose
        self.tree = None  		 			     			  	 
        
    def build_tree(self, data): # Function to build random decision tree.
        if data.shape[0] <= self.leaf_size: 
            return np.array((-1, np.mean(data[:,-1]), np.nan, np.nan))
        elif np.unique(data[:,-1]).shape[0]==1:
            return np.array((-1, data[:,-1][0], np.nan, np.nan))
        else:
            select_f = np.random.randint(0, data.shape[1]-1)    #Randomly select feature to split data.
            split_val = np.median(data[:,select_f])
            if data[data[:,select_f]<=split_val].shape[0] == data.shape[0]:
                return np.array((-1, np.mean(data[:,-1]), np.nan, np.nan))
            else:
                lefttree = self.build_tree(data[data[:,select_f]<=split_val])
                righttree = self.build_tree(data[data[:,select_f]>split_val])
            if lefttree.ndim == 1:
                root = np.array((select_f, split_val, 1, 2))
            else:
                root = np.array((select_f, split_val, 1, lefttree.shape[0]+1))
            return np.vstack((root, lefttree, righttree))

    def add_evidence(self, data_x, data_y):  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        Add training data to learner  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
        :param data_x: A set of feature values used to train the learner  		  	   		 	 	 			  		 			     			  	 
        :type data_x: numpy.ndarray  		  	   		 	 	 			  		 			     			  	 
        :param data_y: The value we are attempting to predict given the X data  		  	   		 	 	 			  		 			     			  	 
        :type data_y: numpy.ndarray  		  	   		 	 	 			  		 			     			  	 
        """
        data = np.concatenate((data_x,np.reshape(data_y, (-1, 1))), axis=1)
        self.tree = self.build_tree(data)
        if self.verbose == True:
            print(self.tree)
        return None
    

    def author(self):  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        :return: The GT username of the student  		  	   		 	 	 			  		 			     			  	 
        :rtype: str  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        return "wkok6"  # replace tb34 with your Georgia Tech username

    def study_group(self):
        """
        :return: A comma separated string of GT_Name of each member of your study group.
        # Example: "gburdell3, jdoe77, tbalch7" or "gburdell3" if a single individual working alone.
        :rtype: str
        """
        return "wkok6"

    def predict(self, x, tree): # Function to transverse decision tree.
        node = int(tree[0,0])
        if node == -1:
            return tree[0,1]
        if x[node]<= tree[0,1]:
            return self.predict(x, tree[1:,:])
        else:
            next_node = int(tree[0,-1])
            return self.predict(x, tree[next_node:,:])

    def query(self, points):  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        Estimate a set of test points given the model we built.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
        :param points: A numpy array with each row corresponding to a specific query.  		  	   		 	 	 			  		 			     			  	 
        :type points: numpy.ndarray  		  	   		 	 	 			  		 			     			  	 
        :return: The predicted result of the input data according to the trained model  		  	   		 	 	 			  		 			     			  	 
        :rtype: numpy.ndarray  		  	   		 	 	 			  		 			     			  	 
        """
        results = np.zeros((1,))
        for x in points:    # Send datapoints one-by-one to predict().
            results = np.append(results, self.predict(x, self.tree))
        return results[1:]		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
# if __name__ == "__main__":  		  	   		 	 	 			  		 			     			  	 
#     print("the secret clue is 'zzyzx'")  		  	   		 	 	 			  		 			     			  	 
