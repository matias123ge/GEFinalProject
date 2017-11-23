# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:19:58 2017

@author: s174435
"""

import numpy as np
import pandas as pd
import time
import copy
#from load_measurement import *

#start mainscript
"""
-----------------------------
MENU LAYER 0
-----------------------------
"""
welcome = "\n============================\nWelcome!\n============================"
print(welcome.center(80))
mainMenu = np.array(["Load data","Aggregate data", "Display statistics", "Visualize electricity consumption", "Quit"]) #define options
while True:
    for i in range(len(mainMenu)):
        print("{:d}. {:s}".format(i+1, mainMenu[i])) #print options menu
        choice = 0
    while not(np.any(choice == np.arange(len(mainMenu))+1)):
        try:
            choice = float(input("Please choose a menu item: ")) #Choose in the menu. 
            print("========================================================")
        except ValueError:
            print("Wow there, cowboy! Please select a valid option from the menu.") #error message for invalid input
            choice = 0
    """
    -----------------------------
    MENU LAYER 1
    -----------------------------
    """
    if choice == 1: #define the filename you want to input and load the data
        while choice == 1:
            try:
                filename = str(input("\nPlease enter the name of the file you want to load: ")) #input filename
                fileBool = True
            except NameError:
                print("\nThe file is not found. Please check if your typed correctly or if the file exists in the folder.\n*TIP* Remember the extention '.csv' when writing the filename")
                fileBool = False
        """
        -----------------------------
        MENU LAYER 2
        -----------------------------
        """
            if fileBool == True:
                fmodeMenu = np.array(["Forward fill", "Backward fill", "Drop", "Return"])
                for i in range(len(fmodeMenu)):
                    print("{:d}. {:s}".format(i+1, fmodeMenu[i])) #print the fmode menu
                try:
                    fmodeOption = (input("\nPlease specify the method of treatment for corrupted measurements: ")) #input fmode
                    if fmodeOption == np.any(np.arange(len(fmodeMenu)-1)+1): #if the user chooses one of the fmode options, execute that command
                        fmode = fmodeMenu[fmodeOption]
                        print(fmode)
                        #load_measurement(filename, fmode)
                        #databackup = np.copy(data)
                        #tvecbackup = np.copy(tvec)
                        break
                    elif fmodeOption == len(fmodeMenu): #if the user chooses Return, break the while loop
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("ERROR DETECTED!\nPlease select a valid option from the menu.")
                except NameError:
                    print("Please write an integer corresponding to an option in the menu.")
            else:
                pass