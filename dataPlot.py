# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 12:12:11 2017
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def dataPlot(data,period,plotType):
    pandata = pd.DataFrame(data = data) #convert data to panda.dataframe 
    if len(pandata) < 25: #if the number of measurements is lower than 25, we do bar plot
        pandata.plot(kind="bar", title="Power Consumption per {}".format(period)) #do a barplot
    else:
        pandata.plot(title="Power Consumption per {}".format(period)) #do a lineplot
    
    #fill labels
    plt.xlabel = ("Time in {}".format(period))  #set x-label
    #plt.xticks 
    plt.ylabel = ("Power in kWh") #set y-label
    if plotType == 1: #give a label to each zone
        legends = np.array(["Zone 1", "Zone 2", "Zone 3", "Zone 4"])
        plt.legend(legends,loc='center left', bbox_to_anchor=(1, 0.5),fancybox=True)
    elif plotType == 2: #set legend to 'all zones' 
        legends = np.array(["All zones"])
        plt.legend(legends,loc='center left', bbox_to_anchor=(1, 0.5),fancybox=True)
    plt.show()