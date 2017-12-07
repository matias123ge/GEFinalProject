# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:43:42 2017

@author: Valdemar
"""
import pandas as pd
import numpy as np
def print_statistics(data):
    """
    Prints data in a table
    
    INPUT:
        'data' as numpy array
    
    OUTPUT:
        Table of data with quarters, minimum and maximum
    """
    x=pd.DataFrame(data) #converts data from numpy array to dataframe
    w=x.sum(axis=1) #extra column for all zones (zones summed)
    w=pd.DataFrame(w,columns=["All ||"]) #give it a header
    w=w.quantile([0,0.25,0.5,0.75,1]) #find the percintiles for all zones column
    x.columns=["1   ||","2   ||","3   ||","4   ||"]  #give a header to zone 1,2,3,4
    t=(x.quantile([0,0.25,0.5,0.75,1])) #find the percentiles
    t=(t.join(w)).T #join zone 1,2,3,4 and "all" and transpose it
    t.columns=([["Minimum","1. quart.","2. quart.","3. quart.","Maximum"],["========","=========","=========","=========","========="]])
    #give the final dataframe (table) the correct header
    t.index.name="Zone||" #index name for extra crispyness 
    print("===============================================================\n",t)
    
    if "period" not in globals():#no aggregation
        print("\n===============================================================\nunit=Watt-hour\ntimescale=Consumption/min\n=========================")
    elif period=="Consumption per hour":
        print("unit=kWh\ntimescale=Consumption/hour")
    elif period=="Consumption per day":
        print("unit=kWh\ntimescale=Consumption/day")
    elif period=="Consumption per month":
        print("unit=kWh\ntimescale=Consumption/month")
    elif period=="Hour-of-day consumption":
        print("unit=kWh\ntimescale=average hourly consumption") 
   
    
    return