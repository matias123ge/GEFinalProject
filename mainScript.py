# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:19:58 2017

@author: s174435
"""

import numpy as np
import pandas as pd
import time
import os.path
from load_measurements import *
from print_statistics import *   
from dataPlot import * 

#start mainscript
"""
-----------------------------
MENU LAYER 0 - Open main menu
-----------------------------
"""
welcome = "\n============================\nWelcome!\n============================\n"
print(welcome.center(80))
menuBool = False #checks if data is loaded
aggBool = False #checks which aggregation is active

mainMenu = np.array(["Load data","Aggregate data", "Display statistics", "Visualize electricity consumption", "Show raw files", "Reset data", "Quit"]) #define options
while True:
    for i in range(len(mainMenu)):
        print("{:d}. {:s}".format(i+1, mainMenu[i])) #print options menu
        choice = 0
    while not(np.any(choice == np.arange(len(mainMenu))+1)):
        try:
            choice = float(input("Please choose the number from the menu item: ")) #Choose in the menu. 
            if (choice < 0) or (choice > len(mainMenu)):
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
    -----------------------------
    MENU LAYER 1 - Choose file name
    -----------------------------
    """
    if choice == 1: #define the filename you want to input and load the data
        while choice == 1:
            filename = str(input("Please enter the name of the file you want to load: ")) #input filename
            
            if os.path.isfile(filename): #determine whether the file exists
                fileBool = True #a variable that tells whether the file exists
            elif filename.lower() == "return":
                break
            else:
                fileBool = False
                print("\nThat file is invalid. Please try again!\nYou can also return to the main menu simply by typing 'return'.\n \n*TIP* Remember the '.csv' extenstion in your filename!\n")
            """
            -----------------------------
            MENU LAYER 2 - fmode Menu
            -----------------------------
            """
            if fileBool == True:
                while True:
                    fmodeMenu = np.array(["Forward fill", "Backward fill", "Drop", "Return to main menu"])
                    print("")
                    for i in range(len(fmodeMenu)):
                        print("{:d}. {:s}".format(i+1, fmodeMenu[i])) #print the fmode menu
                    try:
                        fmodeOption = int(input("Please specify the number corresponding to the method of treatment for corrupted measurements: ")) #user input for fmode
                        if choice < 0:
                            raise ValueError #raise a value error if input is negative
                        else:
                            pass
                        fmode_index = np.arange(len(fmodeMenu)-1)+1 #Make an index of the fmode options
                        if np.any(fmode_index == fmodeOption): #if the user chooses one of the fmode options, execute that command
                            fmode = fmodeMenu[(fmodeOption-1)] #the chosen fmode 
                            
                            start = time.time() #make a timestamp before loading data
                            print("\n============================\nfmode: '" + fmode + "':\nOm Nom Nom...\n")
                            outputLoad = load_measurements(filename, fmode)
                            data = outputLoad[1] #raw data as numpy 4 by x matrix
                            tvec = outputLoad[0] #raw time vector as numpy 6 by x matrix
                            stop = time.time() - start #calculate loadtime
                            
                            print("Data file loaded!\nLoad time: {:f} seconds.\n============================\n".format(stop)) #write loading time
                            tvecbackup = np.copy(tvec) #create backups for reset option
                            databackup = np.copy(data) #same
                            choice = -1
                            menuBool = True #a boolean that varifies that data has been loaded
                            break
                       
                        elif fmodeOption == len(fmodeMenu): #if the user chooses Return, break the while loop
                            choice = -1
                            break
                        else:
                            raise ValueError
                            
                    except ValueError:
                        print("\nERROR DETECTED!\nPlease select a valid option from the menu.")
                    except SyntaxError:
                        print("\nERROR DETECTED!\nThere is an issue with the SYNTAX!\nPlease use letters in the english alphabet\n")
                    except NameError:
                        print("\nERROR DETECTED!\nThe option you chose is invalid.")
            else:
                pass
        
        """
        -----------------------------
        MENU LAYER 1 - Aggregate Data
        -----------------------------
        """
    elif choice == 2:
        if menuBool == True:
            print("Passed.")
            #do something
        else:
            print("\nPlease load data first!\n")
            pass
        
        """
        -----------------------------
        MENU LAYER 1 - Show statistics
        -----------------------------
        """
    elif choice == 3:
        if menuBool == True:
            print_statistics(data) #printing the statistics table
        else:
            print("\nPlease load data first!\n")
            pass
        
        """
        -----------------------------
        MENU LAYER 1 - Visualize electricity consumption
        -----------------------------
        """
    elif choice == 4:
        if menuBool == True:
            if aggBool == True: #if there is aggrigated data, or the data sample is relatively small, just plot data
                imSure = True #boolean that checks whether you are sure you want to plot the data
            elif len(data) < 100000:
                imSure = True
            else: #else ask the user if he/she is sure he/she want to plot the data
                while True:
                    areYouSure = np.array(["Yes","No"]) #Ask the user if he/she is sure that if he/she wants to print the non-aggrigated data
                    print("\nWARNING: Data sample is large!\nData will probably take a while to plot. Are you sure you want to plot the data anyway?\n")
                    for i in range(len(areYouSure)):
                        print("{:d}. {:s}".format(i+1, areYouSure[i])) #print 'Are you sure' menu
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
            -----------------------------
            MENU LAYER 2 - Visualization menu
            -----------------------------
            """
            while imSure == True: #Only runs if you are sure you want to plot the data
                vOptArr = np.array(["Each zones seperately", "All zones combined", "Back to main menu"])
                print("")
                for i in range(len(vOptArr)):
                    print("{:d}. {:s}".format(i+1, vOptArr[i])) #print visualization menu
                
                try: #get input from user
                    vOption = int(input("Please select the number corresponding to your desired visualization: "))
                    if vOption < 0:
                        raise ValueError
                    else:
                        pass
                    
                    if vOption == 1: #plot zones seperately
                        period = "Minute" #temp until aggregate works
                        plotType = 1 #specifies if the plot is for the zones seperately or combined
                        dataPlot(data,period,plotType) #use dataPlot subscript to plot the data
                        print("")
                    elif vOption == 2: #plot the zones combined
                        period = "Minute" #temp until aggregate works
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
        -----------------------------
        MENU LAYER 1 - Show raw data files
        -----------------------------
        """
    elif choice == 5:
        if menuBool == True:
            print("\n============================\nRaw Data\n============================\n")
            print(data)
            print("\n============================\nRaw Time Vector\n============================\n")
            print(tvec)
            print("")
        else:
            print("\nPlease load data first!\n")
            pass
        
        """
        -----------------------------
        MENU LAYER 1 - Reset data
        -----------------------------
        """
    elif choice == 6:
        if menuBool == True:
            data = databackup #define the data as the backup data
            tvec = tvecbackup 
            print("\nData is reset!\n")
            #do something
        else:
            print("\nThere is no data to reset. Please load data first!\n")
            pass
    elif choice == 7: #Exit script
        byebye = "\n============================\nHasta la Vista, baby\n============================"
        print(byebye.center(80))
        time.sleep(1)
        break