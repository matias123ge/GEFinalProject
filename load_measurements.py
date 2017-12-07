# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 
import pandas as pd

#function to load data from csv file, and converting to numpy.array, filtering corrupted lines.
def load_measurements(filename, fmode):
    """
    Loads data from .csv-files.
    
    INPUT:
        filename as type(str),
        fmode as type(str)
    
    OUTPUT:
        'data' as pd.dataFrame
        'tvec' as pd.dataFrame
    """
    fmode = fmode.lower() #makes sure you can input "fmode" in both upper and lower case, in the mainScript
    matrix=pd.read_csv(filename, header=None) #read the csv file, and makes sure the first data row is not used as header for the DataFrame
    matrix=np.array(matrix) #convert to numpy array   
    errormatrix=np.where(matrix==-1) #tuple with two arrays, two indicate where the elements are corrupted
    x=errormatrix[0] #splitting errormatrix, for use in forloop
    y=errormatrix[1] #splitting errormatrix, for use in forloop
    
    if fmode=="forward fill": #filters data appropriately, if fmode="forward fill"
        if np.any(matrix[0,:]==-1):#checks if the first row contains any corrupted elements
            matrix=np.delete(matrix,errormatrix[0],axis=0)  #if so, deletes all rows with corrupted elements
            print("First data input was corrupt, all corrupt inputs have been deleted.")
            pass
        else:
            for i in range (len(x)):
                #replaces corrupted values ("-1") with the last valid value from the same column
                matrix[x[i],y[i]]=matrix[x[i]-1,y[i]]
            
    elif fmode=="backward fill" : #filters data appropriately, if fmode="backward fill"
        #Flip matrix, do forwards fill
        #Check for 1st value if -1
        matrix=np.flipud(matrix)
        errormatrix=np.where(matrix==-1)
        x=errormatrix[0] #splitting errormatrix, for use in forloop
        y=errormatrix[1]
        if np.any(matrix[0,:]==-1):#checks if the first row contains any corrupted elements
            matrix=np.delete(matrix,errormatrix[0],axis=0)  #if so, deletes all rows with corrupted elements
            print("First data input was corrupt, all corrupt inputs have been deleted.")
            pass
        else:
            for i in range (len(x)):
                #replaces corrupted values ("-1") with the last valid value from the same column
                matrix[x[i],y[i]]=matrix[x[i]-1,y[i]]
        #Flips the matrix back to original position
        matrix=np.flipud(matrix)
        #matrix = flipped matrix
    elif fmode=="drop": #filter appropriately, if fmode="drop"
        matrix=np.delete(matrix,errormatrix[0],axis=0) #deletes all rows with corrupted elements
        
    #split tvec into Nx6 tvec matrix and Nx4 
    tvec=matrix[:,[0,1,2,3,4,5]]
    data=matrix[:,[6,7,8,9]]
    header=np.array(["Year","Month","Day","Hour","Minute","Seconds"])
    header1=np.array(["Zone1","Zone2","Zone3","Zone4"])
    tvec=pd.DataFrame(tvec, columns=header)
    data=pd.DataFrame(data, columns=header1)
    return (tvec, data)