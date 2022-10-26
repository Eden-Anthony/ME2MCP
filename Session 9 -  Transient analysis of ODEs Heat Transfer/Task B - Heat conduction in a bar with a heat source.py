# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 09:59:05 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

dx = 0.01
dt = 1
tEnd = 1200
Ta = 10
Tb = 10
Ti = 10
Tw = 5
L = 0.5
alpha = 1.172*10**(-5)
k = 40
h = 500
#x = np.arange(0,0.5+dx,dx)

#fill the array with initial temp of 10
Nt = int (tEnd/dt) +1
Nx = int (L/dx) +1
T = np.full((Nt,Nx), Ti, dtype = "float")

#apply BCs:
midpoint = int(np.round(Nx/2,0))
T[:, midpoint] = 100


#iterate through each time step
for p in range (1,Nt):
    #iterate through each x co-ordinate
    for i in range (1,Nx-1):
        if i != midpoint:
            T[p,i] = (alpha*dt/(dx**2))*(T[p-1,i+1]+T[p-1,i-1])+ (1-2*alpha*dt/(dx**2)) * T[p-1,i]
        #cater for neumann boundaries
        T[p,0] = T[p,1] - (dx*h/k)*(Ta-Tw)
        T[p,-1] = T[p,-2] - (dx*h/k)*(Tb-Tw)

x = np.arange (0,L+dx,dx)
plt.plot (x, T[-1,:], label = "t = 1200")
plt.plot (x, T[midpoint,:], label = "t = 500")
plt.plot (x, T[0,:], label = "t = 0")
plt.legend()