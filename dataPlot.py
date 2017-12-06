# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 12:12:11 2017
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def dataPlot(data,period,plotType):
    """
    Plots given data as with a specified period.
    
    INPUT:
        data as numpy array,
        period as type(str),
        plotType as type(int)
        
    OUTPUT:
        plt.plot of data
    """
    plt.figure()
    pandata = pd.DataFrame(data = data) #convert data to panda.dataframe 
    if len(pandata) < 25: #if the number of measurements is lower than 25, we do bar plot
        pandata.plot(kind="bar", title="Power Consumption per {:s}".format(period)) #do a barplot
    else:
        pandata.plot(title="Power Consumption per {:s}".format(period)) #do a lineplot
    
    #fill label
    plt.xlabel("Time in {:s}".format(period))  #set name for x-axis
    #plt.xticks 
    plt.ylabel("Power in kWh") #set name for y-axis
    
    if plotType == 1: #give a label to each zone
        legends = np.array(["Zone 1", "Zone 2", "Zone 3", "Zone 4"])
        plt.legend(legends,loc='center left',
                   bbox_to_anchor=(1, 0.5),fancybox=True)
    elif plotType == 2: #set legend to 'all zones' 
        legends = np.array(["All zones"])
        plt.legend(legends,loc='center left',
                   bbox_to_anchor=(1, 0.5),fancybox=True)
    plt.show()

"""    
if __name__ == "__main__":
    from load_measurements import load_measurements
    from aggregate_measurements import aggregate_measurements
    tvec,data = load_measurements("2008.csv","drop")
    tvec,data = aggregate_measurements(tvec,data,"hour")
    
    dataPlot(data,"hour",1)
"""