# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 
import pandas as pd
import time
def load_measurements(filename, fmode):
    fmode = fmode.lower()
    matrix=pd.read_csv(filename, header=None)
    matrix=np.array(matrix)        
    errormatrix=np.where(matrix==-1)
    x=errormatrix[0]
    y=errormatrix[1]
    if fmode=="forward fill":
        if np.any(matrix[0,:]==-1):
            matrix=np.delete(matrix,errormatrix[0],axis=0)
            print("First data input was corrupt, all corrupt inputs have been deleted.")
            pass
        else:
            for i in range (len(x)):
                matrix[x[i],y[i]]=matrix[x[i]-1,y[i]]
            
    elif fmode=="backward fill" :
        if np.any(matrix[len(matrix)-1,:]==-1): 
            matrix=np.delete(matrix,errormatrix[0],axis=0)
            print("First data input was corrupt, all corrupt inputs have been deleted.")
            pass
        else:
            for i in range (len(x)):
                matrix[x[i],y[i]]=matrix[x[i]+1,y[i]]
    elif fmode=="drop":
        matrix=np.delete(matrix,errormatrix[0],axis=0)
    #split tvec into NX6 tvec matrix and NX4 
    tvec=matrix[:,[0,1,2,3,4,5]]
    data=matrix[:,[6,7,8,9]]
    return (tvec, data)