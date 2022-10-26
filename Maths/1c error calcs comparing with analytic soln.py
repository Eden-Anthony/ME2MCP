# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 20:27:31 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

k = 0.2
h = k
xVals = np.linspace (0-k,1+k,8, endpoint = True) #2 extra points for x = 0.2 & 1.2
u = np.zeros( shape = (8,11) , dtype = float)
#apply intial conditions
u[:,0] = np.cos(np.pi*xVals)

#analytic solution
uAnalytic = np.copy(u)

for j in range (0,10):
    t = j*0.2
    #Set analytic solution for i = 0 and i = 7
    uAnalytic[0,j] = np.cos(np.pi*0)*np.cos(np.pi*t)
    uAnalytic[-1,j] = np.cos(np.pi*xVals[-1])*np.cos(np.pi*t)
    #calculate displacement value at each x position
    for i in range (1,7): #x = 0 to x = 1.8
        x = (i-1)*0.2
        #analytic solution catering
        uAnalytic[i,j] = np.cos(np.pi*x)*np.cos(np.pi*t)
        if j == 0:
            u[i,j+1] = 0.5* (u[i-1,j] + u[i+1,j])
        elif i == 1 or i == 6:
            u[i,j+1] = 2*u[i+1,j] - u[i,j-1]
        else:
            u[i,j+1] = u[i-1,j] + u[i+1,j] - u[i,j-1]
        #symemtry around x = 0 and x = 1
        u[7,j] = u [5,j] 
        u[0,j] = u [2,j]
    plt.plot(xVals, u[:,j], label = ("t = " + str(round(t,1) )))

errors = (uAnalytic - u)/uAnalytic

