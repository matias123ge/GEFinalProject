# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 22:00:10 2017

"""
import matplotlib.pyplot as plt
import numpy as np

def visualization(data,tvec):
    zonelib = {} #define an empty zone library
    for i in range(data.shape[1]):
        zonelib["zone{0}".format(i+1)] = data[:,i] #fill the zone library with the data
    print(zonelib["zone1"])

    