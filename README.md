# Shell.AI EV Challenge 2022 - Team Cerebro
This was the submission for the SHELLAI-EV-Challenge 2022 

# Problem Statement:
The challenge was to optimally place EV charging stations so that the configuration remains robust to demographic changes.

All demand points of a geographic region collectively create a demand map over the region of interest. For each demand point, forecasting can be done using the historical demand maps.

EV charging stations are typically installed at public parking locations so that EVs can be charged during the idle parking time. These parking locations are predefined based on how real estate has been developed in the region. These are called supply points. Each parking location has a fixed number of parking slots i.e. potential places to install EV charging stations. Typically, two types of charging station are installed based on their supply capacity: i) slow charging station (SCS) and ii) fast charging station (FCS). Based on how many SCS and FCS are installed at a parking location and their respective charging capacities, we can calculate the maximum supply that can be given by each supply point. All supply points of a geographic region collectively create a supply map over a region.

Using the demand map, supply map, demand-supply constraints and objective, optimally place the EV charging stations so that the designed EV infrastructure is best suited to cater the forecasted demand.

![EV charging stations](./images/readme.png)

# Our Solution:

We classified our approach into two parts. The first part involves robust prediction of demand using  N-beats model which can give very accurate demand results using effective time-series approach. The second part involves taking various demand predicted and formulating the demand supply matrixes for year 2019 and 2020 that satisfy various constraints using the linear programming. 


## N-BEATS: NEURAL BASIS EXPANSION ANALYSIS FOR INTERPRETABLE TIME SERIES FORECASTING

We focus on solving the univariate times series point forecasting problem using deep learning. We propose a deep neural architecture based on backward and forward residual links and a very deep stack of fully-connected layers. The architecture has a number of desirable properties, being interpretable, applicable without modification to a wide array of target domains, and fast to train. The model demonstrates state-of-the-art performance for two configurations of N-BEATS for all the datasets, improving forecast accuracy by 11% over a statistical benchmark and by 3% over last year’s winner of the M4 competition, a domain-adjusted hand-crafted hybrid between neural network and statistical time series models. 
For more information visit: https://github.com/philipperemy/n-beats
For more information about the paper, refer https://arxiv.org/pdf/1905.10437.pdf 


## Linear Programming Part

We used PuLP library for the implementation of the constraints as provided in the problem statement. Then the solution is converted into a demand-supply matrix that can represent the spread of demand between 4096 demand points and 100 supply points. 
For more information about PuLP library, visit: https://coin-or.github.io/pulp/

# Team Details:
| Name | Year | Major| Institution | Groups within IITR |
|-----|------|------|-------------|--------------------|
| Aryan Gupta | Sophomore | BTech Electrical Engineering | IIT Roorkee | Core Team Member DSG 
| Devansh Bharadwaj | Sophomore | BTech Electronics & Computation Engineering | IIT Roorkee | Core Team Member DSG 
| Pradnya Shimpi| Sophomore | BTech Electrical Engineering | IIT Roorkee | Core Team Member DSG & Developer SDSLabs 
| Sanidhya Singh| Sophomore | BTech Computer Science Engineering | IIT Roorkee | Core Team Member DSG 



