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
    Rownames=["1   ||","2   ||","3   ||","4   ||","All ||"]
    Columnames=([["Minimum","1. quart.","2. quart.","3. quart.","Maximum"],["========","=========","=========","=========","========="]])
    
    #Gotta redo when we got the aggregate function up and running
    
    dataT=data.T
    alldata=np.sum(dataT,axis=0)
    Table1=np.array([0,0,0,0,0])
    Table1[0]=np.min(dataT[0,:])
    Table1[1]=np.percentile(dataT[0,:],25)
    Table1[2]=np.median(dataT[0,:])
    Table1[3]=np.percentile(dataT[0,:],75)
    Table1[4]=np.max(dataT[0,:])
    
    Table2=np.array([0,0,0,0,0])
    Table2[0]=np.min(dataT[1,:])
    Table2[1]=np.percentile(dataT[1,:],25)
    Table2[2]=np.median(dataT[1,:])
    Table2[3]=np.percentile(dataT[1,:],75)
    Table2[4]=np.max(dataT[1,:])
    
    Table3=np.array([0,0,0,0,0])
    Table3[0]=np.min(dataT[2,:])
    Table3[1]=np.percentile(dataT[2,:],25)
    Table3[2]=np.median(dataT[2,:])
    Table3[3]=np.percentile(dataT[2,:],75)
    Table3[4]=np.max(dataT[2,:])
    
    Table4=np.array([0,0,0,0,0])
    Table4[0]=np.min(dataT[3,:])
    Table4[1]=np.percentile(dataT[3,:],25)
    Table4[2]=np.median(dataT[3,:])
    Table4[3]=np.percentile(dataT[3,:],75)
    Table4[4]=np.max(dataT[3,:])
    
    Table5=np.array([0,0,0,0,0])
    Table5[0]=np.min(alldata)
    Table5[1]=np.percentile(alldata,25)
    Table5[2]=np.median(alldata)
    Table5[3]=np.percentile(alldata,75)
    Table5[4]=np.max(alldata)
    
    Tablevalues=np.vstack((Table1,Table2,Table3,Table4,Table5))
    Table=pd.DataFrame(Tablevalues,index=Rownames,columns=Columnames)
    
    Table.index.name = 'Zone||'
    print("===============================================================\n",Table)
    
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