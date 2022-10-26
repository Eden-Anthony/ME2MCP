  # -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 09:07:25 2021

@author: ae1220
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
        #print (outerSum)
    #print (x,y)
    return(y)

# Receives the sets of know values, xn and yn, the points to be interpolated x, 
# and returns the interpolated values y, 
# by using Lagrangian polynomials.

#for finding a single interpolation value i.e. x ia a single value
def LagrInterp (xn,yn,x):
    outerSum = 0
    #outer sum of  yj x Lj
    for j in range (0,len(xn)):
        outerSum += yn[j]*Lagrangian (xn,x,j)
    return(outerSum)

x = np.linspace(0,3,50, dtype=float)
n = 6

xn = np.linspace(1,2,n)
#print (xn)
yn  = np.sin (xn)
yLagr = LagrInterpMulti (xn,yn,x)
plt.scatter (x, yLagr, color = 'red')
plt.plot (x, np.sin(x))
#n = 3
#x = np.
#xn = np.array([0,1,2]).astype(float)
#yn = np.array([1,4,2]).astype(float)
#print(LagrInterp(xn,yn,1.25))


#plt.scatter (xVals, LagrInterp(xn,yn,xVals))
    
