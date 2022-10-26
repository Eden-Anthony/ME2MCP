# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 15:30:48 2022

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

for j in range (0,10):
    t = j*0.2
    #calculate displacement value at each x position
    for i in range (1,7): #x = 0 to x = 1.8
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
    
plt.legend()

