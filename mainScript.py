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
MENU LAYER 0 - Main menu
-----------------------------
"""
welcome = "\n============================\nWelcome!\n============================\n"
print(welcome.center(80))
mainMenu = np.array(["Load data","Aggregate data", "Display statistics", "Visualize electricity consumption", "Quit"]) #define options
while True:
    for i in range(len(mainMenu)):
        print("{:d}. {:s}".format(i+1, mainMenu[i])) #print options menu
        choice = 0
    while not(np.any(choice == np.arange(len(mainMenu))+1)):
        try:
            choice = float(input("Please choose the number of a menu item: ")) #Choose in the menu. 
        except ValueError:
            print("Wow there, cowboy! Please select a valid option from the menu.") #error message for invalid input
            choice = 0
    """
    -----------------------------
    MENU LAYER 1 - Choose file name
    -----------------------------
    """
    if choice == 1: #define the filename you want to input and load the data
        while choice == 1:
            try:
                filename = str(raw_input("\nPlease enter the name of the file you want to load: ")) #input filename
                fileBool = True
            except NameError:
                print("\nThe file is not found. Please check if your typed correctly or if the file exists in the folder.\n*TIP* Remember the extention '.csv' when writing the filename")
                fileBool = False
            """
            -----------------------------
            MENU LAYER 2 - fmode Menu
            -----------------------------
            """
            if fileBool == True:
                while True:
                    fmodeMenu = np.array(["Forward fill", "Backward fill", "Drop", "Return to main menu"])
                    for i in range(len(fmodeMenu)):
                        print("{:d}. {:s}".format(i+1, fmodeMenu[i])) #print the fmode menu
                    try:
                        fmodeOption = int(input("\nPlease specify the method of treatment for corrupted measurements: ")) #input fmode
                        fmode_index = np.arange(len(fmodeMenu)-1)+1
                        if np.any(fmode_index == fmodeOption): #if the user chooses one of the fmode options, execute that command
                            fmode = fmodeMenu[(fmodeOption-1)]
                            print(fmode + "\n")
                            #load_measurement(filename, fmode)
                            #databackup = np.copy(data)
                            #tvecbackup = np.copy(tvec)
                            choice = -1
                            break
                        elif fmodeOption == len(fmodeMenu): #if the user chooses Return, break the while loop
                            choice = -1
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("\nERROR DETECTED!\nPlease select a valid option from the menu.")
                    #except FileNotFoundError:
                        #print("\nIt does not lookj like your file is present in the folder, chap.\nEither you did a typo or the file is not in your folder...\n*TIP* Remember the '.csv' extenstion of your filename.")
            else:
                pass
        """
        -----------------------------
        MENU LAYER 1 - Aggregate Data
        -----------------------------
        """
    elif choice == 2: 
        pass #do something
        """
        -----------------------------
        MENU LAYER 1 - Choose file name
        -----------------------------
        """
    elif choice == 3:
        #do something else
        pass
        """
        -----------------------------
        MENU LAYER 1 - Visualize electricity consumption
        -----------------------------
        """
    elif choice == 4:
        #do something entirely different
        pass
    elif choice == 5: #Exit script
        byebye = "\n============================\nHasta la Vista, baby\n============================"
        print(byebye.center(80))
        break