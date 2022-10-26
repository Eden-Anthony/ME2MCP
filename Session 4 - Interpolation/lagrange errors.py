# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:03:53 2021

@author: ae1220
"""

import numpy as np
import matplotlib.pyplot as plt

def Lagrangian (xn,xp,j):
    #inner product of all Lj
    innerProduct = 1
    for k in range (0, len(xn)):
        if (k != j): 
            innerProduct *= (xp-xn[k])/(xn[j]-xn[k])
    return (innerProduct)

def LagrInterp (xn,yn,x):
    outerSum = 0
    #outer sum of  yj x Lj
    for j in range (0,len(xn)):
        outerSum += yn[j]*Lagrangian (xn,x,j)
        #print (outerSum)
    #print (x,y)
    return(outerSum)

errors = np.ndarray(14)
p = np.ndarray(15)

#calculate interp values for N = 1 to 15
for i in range (0,14):
    n = i+1
    xn = np.linspace (1, 2, n+1)
    yn = np.sin(xn)
    p[i]= LagrInterp(xn,yn,np.pi/2)

for i in range (0,14):
    errors[i]= p[i+1]-p[i]
    
print(errors)
          

