# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 10:48:29 2022

@author: Anthony Eden
01853219
"""

import numpy as np
import matplotlib.pyplot as plt

# compute the Lagrangian polynomial j at a point xp, with given nodes xn
def Lagrangian (xn,xp,j):
    #inner product of all Lj
    innerProduct = 1
    for k in range (0, len(xn)):
        if (k != j): 
            innerProduct *= (xp-xn[k])/(xn[j]-xn[k])
    return (innerProduct)

#for finding multiple interpolation values i.e. x is an array
def LagrInterpMulti (xn,yn,x):
    y = x.copy().astype(float)
    #iterate through values of x that we want to find interpolations of
    for i in range (0,len(x)):
        outerSum = 0
            #outer sum of  yj x Lj
        for j in range (0,len(xn)):
            outerSum += yn[j]*Lagrangian (xn,x[i],j)
        y[i] = outerSum
    return(y)

#read in files
xnFile = open('LogoXn.txt','r')
ynFile = open ('LogoYn.txt','r')
xn = xnFile.readlines()
yn = ynFile.readlines()
xnFile.close(); ynFile.close()


#convert data from strings to floating points
xn = list(map (float,xn))
yn = list(map (float,yn))

#constants
dx = 0.5

#find interpolated set of points
x = np.arange(-19, 19+dx,dx)
y = LagrInterpMulti(xn,yn,x)

plt.scatter(xn,yn, color = 'blue', label = 'Known Points')
plt.plot(x,y,color = 'red', label = 'Interpolated Curve')
plt.legend()