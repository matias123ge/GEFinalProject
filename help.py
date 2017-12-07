# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:45:07 2017

@author: Aimas
"""
import time

def help():
    file = open("help.txt","r")
    helptxt = file.read().splitlines()
    file.close
    helptxt = "".join(helptxt)
    return(helptxt)
    