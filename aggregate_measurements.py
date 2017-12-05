# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 18:03:08 2017

@author: s174438
"""

import numpy as np 
import pandas as pd
#Convert tvec and data back to panda dataframe for easier processing:
def aggregate_measurements(tvec,data,period):
    header=np.array(["Year","Month","Day","Hour","Minutes","Seconds"])
    header2=np.array(["Zone1","Zone2","Zone3","Zone4"])
    tvec.astype(int)
    data.astype(int)
    tvec=pd.DataFrame(tvec,columns=header)
    data=pd.DataFrame(data, columns=header2)
    #Make sure period is case insensitive
    period=period.lower()
    complete=tvec.join(data)
    if period=="hour":
        #Group by hour
        complete.groupby("Hour")
        #There needs to be some kind of sum command here or minutes wont be combined. 
        complete.head(1)#This is wrong, gives what we would expect for hour of the day, but only for the first day...
        
        
    
    
    if period=="day":
        complete.groupby("Day").sum()
    
    if period=="month":
        complete.groupby("Month").sum()
    
    if period=="hour of the day":
         complete.groupby("Hour").sum() #This is all the hour summed. Needs seperation 
        
        #.mean BRUGBAR TIL GENNEMSNITTET AF MÅLINGER
        #COUNT FUNCTIONEN BLIVER BRUGBAR TIL tvec_a
    
        