### This was the submission for the SHELLAI-EV-Challenge

# Problem Statement:
The challenge was to optimally place EV charging stations so that the configuration remains robust to demographic changes.

All demand points of a geographic region collectively create a demand map over the region of interest. For each demand point, forecasting can be done using the historical demand maps.

EV charging stations are typically installed at public parking locations so that EVs can be charged during the idle parking time. These parking locations are predefined based on how real estate has been developed in the region. These are called supply points. Each parking location has a fixed number of parking slots i.e. potential places to install EV charging stations. Typically, two types of charging station are installed based on their supply capacity: i) slow charging station (SCS) and ii) fast charging station (FCS). Based on how many SCS and FCS are installed at a parking location and their respective charging capacities, we can calculate the maximum supply that can be given by each supply point. All supply points of a geographic region collectively create a supply map over a region.

Using the demand map, supply map, demand-supply constraints and objective, optimally place the EV charging stations so that the designed EV infrastructure is best suited to cater the forecasted demand.

# Our Solution:
##For Demand Forcasting
For demand forecasting we took max values for 2019 and 2020 demands predicted using the following two models:

### Linear Regression:
The first model is a simple linear regressor where seperate linear regression models were trained for 4096 demand points.

### N-BEATS: 
### Optimiztion:

## Team Details:
Aryan Gupta: Sophomore | BTech Electrical Engineering | IIT Roorkee | Core Team Member DSG 
Devansh Bharadwaj: Sophomore | BTech Electronics & Computation Engineering | IIT Roorkee | Core Team Member DSG 
Pradnya Shimpi: Sophomore | BTech Electrical Engineering | IIT Roorkee | Core Team Member DSG | Developer SDSLabs 
Sanidhya Singh: Sophomore | BTech Computer Science Engineering | IIT Roorkee | Core Team Member DSG 



