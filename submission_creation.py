'''Variables Assumed: 
SCS,FCS2019,20
dsmatrix2019,20'''

import warnings
warnings.filterwarnings("ignore")

submit = pd.DataFrame(columns=["year","data_type","demand_point_index","supply_point_index","value"])
for i in range(100):
    submit.loc[len(submit.index)]=[2019,"SCS","",i,SCS_2019[i]]
for i in range(100):
    submit.loc[len(submit.index)]=[2019,"FCS","",i,FCS_2019[i]]  
for i in range(4096):
    for j in range(100):
        submit.loc[len(submit.index)]=[2019,"DS",i,j,dsmatrix2019[i][j]]
for i in range(100):
    submit.loc[len(submit.index)]=[2020,"SCS","",i,SCS_2020[i]]
for i in range(100):
    submit.loc[len(submit.index)]=[2020,"FCS","",i,FCS_2020[i]]  
for i in range(4096):
    for j in range(100):
        submit.loc[len(submit.index)]=[2020,"DS",i,j,dsmatrix2020[i][j]]
submit.to_csv('submit.csv')
submit.head()
