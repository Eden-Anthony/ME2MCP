# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 09:18:24 2021

@author: ae1220
"""
import numpy as np
import math
import matplotlib.pyplot as plt

#trapezium rule function
def trapzeqd (x,y):
    #equidistant nodes
    h = x[1]-x[0]
    I = 0.5*h*(y[0]+y[-1])
    for i in range (1,len(x)-1):
        I += h*y[i]
    return (I)

#define points x, y

x = np.linspace(2,4,13)
y = np.linspace(2,5,27)
G = np.zeros (len(x))

for i in range (0, len(x)):#traverse x

    # all z values for a given x as we traverse the y direction 
    z = np.zeros (len(y))
    
    for j in range (0,len(y)): #actually traversing y
        z = (x[i]-1)**2 +((1/y) -2)**2
    
    #Calculating the area under the curve for a given x 
    G[i] = trapzeqd(y, z)

# Calculating the total area by summing all the areas traversed in the y direction
I = trapzeqd(x, G)
print (I)

