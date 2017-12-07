# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:19:58 2017

@author:
"""
import math
import numpy as np
import pandas as pd
import time
import os.path
from load_measurements import *
from print_statistics import *   
from dataPlot import *
from aggregate_measurements import * 

#start mainscript
"""
-----------------------------------------
MENU LAYER 0 - Open main menu
-----------------------------------------
"""
welcome = "\n============================\nWelcome!\n============================\n"
print(welcome.center(80))
menuBool = False #checks if data is loaded
aggBool = False #checks which aggregation is active
mainMenu = np.array(["Load data",
                     "Aggregate data",
                     "Display statistics",
                     "Visualize electricity consumption",
                     "Show raw data",
                     "Clear Aggregation",
                     "Quit"]) #define options
while True:
    print("============================\nMain Menu Info\n") #print main menu info
    if menuBool == True: #print details about the loaded file and data
        print("File named '" + filename + "' is loaded")
        print("Data is loaded with fmode: '" + fmode + "'!")
    else:
        print("No data is loaded")
    if aggBool == True:
        print("Active Aggregation: '" + period + "'") #prints details about aggregation
    else:
        pass
    print("============================")
    counter = 0 #counts the number of loops done by a specific while loop
    for i in range(len(mainMenu)):
        print("{:d}. {:s}".format(i+1, mainMenu[i])) #print options menu
        choice = 0
    while not(np.any(choice == np.arange(len(mainMenu))+1)):
        try:
            choice = math.floor(float(input("Please choose the number from the menu item: "))) #Choose in the menu. 
            if (choice <= 0) or (choice > len(mainMenu)):
                raise ValueError #raise a value error if input is negative
            else:
                pass
        except ValueError:
            print("Wow there, cowboy! Please select a valid option from the menu.") #error message for invalid input
            choice = 0
        except SyntaxError:
            print("Please give me an input...")
            choice = 0
        except NameError:
            print("Wow there, cowboy! Please select a valid option from the menu.")
    
    """
    -----------------------------------------
    MENU LAYER 1 - Choose file name
    -----------------------------------------
    """
    if choice == 1: #define the filename you want to input and load the data
        while choice == 1:
            counter = counter + 1 #count how many attempts the user has done to load data
            if counter > 2:
                print("*TIP* You can return to the main menu by writing 'return'.") #tell the user, after 2 attempts, that they can choose to leave the menu by writing 'return'
            filename = str(input("\nPlease enter the name of the file you want to load: ")) #input filename
            
            if os.path.isfile(filename): #checks whether the file exists
                if filename.endswith(".csv"): #checks whether the file has '.csv' extension
                    fileBool = True #a variable that tells whether the file exists
                else:
                    print("\nERROR DETECTED! Only '.csv'-files can be loaded")
                    fileBool = False
                
            elif filename.lower() == "return":
                break
            else:
                fileBool = False
                print("\nThat file is invalid. Please try again!\n*TIP* Remember the '.csv' extenstion in your filename!")
            """
            -----------------------------------------
            MENU LAYER 2 - fmode Menu
            -----------------------------------------
            """
            if fileBool == True:
                fmodeMenu = np.array(["Forward fill",
                                      "Backward fill",
                                      "Drop",
                                      "Return to main menu"])
                print("")
                for i in range(len(fmodeMenu)):
                    print("{:d}. {:s}".format(i+1, fmodeMenu[i])) #print the fmode menu
                while True:
                    try:
                        fmodeOption = int(input("Please specify the number corresponding to the method of treatment for corrupted measurements: ")) #user input for fmode
                        if choice < 0:
                            raise ValueError #raise a value error if input is negative
                        else:
                            pass
                        fmode_index = np.arange(len(fmodeMenu)-1)+1 #Make an index of the fmode options excluding 'Return to menu'
                        if np.any(fmode_index == fmodeOption): #if the user chooses one of the fmode options, execute that command
                            fmode = fmodeMenu[(fmodeOption-1)] #the chosen fmode 
                            
                            start = time.time() #make a timestamp before loading data
                            print("\n============================\nfmode: '" + fmode + "':\nOm Nom Nom...\n")
                            outputLoad = load_measurements(filename, fmode)
                            data = outputLoad[1] #raw data as numpy 4 by x matrix
                            tvec = outputLoad[0] #raw time vector as numpy 6 by x matrix
                            stop = time.time() - start #calculate loadtime
                            
                            print("Data file loaded!\nLoad time: {:f} seconds.\n============================\n".format(stop)) #write loading time
                            aggBool = False #when loading new data, the aggregation is automatically cleared (obviously)
                            tvecbackup = tvec.copy() #create backups for reset option
                            databackup = data.copy() #same
                            choice = -1
                            menuBool = True #a boolean that varifies that data has been loaded
                            imSure = False #checks if you are certain you want to plot big data
                            break
                       
                        elif fmodeOption == len(fmodeMenu): #if the user chooses Return, break the while loop
                            choice = -1
                            break
                        else:
                            raise ValueError
                            
                    except ValueError:
                        print("\nERROR DETECTED! Please select a valid option from the menu.\n")
                    except SyntaxError:
                        print("\nERROR DETECTED! There is an issue with the SYNTAX!\nPlease use letters in the english alphabet\n")
                    except NameError:
                        print("\nERROR DETECTED! The option you chose is invalid.")
            else:
                pass
        
        """
        -----------------------------------------
        MENU LAYER 1 - Aggregate Data
        -----------------------------------------
        """
    elif choice == 2:
        if menuBool == True:
            
            """
            -----------------------------------------
            MENU LAYER 2 - Aggregation Menu
            -----------------------------------------
            """
            aggModeMenu = np.array(["Hourly consumption",
                                    "Daily consumption",
                                    "Monthly consumption",
                                    "Average hourly consumption",
                                    "Average daily consumption",
                                    "Return to main menu"]) #array for menu
            aggPeriod = np.array(["hour",
                                  "day",
                                  "month",
                                  "hour of the day",
                                  "average daily consumption"]) #an array for period input
            while True:
                for i in range(len(aggModeMenu)):
                    print("{:d}. {:s}".format(i+1,
                          aggModeMenu[i])) #print the fmode menu
                try:
                    aggModeInput = int(input("Please specify the number corresponding to the type of aggregation: ")) #user input for fmode
                    if choice < 0:
                        raise ValueError #raise a value error if input is negative
                    else:
                        pass
                    
                    agg_index = np.arange(len(aggModeMenu)-1)+1 #index for the aggModeMenu excluding 'Return to menu'
                    if np.any(aggModeInput == agg_index):
                        
                        if aggBool == True: #if you already have an active aggregation, this aggregation is cleared, and the other one is applied
                            data = databackup
                            tvec = tvecbackup
                        else:
                            pass
                        period = aggPeriod[aggModeInput-1] #period is defined from aggPeriod array
                        aggBool = True #aggBool is now said to be active
                        aggOutPut = aggregate_measurements(tvec,data,period) #access aggregation subscribt
                        data = aggOutPut[1]
                        tvec = aggOutPut[0]
                        imSure = False #checks if you are certain you want to plot big data
                        break
                    
                    elif aggModeInput == len(aggModeMenu): #go back to mainmenu
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("\nERROR DETECTED! Please select a valid option from the menu.\n")
 
        else:
            print("\nPlease load data first!\n")
            pass
        
        """
        ------------------------------------------
        MENU LAYER 1 - Show statistics
        -----------------------------------------
        """
    elif choice == 3:
        if menuBool == True:
            print_statistics(data) #printing the statistics table
        else:
            print("\nPlease load data first!\n")
            pass
        
        """
        -----------------------------------------
        MENU LAYER 1 - Visualize electricity consumption
        -----------------------------------------
        """
    elif choice == 4:
        if menuBool == True:
            if imSure == True: #if you're already made it clear that you are sure, pass by this menu
                pass
            elif aggBool == True: #if there is aggrigated data, or the data sample is relatively small, just plot data
                imSure = True #boolean that checks whether you are sure you want to plot the data
            elif len(data) < 100000:
                imSure = True
            else: #else ask the user if he/she is sure he/she want to plot the data
                print("\nWARNING: Data sample is large! Data will probably take a while to plot.\n")
                while True:
                    areYouSure = np.array(["Yes",
                                           "No"]) #Ask the user if he/she is sure that if he/she wants to print the non-aggrigated data
                    print("Are you sure you want to plot the data anyway?\n")
                    for i in range(len(areYouSure)):
                        print("{:d}. {:s}".format(i+1,
                              areYouSure[i])) #print 'Are you sure' menu
                    print("")
                    
                    try: #get input from user
                        aYSchoice = int(input("Please pick a number corresponding to your choice: ")) #user input for whether they want to continue plotting non-aggrigated data
                        if aYSchoice < 0:
                            raise ValueError
                        else:
                            pass
                            if aYSchoice == 1:
                               imSure = True #boolean that checks whether you are sure you want to plot the data
                               break
                            elif aYSchoice == 2:
                                imSure = False #boolean that checks whether you are sure you want to plot the data
                                break
                            else:
                                print("\nThat option number is not valid!")
                    except ValueError:
                        print("\nThat option number is not valid!")
               
            """
            -----------------------------------------
            MENU LAYER 2 - Visualization menu
            -----------------------------------------
            """
            while imSure == True: #Only runs if you are sure you want to plot the data
                vOptArr = np.array(["Each zones seperately", "All zones combined", "Back to main menu"])
                print("")
                for i in range(len(vOptArr)):
                    print("{:d}. {:s}".format(i+1,
                          vOptArr[i])) #print visualization menu
                
                try: #get input from user
                    vOption = int(input("Please select the number corresponding to your desired visualization: "))
                    if vOption < 0:
                        raise ValueError
                    else:
                        pass
                    if aggBool == False: #check whether there is an aggregation
                        period = "minute"
                    else:
                        pass
                    if vOption == 1: #plot zones seperately
                        plotType = 1 #specifies if the plot is for the zones seperately or combined
                        dataPlot(data,period,plotType) #use dataPlot subscript to plot the data
                        print("")
                    elif vOption == 2: #plot the zones combined
                        plotType = 2 
                        dataSum = np.sum(data,axis=1) #summing the data
                        dataPlot(dataSum,period,plotType) #use dataPlot subscript to plot the data
                        print("")
                    elif vOption == 3: #go to main menu
                        break
                    else:
                        print("\nThat option number is not valid!")
                except ValueError:
                    print("\nThat option number is not valid!")                 
        else:
            print("\nPlease load data first!\n")
            pass
            
        """
        -----------------------------------------
        MENU LAYER 1 - Show raw data files
        -----------------------------------------
        """
    elif choice == 5:
        if menuBool == True and aggBool== True: #prints raw data, if any is loaded
            print("\n============================\nRaw Data\n============================\n")
            print(data)
        elif menuBool==True:
            print("\n============================\nRaw Data\n============================\n")
            print(data)
            print("\n============================\nRaw Time Vector\n============================\n")
            print(tvec)
            print("")
        else:
            print("\nPlease load data first!\n")
        
        
        """
        -----------------------------
        MENU LAYER 1 - Clear Aggregation
        -----------------------------
        """
    elif choice == 6:
        if menuBool == True:
            data = databackup #define the data as the backup data
            tvec = tvecbackup 
            aggBool = False #aggregation is now unapplied
            imSure = False #checks if you are certain you want to plot big data
            print("\nAggregation is cleared!\n")
        else:
            print("\nThere is no data. Please load data first!\n")
            pass
    elif choice == 7: #Exit script
        byebye = "\n============================\nHasta la Vista, baby\n============================"
        print(byebye.center(80))
        time.sleep(1)
        break
    