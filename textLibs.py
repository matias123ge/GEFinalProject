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
    
    return(errorFile, otherFile)