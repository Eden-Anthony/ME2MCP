# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:03:53 2021

@author: ae1220
"""

import numpy as np
import math
import matplotlib.pyplot as plt

nodes = 5

#trapezium rule function
def trapzeqd (x,y):
    h = (x[len(x)-1]-x[0])/(nodes-1)
    I = 0.5*h*(y[0]+y[len(y)-1])
    for i in range (1,len(x)-2):
        I += h*y[i]
    return (I)

a = 0

#empty array for trapzeqd values and b values
Ivals = np.zeros(4)
bVals = np.array([10,100,1000,10000])

for i in range (0,4):
    b = bVals[i]
    dx = (b-a)/(nodes-1)
    x = np.arange(a,b+dx,dx)
    y = np.zeros(len(x))
    #define points y
    for j in range (0, len(x)):
        y[j] = 1/math.sqrt(x[j]**18.1 -2021)
    Ivals[i]= trapzeqd(x,y)
    
plt.plot(bVals, Ivals)