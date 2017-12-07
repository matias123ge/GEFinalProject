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
    if period=="minute":
        #Group by minute(the data displayed is the same as the data loaded originally)
        complete1=complete.copy()
        tvec_a=complete1
        #Display the data per time unit
        data_a=complete1[["Zone1","Zone2","Zone3","Zone4"]]#Display the data
        data_a.index.name="Minute"
    if period=="hour":
        #Group by hour for aggregation
        complete1=complete.groupby(["Hour"]).sum() #sum the hours
        tvec_a=complete1
        #Display the data per time unit
        data_a=complete1[["Zone1","Zone2","Zone3","Zone4"]]
        
    if period=="day":
        #Group by day for aggregation
        complete1=complete.groupby("Day").sum()
        tvec_a=complete1
        data_a=complete1[["Zone1","Zone2","Zone3","Zone4"]]
    
    if period=="month":
        #Group by month for aggregation
        complete1=complete.groupby("Month").sum()
        tvec_a=complete1
        data_a=complete1[["Zone1","Zone2","Zone3","Zone4"]]
          
    if period=="hour of the day":
         complete1=complete.groupby("Hour").mean() #This the average (mean) of all the electricity usage per hour
         tvec_a=complete1
         data_a=complete1[["Zone1","Zone2","Zone3","Zone4"]]
         #Let the user know that these values are averages, not sums in the time interval
         print("These are the mean values per hour:")
         print(" ")
    if period=="average daily consumption":
        #Same as above except for daily average instead of hour
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

        
       
    
        