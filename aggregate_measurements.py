# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 18:03:08 2017

@author: s174438
"""

import numpy as np 
import pandas as pd
#Convert tvec and data back to panda dataframe for easier processing:
def aggregate_measurements(tvec,data,period):
    """
    Aggregation of data
    
    INPUT:
        Time vector 'tvec' as numpy array,
        data 'data' as numpy array,
        'period' as type(str)
    
    OUTPUT:
        Aggregated data of 'tvec' and 'data' as numpy array
    """
   
    #Make sure period is case insensitive
    period=period.lower()
    #Join Dataframes so data stays consistent.
    complete=tvec.join(data)
    if period=="hour":
        #Group by hour
        complete1=complete.groupby(["Year","Month","Day","Hour"]).sum()
        tvec_a=complete1
        #Display the data per time unit
        data_a=complete1[["Zone1","Zone2","Zone3","Zone4"]]
        
    if period=="day":
        complete1=complete.groupby("Day").sum()
        tvec_a=complete1
        data_a=complete1[["Zone1","Zone2","Zone3","Zone4"]]
    
    if period=="month":
        complete1=complete.groupby("Month").sum()
        tvec_a=complete1
        data_a=complete1[["Zone1","Zone2","Zone3","Zone4"]]
          
    if period=="hour of the day":
        # index1=np.array(["0:00-1:00","1:00-2:00","2:00-3:00","3:00-4:00","4:00-5:00","5:00-6:00","6:00-7:00","7:00-8:00","8:00-9:00","9:00-10:00","10:00-11:00","11:00-12:00","12:00-13:00","13:00-14:00","14:00-15:00","15:00-16:00","16:00-17:00","17:00-18:00","18:00-19:00","19:00-20:00","20:00-21:00","21:00-22:00","22:00-23:00","23:00-00:00"])
         complete1=complete.groupby("Hour").mean() #This is all the hour summed
         tvec_a=complete1
         data_a=complete1[["Zone1","Zone2","Zone3","Zone4"]]
         #Let the user know that these values are averages, not sums in the time interval
         print("These are the mean values per hour:")
         print(" ")
    if period=="Average Daily Consumption":
        complete1=complete.groupby("Day").mean()
        tvec_a=complete1
        data_a=complete1[["Zone1","Zone2","Zone3","Zone4"]]
        print("These are the mean values per day:")
        print(" ")
    #Display the aggregated data
    print("===================================================")
    print(" ")
    print(data_a)
    print("---------------------------------------------------")
    print(" ")
    #Convert to array for use in other functions. 
    return (tvec_a,data_a)

        
       
    
        