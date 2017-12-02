# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 18:03:08 2017

@author: s174438
"""

import numpy as np 
import pandas as pd
#Convert tvec and data back to panda dataframe for easier processing:
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
        hour:
        sortedcomplete=pd.DataFrame.sort(complete(ascending=[3,:]))
    