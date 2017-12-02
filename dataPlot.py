# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 12:12:11 2017

@author: Aimas
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def dataPlot(data,period):
    pandata = pd.DataFrame(data = data) #convert data to panda.dataframe 
    if len(pandata) < 25: #if the number of measurements is lower than 25, we do bar plot
        pandata.plot(kind="bar", title="Power Consumption per {}".format(period))
    else:
        pandata.plot(title="Power Consumption per {}".format(period))
    
    #fill labels
    plt.xlabel=("Time in {}".format(period)) 
    #plt.xticks=
    plt.ylabel=("Power in kWh")
    legends = np.array(["Zone 1", "Zone 2", "Zone 3", "Zone 4"])
    plt.legend(legends,loc='center left', bbox_to_anchor=(1, 0.5),fancybox=True)
    plt.show()