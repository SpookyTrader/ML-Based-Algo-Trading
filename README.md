## CS7646 - Machine Learning for Trading
This repository is a catalog of projects I have completed as part of the course, CS7646, for the Master of Science in Computer Science program in
Georgia Tech. Each project is a stepping stone to the capstone project in which students are required to build and evaluate a machine learning-based
AI trading system. The smaller projects enable students to acquire the skills and knowledge required for constructing each component of the AI trading 
system in final capstone project. The relationship of these projects in relation to the capstone is illustrated in Figure 1. The objective of each 
project is as described below. Key results of each project are presented where appropriate.

<p align="center">
  <img src="https://github.com/user-attachments/assets/7faac237-3fa6-46f6-b221-d8677c183108" alt="Diagram" width="850" height='300'/>
</p>
<p align="center"><em>Figure 1: Relationship of the smaller projects in relation to the capstone project. (Source: Georgia Tech CS7646 Spring 2025 Canvas).</em></p>

### Project 1 (martingale)
The goal of this project is to enable students to develope an understanding of common probabilistic and statistical concepts and tools associated with 
machine learning, such as expectations, standard deviations, sampling, minimum values, maximum values and convergence via analysing the statistical
properties of a martingale betting strategy. The scripts can be run by executing the commands as following.

For Linux/Ubuntu
```
PYTHONPATH=../:. python martingale.py
```
For Window Powershell
```
$env:PYTHONPATH = "..;."
python martingale.py
```

### Project 2 (optimize_something)
The goal of this project is allow students to learn how to use the SciPy optimization function to determine the stock allocation in a portfolio that maximizes 
specific portfolio performance metric, and familarize themselves with the implementation of several metrics commonly used in portfolio performance evaluation.
Figure 2 compares the performances of a portfolio of optimized stock allocation and SPY index ETF.

<p align="center">
  <img src="https://github.com/user-attachments/assets/6c41f3bf-d2ac-4586-93db-b48046cd521d" alt="Diagram" width="500" height='400'/>
</p>
<p align="center"><em>Figure 2: Comparison of optimized portfolio with SPY ETF. Portfolio is optimized for Sharpe ratio.</em></p>

The scripts for generating the results can be run by executing the commands as following.

For Linux/Ubuntu
```
PYTHONPATH=../:. python optimization.py
```
For Window Powershell
```
$env:PYTHONPATH = "..;."
python optimization.py
```

### Project 3 (assess_learners)
The goal of this project is to construct and implement 4 supervised regression learners from an algorithmic family called Classification and Regression Trees (CARTs)
from scratch according to the JR Quinlan method. Specifically, a decision tree, a random decision tree, an ensemble bag learner that incorporate bootstrap aggregation 
with any basic learner, and an insane learner that consists of a collection of 20 bag learners are implemented. The effects of leaf size and number of bags on overfitting
and underfitting are investigated by applying the algorithms on a dataset to predict the return of MSCI Emerging Markets index from that of the other market indices.
Figure 3 shows the effects of leaf size and bagging on overfitting of decision tree.

<p align="center">
  <img src="https://github.com/user-attachments/assets/cafb9270-606e-4947-a678-8b1b3318119b" alt="Diagram" width="500" height='400'/>
  <img src="https://github.com/user-attachments/assets/c59d5d2a-3aef-41b7-a371-7a4c946075a1" alt="Diagram" width="500" height='400'/>
</p>
<p align="center"><em>Figure 3: Effects of leaf size and bagging on overfitting of decision tree.</em></p>

The scripts for generating the results can be run by executing the commands as following.

For Linux/Ubuntu
```
PYTHONPATH=../:. python testlearner.py
```
For Window Powershell
```
$env:PYTHONPATH = "..;."
python testlearner.py
```

### Project 4 (defeat_learners)
The goal of this project is to demonstrate the relative strengths and weaknesses of a Decision Tree learner as compared to a Linear Regression Learner by producing
1) synthetic dataset that enable a linear regression learner to consistently outperform a decision tree learner.
2) synthetic dataset that enable a decision tree learner to consistently outperform a linear regression learner. 

The scripts for generating the datasets and results can be run by executing the commands as following.

For Linux/Ubuntu
```
PYTHONPATH=../:. python testbest4.py
```
For Window Powershell
```
$env:PYTHONPATH = "..;."
python testbest4.py
```

