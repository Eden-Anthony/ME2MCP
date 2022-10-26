# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 10:14:47 2022

@author: Anthony Eden
01853219
"""

import numpy as np
import matplotlib.pyplot as plt

dx = 0.5
dt = 1
tEnd = 1000
R = 30
alpha1 = 4.5e-2 # alpha for Watermelon
alpha2 = 8.6e-2 # alpha for pistachio
#x = np.arange(0,0.5+dx,dx)

#fill the array with initial temp of 10
Nt = int (tEnd/dt) +1
Nx = int (2*R/dx) +1
mid = int(round(Nx/2))
T = np.zeros((Nt,Nx), dtype = "float")

#apply Iniitial Conditions
T[0,:mid] = 2 #initial temp of watermelon
T[0,mid:] = 6 # initial temp of pistachio
# Apply boundary conditions
T[:,-1]= T[:,0] = 35
Tavg1 = np.zeros(Nt-1) # average temp of watermelon
Tavg2 = Tavg1.copy() # average temp of pistachio
t = np.linspace(0,tEnd,Nt-1)
Tavg1[0]= 2
Tavg2[0] = 6

pMelting = 0 

#iterate through each time step
for p in range (1,Nt-1):
    #iterate through each x co-ordinate
    for i in range (1,Nx-1):
        if i < mid:
            T[p,i] = (alpha1*dt/(dx**2))*(T[p-1,i+1]+T[p-1,i-1])+ (1-2*alpha1*dt/(dx**2)) * T[p-1,i]
        else:
            T[p,i] = (alpha2*dt/(dx**2))*(T[p-1,i+1]+T[p-1,i-1])+ (1-2*alpha2*dt/(dx**2)) * T[p-1,i]
    Tavg1[p] = sum (T[p,:mid])/mid 
    Tavg2[p] = sum (T[p,mid:])/mid
    if Tavg2[p] > 15: #check if melting condition readched
        pMelting = p
        

x = np.arange (-R,R+dx,dx)

# plotting the temperature profiles

#part d
plt.plot (t, Tavg1, color = 'red', label = 'Watermelon')
plt.plot(t,Tavg2, color = 'blue', label = 'pistachio')
plt.legend ()

# part e, this works, please uncomment to test & comment out part d before running
#plt.plot (x, T[pMelting,:]) 
