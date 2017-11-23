# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:19:58 2017

@author: s174435
"""

import numpy as np
import pandas as pd
import time
import copy
import os.path
from load_measurements import *
    
#start mainscript
"""
-----------------------------
MENU LAYER 0 - Main menu
-----------------------------
"""
welcome = "\n============================\nWelcome!\n============================\n"
print(welcome.center(80))
menuBool = False #make the user unable to do a function without loading data
mainMenu = np.array(["Load data","Aggregate data", "Display statistics", "Visualize electricity consumption", "Show raw files", "Reset data", "Quit"]) #define options
while True:
    for i in range(len(mainMenu)):
        print("{:d}. {:s}".format(i+1, mainMenu[i])) #print options menu
        choice = 0
    while not(np.any(choice == np.arange(len(mainMenu))+1)):
        try:
            choice = float(input("Please choose the number of a menu item: ")) #Choose in the menu. 
            if choice < 0:
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
            filename = str(input("\nPlease enter the name of the file you want to load: ")) #input filename
            if os.path.isfile(filename):
                fileBool = True
            elif filename.lower() == "return":
                break
            else:
                fileBool = False
                print("\nThat file is invalid. Please try again!\nYou can also return to the main menu simply by typing 'return'.\n \n*TIP* Remember the '.csv' extenstion in your filename!")
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
                        fmodeOption = int(input("\nPlease specify the number corresponding to the method of treatment for corrupted measurements: ")) #input fmode
                        if choice < 0:
                            raise ValueError #raise a value error if input is negative
                        else:
                            pass
                        fmode_index = np.arange(len(fmodeMenu)-1)+1
                        if np.any(fmode_index == fmodeOption): #if the user chooses one of the fmode options, execute that command
                            fmode = fmodeMenu[(fmodeOption-1)]
                            start = time.time() #make a timestamp before loading data
                            print("\n============================\nfmode: '" + fmode + "':\nOm Nom Nom...\n")
                            outputLoad = load_measurements(filename, fmode)
                            stop = time.time() - start #calculate loadtime
                            print("Data file loaded!\nLoad time: {:f} seconds.\n============================\n".format(stop)) #write loading time
                            databackup = np.copy(outputLoad[0])
                            tvecbackup = np.copy(outputLoad[1])
                            choice = -1
                            menuBool = True
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
        MENU LAYER 1 - Choose file name
        -----------------------------
        """
    elif choice == 3:
        if menuBool == True:
            print("Passed.")
            #do something else
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
            print("Passed.")
            #do something entirely differnet
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
            print("Passed.")
            #do somehting
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
            data = databackup
            tvec = tvecbackup
            print("\nData is reset!\n")
            #do somehting
        else:
            print("\nThere is no data to reset. Please load data first!\n")
            pass
    elif choice == 7: #Exit script
        byebye = "\n============================\nHasta la Vista, baby\n============================"
        print(byebye.center(80))
        break