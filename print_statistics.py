# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:43:42 2017

@author: Valdemar
"""
import pandas as pd
import numpy as np
def print_statistics(data,aggBool,period):
    """
    Prints data in a table
    
    INPUT:
        'data' as pd.dataFrame
    
    OUTPUT:
        Table of data with quarters, minimum and maximum
    """
    StatData=data.copy()
    w=StatData.sum(axis=1) #extra column for all zones (zones summed)
    w=pd.DataFrame(w,columns=["All ||"]) #give it a header
    w=w.quantile([0,0.25,0.5,0.75,1]) #find the percintiles for all zones column
    StatData.columns=["1   ||","2   ||","3   ||","4   ||"]  #give a header to zone 1,2,3,4
    t=(StatData.quantile([0,0.25,0.5,0.75,1])) #find the percentiles
    t=(t.join(w)).T #join zone 1,2,3,4 and "all" and transpose it
    t.columns=([["Minimum",
                 "1. quart.",
                 "2. quart.",
                 "3. quart.",
                 "Maximum"],
    ["========","=========","=========","=========","========="]])
    #give the final dataframe (table) the correct header
    t.index.name="Zone||" #index name for extra crispyness 
    
    if np.any(t>10000): #show the table with unit kWh instead of Wh, if data values are large
        t = t/1000
        unit = "kWh"
        unit2 = "Kilo watt "
    else:
        unit = "Wh"
        unit2 = "Watt "
    
    print("===============================================================\n",t,
          "\n===============================================================")
    #print the units of the table and method of aggregation
    if aggBool == False: #no aggregation
        print("unit: {}hours [{}]\ntimeinterval: Consumption per minute [{}/min]\n=========================\n".format(unit2,unit,unit))
    elif period == "hour of the day":
        print("unit: {}hours [{}]\ntimeinterval: Consumption per hour [{}/h]\n=========================\n".format(unit2,unit,unit))
    elif period == "average daily consumption":
        print("units: {}hours [{}]\ntimeinterval: Average consumption per day [{}/day]\n=========================\n".format(unit2,unit,unit))
    else:
        print("unit: {}hours [{}]\ntimeinterval: Consumption per {} [{}/{}]\n=========================\n".format(unit2,unit,period,unit,period))

    return