### Project 5 (marketsim)
The goal of project 5 is to create a market simulator that accepts trading orders, keeps track of and assess a portfolio’s value and performance over time.
Develop an understanding of market costs and how they affect the value of a portfolio. Transaction costs are an important consideration of an investing strategy.
Transaction costs include things like commissions, slippage, market impact, and tax considerations. High transaction costs encourage less frequent trading, and 
accordingly a search for strategies that payout over longer periods of time rather than just intraday or over several days. Here, commission and market impact are
considered. The scripts for generating the market simulator and results can be run by executing the commands as following.

For Linux/Ubuntu
```
PYTHONPATH=../:. python marketsim.py
```
For Window Powershell
```
$env:PYTHONPATH = "..;."
python marketsim.py
```

### Project 6 (indicator_evaluation)
In this project, the goals are:
1) Develop technical indicators illustrating how they might be used to generate trading signals. They will be utilized in the capstone project to devise an
   intuition-based trading strategy and a Machine Learning-based trading strategy. 
2) Develop a Theoretically Optimal Strategy which represents the maximum amount a portfolio can theoretically return.

<p align="center">
  <img src="https://github.com/user-attachments/assets/f6a8381c-96e2-49ff-b633-1393991e39f0" alt="Diagram" width="500" height='400'/>
  <img src="https://github.com/user-attachments/assets/67a291aa-09c7-4de9-bdd6-126dd632998b" alt="Diagram" width="500" height='400'/>
</p>
<p align="center"><em>Figure 4: %B (left) and CCI (right) indicators identifying potential overbought and oversold price actions of JPM stock.</em></p>
</p>


<p align="center">
  <img src="https://github.com/user-attachments/assets/720ae201-e1b9-4ae1-832d-758c73c54ab2" alt="Diagram" width="500" height='400'/>
  <img src="https://github.com/user-attachments/assets/10bf8776-e354-4ad4-a93b-96d76f98a8c0" alt="Diagram" width="500" height='400'/>
</p>
<p align="center"><em>Figure 5: Momentum (left) and PPO (right) indicators identifying potential change in price momentum and trend direction of JPM stock.</em></p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/e674b26e-b6bc-49a8-9cce-d7c4dff081dc" alt="Diagram" width="500" height='400'/>
</p>
<p align="center"><em>Figure 6: Maximum performance that can be achieved assuming we can see the future. Benchmark = Buy and hold strategy.</em></p>

For Linux/Ubuntu
```
PYTHONPATH=../:. python testproject.py
```
For Window Powershell
```
$env:PYTHONPATH = "..;."
python testproject.py
```

### Project 7 (qlearning_robot)
The goal of this project is to implement the Q-Learning and Dyna-Q solutions to the reinforcement learning problem via application in a navigation problem. 
It can be adapted for application in trading subsequently in the capstone project. 

For Linux/Ubuntu
```
PYTHONPATH=../:. python testqlearner.py
```
For Window Powershell
```
$env:PYTHONPATH = "..;."
python testqlearner.py
```

### Capstone Project (strategy evaluation)

<p align="center">
  <img src="https://github.com/user-attachments/assets/62d0f08a-9f93-4c67-ad27-747a1975953b" alt="Diagram" width="500" height='400'/>
  <img src="https://github.com/user-attachments/assets/463c33a4-4b38-4124-b936-616f28b93095" alt="Diagram" width="500" height='400'/>
</p>
<p align="center"><em>Figure 1: Building Blocks of A Machine Learning-Based AI Trading Agent.</em></p>


<p align="center">
  <img src="https://github.com/user-attachments/assets/26baf084-8776-4fcb-9604-1817af295a67" alt="Diagram" width="500" height='400'/>
  <img src="https://github.com/user-attachments/assets/26baf084-8776-4fcb-9604-1817af295a67" alt="Diagram" width="500" height='400'/>
</p>
<p align="center"><em>Figure 1: Building Blocks of A Machine Learning-Based AI Trading Agent.</em></p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/51633d1d-d058-4452-a6ed-53bf832d8805" alt="Diagram" width="500" height='400'/>
  <img src="https://github.com/user-attachments/assets/2071bd41-c004-4ef4-8220-d56457d32354" alt="Diagram" width="500" height='400'/>
</p>
<p align="center"><em>Figure 1: Building Blocks of A Machine Learning-Based AI Trading Agent.</em></p>








