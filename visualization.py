# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 22:00:10 2017

"""
import matplotlib.pyplot as plt
#from matplotlib.dates import date2num
import numpy as np
import copy
#import datetime

def dataPlot(data,tvec,vOption,aggBool):
    #determine the order of the plot
    plotData = copy.copy(data)
    listMonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    zones = ["Zone 1", "Zone 2", "Zone 3", "Zone 4"]
    if len(plotData) < 25: #check if no. of measurements < 25
        #do barplot
        if vOption == 1: #Each zone seperately
            x = np.array([])
            for i in range (len(data)):
                x = np.hstack((x,datetime.datetime(int(tvecbackup[i,0]),int(tvecbackup[i,1]),int(tvecbackup[i,2]),int(tvecbackup[i,3]),int(tvecbackup[i,4]),int(tvecbackup[i,5]))))
            x = x.tolist()
            x_time = date2num(x)
            yZone1 = plotData[:,0]
            yZone2 = plotData[:,1]
            yZone3 = plotData[:,2]
            yZone4 = plotData[:,3]
            ax = plt.subplot(111)
            ax.xaxis_date()
            w = 0.1
            ax.bar(x-w, y,width=w,color='b',align='center')
            ax.bar(x, z,width=w,color='g',align='center')
            ax.bar(x+w, k,width=w,color='r',align='center')
            ax.autoscale(tight=True)
            
            plt.show()
       
        #tvecMultiplicationFactor = [0, 60*24*30, 60*24, 60, 1, 1/60] #factor to calculate how many minues there are in the given dataset
        x = np.sum(np.multiply(tvecMultiplicationFactor, tvec),axis=1)
        x_adjust = x - x[0]
        plt.bar(x_adjust, y, align="center", alpha = 0.5)
        plt.xticks(x_adjust,zones)
        plt.ylabel("Energy Consumption (in kWh)")
        plt.title("Power Consumption Per Minute")
        plt.show()
    else:
        #tvecMultiplicationFactor = [0, 60*24*30, 60*24, 60, 1, 1/60] #factor to calculate how many minues there are in the given dataset
        x = date2num
        #x = np.sum(np.multiply(tvecMultiplicationFactor, tvec),axis=1)
        x_adjust = x - x[0]
        #define y-values
        yZone1 = plotData[:,0]
        yZone2 = plotData[:,1]
        yZone3 = plotData[:,2]
        yZone4 = plotData[:,3]
        #define lines
        plt.plot(x_adjust,yZone1,"red")
        plt.plot(x_adjust,yZone2,"blue")
        plt.plot(x_adjust,yZone3,"green")
        plt.plot(x_adjust,yZone4,"black")
        
        plt.title("Power Consumption Per Minute") #line diagram title
        plt.xlabel("Minutes") #x-label
        plt.ylabel("Energy Consumption (in kWh)") #y-label
        plt.xlim([x_adjust[0],x_adjust[max(x_adjust)]]) #limits in the x-direction
        plt.ylim([0,plotData.max() + plotData.mean()]) #limit in the y-direction
        legends = np.array(["Zone 1", "Zone 2", "Zone 3", "Zone 4"])
        plt.legend(legends,loc='center left', bbox_to_anchor=(1, 0.5),fancybox=True)
        #plt.legend(["Salmonella Enterica", "Bacillus Cereus", "Listeria", "Brochothrix Thermosphacta"],loc='center left', bbox_to_anchor=(1, 0.5),fancybox=True) #legend specifications
        plt.show()
        #print line diagram
        #print pie diagram
    
    
    
    if aggBool == 1: #no aggregation is active
        if vOption == 1: #Each zone seperately
            if len(plotData) < 25: #check if no. of measurements < 25
                y = np.array([]) #Count the number of occurrences of each integer in 3rd column of the data matrix
                #tvecMultiplicationFactor = [0, 60*24*30, 60*24, 60, 1, 1/60] #factor to calculate how many minues there are in the given dataset
                x = np.sum(np.multiply(tvecMultiplicationFactor, tvec),axis=1)
                x_adjust = x - x[0]
                plt.bar(x_adjust, y, align="center", alpha = 0.5)
                plt.xticks(x_adjust,zones)
                plt.ylabel("Energy Consumption (in kWh)")
                plt.title("Power Consumption Per Minute")
                plt.show()
            else:
                #tvecMultiplicationFactor = [0, 60*24*30, 60*24, 60, 1, 1/60] #factor to calculate how many minues there are in the given dataset
                x = date2num
                #x = np.sum(np.multiply(tvecMultiplicationFactor, tvec),axis=1)
                x_adjust = x - x[0]
                #define y-values
                yZone1 = plotData[:,0]
                yZone2 = plotData[:,1]
                yZone3 = plotData[:,2]
                yZone4 = plotData[:,3]
                #define lines
                plt.plot(x_adjust,yZone1,"red")
                plt.plot(x_adjust,yZone2,"blue")
                plt.plot(x_adjust,yZone3,"green")
                plt.plot(x_adjust,yZone4,"black")
                
                plt.title("Power Consumption Per Minute") #line diagram title
                plt.xlabel("Minutes") #x-label
                plt.ylabel("Energy Consumption (in kWh)") #y-label
                plt.xlim([x_adjust[0],x_adjust[max(x_adjust)]]) #limits in the x-direction
                plt.ylim([0,plotData.max() + plotData.mean()]) #limit in the y-direction
                legends = np.array(["Zone 1", "Zone 2", "Zone 3", "Zone 4"])
                plt.legend(legends,loc='center left', bbox_to_anchor=(1, 0.5),fancybox=True)
                #plt.legend(["Salmonella Enterica", "Bacillus Cereus", "Listeria", "Brochothrix Thermosphacta"],loc='center left', bbox_to_anchor=(1, 0.5),fancybox=True) #legend specifications
                plt.show()
                #print line diagram
                #print pie diagram
        elif vOption == 2:
            plt.title("Power Consumption Per Minute") #line diagram title
            plt.xlabel("Minutes") #x-label
            plt.ylabel("Electrical Energy (in kWh)") #y-label
            plt.xlim([x_adjust[0],x_adjust[max(x_adjust)]]) #limits in the x-direction
            plt.ylim([0,plotData.max() + plotData.mean()]) #limit in the y-direction
            legends = np.array(["Zone 1", "Zone 2", "Zone 3", "Zone 4"])
            plt.legend(legends,loc='center left', bbox_to_anchor=(1, 0.5),fancybox=True)
            #plt.legend(["Salmonella Enterica", "Bacillus Cereus", "Listeria", "Brochothrix Thermosphacta"],loc='center left', bbox_to_anchor=(1, 0.5),fancybox=True) #legend specifications
            plt.show()
                dataSum = np.sum(data, axis=1) #array with the sum of all data-rows
            #dataSum = dataSum[np.lexsort((dataSum, ))]
   
    
    
    if aggBool == 1:
        print("")
        #Minutely consumption
    elif aggBool == 2:
        print("")
        #Hourly consumption is active
    elif aggBool == 3:
        print("")
        #Daily consumption is active
    elif aggBool == 4:
        print("")
        #Monthly consumption is active
    elif aggBool == 5:
        print("")
        #Hour-of-day consumption is active
    
    if vOption == 1:
        print("")
        #Each zone seperately
    elif vOption == 2:
        dataSum = np.sum(data, axis=1) #array with the sum of all data-rows
        #dataSum = dataSum[np.lexsort((dataSum, ))]
        
        
    
    if len(plotData) < 25:
        for i in range(len(data)):
            y = np.array([]) #Count the number of occurrences of each integer in 3rd column of the data matrix
        bacteria = np.array(["Salmonella E.","Bacillus Cereus","Listeria","Brochothrix T."])
        x_pos = np.arange(len(bacteria)) #Define an array that shows the location in the x-direction for the different species
        plt.bar(x_pos, y, align="center", alpha = 0.5)
        plt.xticks(x_pos,bacteria)
        plt.ylabel("Number of occurences")
        plt.title("Plot of occurrences of different bacteria")
        plt.show()
    else:
        print("")
        #print line diagram
        #print pie diagram