# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 14:07:02 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

xVals = np.linspace (0,1,6, endpoint = True)
k = 0.2
h = k
u = np.zeros( shape = (6,11) , dtype = float)
#apply inital conditions
u[:,0] = np.sin(np.pi*xVals)
u[0] = 0
u[-1] = 0

for j in range (0,10):
    t = j*0.2
    #calculate displacement value at each x position
    for i in range (1,5):
       #x = i*0,2
        if j == 0:
            u[i,j+1] = 0.5* (u[i-1,j] + u[i+1,j])
        else:
            u[i,j+1] = u[i-1,j] + u[i+1,j] - u[i,j-1]
    plt.plot(xVals, u[:,j], label = ("t = " + str(round(t,1) )))
#plot for t = 2
plt.plot(xVals, u[:,-1], label = ("t = " + str(round(t,1) )))
    
plt.legend()

