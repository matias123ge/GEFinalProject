# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 22:31:10 2017

@author: Aimas
"""

def textLibs():
    file1 = open("ErrorLib.txt","r") #opens and reads the dictionary txt files
    errorFile = file1.readlines()
    file1.close()
    file2 = open("OtherLib.txt","r")
    otherFile = file2.readlines()
    file2.close()
    lib1 = {} #making an empty dictionary
    for i in range(len(errorFile)): #filling the error dictionary with the lines from the txt file
        lib1["Error{0}".format(i)] = errorFile[i]
    lib2 = {} #same, just with 'other' types of messages
    for i in range(len(otherFile)):
        lib2["Other{0}".format(i)] = otherFile[i]
    return(lib1, lib2)