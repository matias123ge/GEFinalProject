# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 12:12:11 2017

@author: Aimas
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def dataPlot(data,period):
    pandata = pd.DataFrame(data = data)
    if len(pandata) < 25:
        pandata.plot(kind="bar", title="Power Consumption per {}".format(period))
    else:
        pandata.plot(title="Power Consumption per {}".format(period))
    
    plt.xlabel=("Time in {}".format(period))
    #plt.xticks=
    plt.ylabel=("Power in kWh")
    legends = np.array(["Zone 1", "Zone 2", "Zone 3", "Zone 4"])
    plt.legend(legends,loc='center left', bbox_to_anchor=(1, 0.5),fancybox=True)
    plt.show()