""""""  		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 
Template for implementing QLearner  (c) 2015 Tucker Balch  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
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
  		  	   		 	 	 			  		 			     			  	 
import random as rand  		  	   		 	 	 			  		 			     			  	  		  	   		 	 	 			  		 			     			  	 
import numpy as np  		  	   		 	 	 			  		 			     			  	   	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
class QLearner(object):  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    This is a Q learner object.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
    :param num_states: The number of states to consider.  		  	   		 	 	 			  		 			     			  	 
    :type num_states: int  		  	   		 	 	 			  		 			     			  	 
    :param num_actions: The number of actions available..  		  	   		 	 	 			  		 			     			  	 
    :type num_actions: int  		  	   		 	 	 			  		 			     			  	 
    :param alpha: The learning rate used in the update rule. Should range between 0.0 and 1.0 with 0.2 as a typical value.  		  	   		 	 	 			  		 			     			  	 
    :type alpha: float  		  	   		 	 	 			  		 			     			  	 
    :param gamma: The discount rate used in the update rule. Should range between 0.0 and 1.0 with 0.9 as a typical value.  		  	   		 	 	 			  		 			     			  	 
    :type gamma: float  		  	   		 	 	 			  		 			     			  	 
    :param rar: Random action rate: the probability of selecting a random action at each step. Should range between 0.0 (no random actions) to 1.0 (always random action) with 0.5 as a typical value.  		  	   		 	 	 			  		 			     			  	 
    :type rar: float  		  	   		 	 	 			  		 			     			  	 
    :param radr: Random action decay rate, after each update, rar = rar * radr. Ranges between 0.0 (immediate decay to 0) and 1.0 (no decay). Typically 0.99.  		  	   		 	 	 			  		 			     			  	 
    :type radr: float  		  	   		 	 	 			  		 			     			  	 
    :param dyna: The number of dyna updates for each regular update. When Dyna is used, 200 is a typical value.  		  	   		 	 	 			  		 			     			  	 
    :type dyna: int  		  	   		 	 	 			  		 			     			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		 	 	 			  		 			     			  	 
    :type verbose: bool  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    def __init__(  		  	   		 	 	 			  		 			     			  	 
        self,  		  	   		 	 	 			  		 			     			  	 
        num_states=100,  		  	   		 	 	 			  		 			     			  	 
        num_actions=4,  		  	   		 	 	 			  		 			     			  	 
        alpha=0.2,  		  	   		 	 	 			  		 			     			  	 
        gamma=0.9,  		  	   		 	 	 			  		 			     			  	 
        rar=0.5,  		  	   		 	 	 			  		 			     			  	 
        radr=0.99,  		  	   		 	 	 			  		 			     			  	 
        dyna=0,  		  	   		 	 	 			  		 			     			  	 
        verbose=False,  		  	   		 	 	 			  		 			     			  	 
    ):  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        Constructor method  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        self.num_states = num_states
        self.num_actions = num_actions 
        self.alpha =  alpha
        self.gamma = gamma
        self.rar = rar
        self.radr = radr
        self.dyna = dyna 		  	   		 	 	 			  		 			     			  	 
        self.verbose = verbose  

        self.s = 0  		  	   		 	 	 			  		 			     			  	 
        self.a = 0
        self.Q_table = np.zeros((self.num_states, self.num_actions))    # Create and initialize a Q array.
        
        if self.dyna > 0:   # If dyna is used, create and initialize the experience, Tc, T and R arrays.
            self.experience = np.array([[0, 0, 0, 0]])
            self.Tc_table = np.zeros((self.num_states, self.num_actions, self.num_states))
            self.Tc_table[:,:,:] = 0.00001  # Initialize to a very small number to prevent division by zero error (Prof Balch's video).
            self.T_table = self.Tc_table.copy()
            self.R_table = np.zeros((self.num_states, self.num_actions))

    def update_Qtable(self, s, a, s_prime, r):  # Function for updating Q array.
        self.Q_table[s,a] = (1-self.alpha)*self.Q_table[s,a] + self.alpha * (r + self.gamma * (self.Q_table[s_prime, np.argmax(self.Q_table[s_prime,:])]))

    def next_action(self, s_prime):     # Function for determining the next action to take, given the new state.
        if rand.random() < self.rar:
            action = rand.randint(0, self.num_actions - 1)
        else:
            action = np.argmax(self.Q_table[s_prime,:])  		 
        self.rar *= self.radr

        return action

    def update_models(self, s, a, s_prime, r):  # Function for updating the experience, Tc, T and R arrays.
        if np.all(self.experience[0,:]==0):
            self.experience[0,:] = [s, a, s_prime, r]   # Assign the 1st experience tuple to the 1st row.
        else:
            self.experience = np.append(self.experience,[[s, a, s_prime, r]], axis=0)   # Append subsequent experience tuples to the array.

        self.Tc_table[s, a, s_prime] += 1
        self.T_table = self.Tc_table / (np.sum(self.Tc_table, axis=2).reshape(self.num_states, self.num_actions, -1))   # Compute transition state probabilities.
        
        self.R_table[s, a] = (1-self.alpha) * self.R_table[s, a] + (self.alpha * r) # Update R array.

    def hallucinate(self):  # Function to generate hallucination experience from past experiences for dyna step.
        exp_idx = rand.randint(0, self.experience.shape[0]-1)
        dyna_s = self.experience[exp_idx,0]
        dyna_a = self.experience[exp_idx,1]
        dyna_s_prime = np.argmax(self.T_table[dyna_s, dyna_a,:])    # Determine the transition state with the highest probability.
        dyna_r = self.R_table[dyna_s, dyna_a]
        self.update_Qtable(dyna_s, dyna_a, dyna_s_prime, dyna_r)    # Update Q array.

    def querysetstate(self, s):  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        Update the state without updating the Q-table  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
        :param s: The new state  		  	   		 	 	 			  		 			     			  	 
        :type s: int  		  	   		 	 	 			  		 			     			  	 
        :return: The selected action  		  	   		 	 	 			  		 			     			  	 
        :rtype: int  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        self.s = s  		  	   		 	 	 			  		 			     			  	 
        action = rand.randint(0, self.num_actions - 1)
        self.a = action	  	   		 	 	 			  		 			     			  	 
        if self.verbose:  		  	   		 	 	 			  		 			     			  	 
            print(f"s = {s}, a = {action}")  		  	   		 	 	 			  		 			     			  	 
        return action  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
    def query(self, s_prime, r):  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        Update the Q table and return an action  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
        :param s_prime: The new state  		  	   		 	 	 			  		 			     			  	 
        :type s_prime: int  		  	   		 	 	 			  		 			     			  	 
        :param r: The immediate reward  		  	   		 	 	 			  		 			     			  	 
        :type r: float  		  	   		 	 	 			  		 			     			  	 
        :return: The selected action  		  	   		 	 	 			  		 			     			  	 
        :rtype: int  		  	   		 	 	 			  		 			     			  	 
        """  		  	   		 	 	 			  		 			     			  	 
        
        self.update_Qtable(self.s, self.a, s_prime, r)
        
        if self.dyna > 0:
            self.update_models(self.s, self.a, s_prime, r)
            for i in range(self.dyna):
                self.hallucinate()

        action = self.next_action(s_prime)

        self.s = s_prime
        self.a = action	   		 	 	 			  		 			     			  	 
        
        if self.verbose:  		  	   		 	 	 			  		 			     			  	 
            print(f"s = {s_prime}, a = {action}, r={r}")  		  	   		 	 	 			  		 			     			  	 
        return action  		  	   		 	 	 			  		 			     			  	 

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
  		  	   		 	 	 			  		 			     			  	 
# if __name__ == "__main__":  		  	   		 	 	 			  		 			     			  	 
#     print("Remember Q from Star Trek? Well, this isn't him")  		  	   		 	 	 			  		 			     			  	 
