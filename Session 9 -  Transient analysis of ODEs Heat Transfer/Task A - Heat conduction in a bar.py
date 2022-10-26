# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 09:24:37 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

dx = 0.01
dt = 1
tEnd = 1000
Ta = 50
Tb = 70
Ti = 10
L = 0.5
alpha = 1.172*10**(-5)
#x = np.arange(0,0.5+dx,dx)

#fill the array with initial temp of 10
Nt = int (tEnd/dt) +1
Nx = int (L/dx) +1
T = np.full((Nt,Nx), Ti, dtype = "float")

#apply BCs:
T[:,0] = Ta
T[:,-1] = Tb

#iterate through each time step
for p in range (1,Nt):
    #iterate through each x co-ordinate
    for i in range (1,Nx-1):
        T[p,i] = (alpha*dt/(dx**2))*(T[p-1,i+1]+T[p-1,i-1])+ (1-2*alpha*dt/(dx**2)) * T[p-1,i]

x = np.arange (0,L+dx,dx)
plt.plot (x, T[-1,:])