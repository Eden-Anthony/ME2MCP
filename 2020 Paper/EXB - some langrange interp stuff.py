# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 18:33:10 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

xn = np.arange(1,9,1)
yn = np.array([0,1,8,5,3,2,1,9])

a = 1; b = 8
dx = 0.1
N = int((b-a)/dx)
x = np.linspace(1, 8+ dx,N)

y = x.copy().astype(float)
#iterate through values of x that we want to find interpolations of
for i in range (0,len(x)):
    outerSum = 0
        #outer sum of  yj x Lj
    for j in range (0,len(xn)):
        #calculate Lj
        innerProduct = 1
        for k in range (0, len(xn)):
            if (k != j): 
                innerProduct *= (x[i]-xn[k])/(xn[j]-xn[k])
        outerSum += yn[j]*innerProduct
    y[i] = outerSum
    
plt.plot(xn,yn, color = 'red')
plt.plot (x,y, color = 'blue')



