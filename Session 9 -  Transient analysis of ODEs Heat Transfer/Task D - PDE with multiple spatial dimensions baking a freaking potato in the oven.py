# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:22:22 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

dx = 0.01
dy = dx
dt = 1
tEnd = 9000
Tw = 180
Ti = 25
Tpot = -15
b = 0.4
d = 0.3
pw = 0.06  # potato size
alphaA = 1.9e-5
alphaP = 1.3e-7
#x = np.arange(0,0.5+dx,dx)

#fill the array with initial temp of 25
xn = np.arange(0,b+dx,dx)
Nx = len(xn)
yn = np.arange(0,d+dy,dy)
Ny = len(yn)
t = np.arange(0,tEnd+dt,dt)
Nt = len(t)
T = np.full((Ny,Nx,Nt), Ti, dtype = "float")

#apply BCs:
T[:,-1,:] = Tw
T[:,0,:] = Tw
T[0,:,:] = Tw
T[-1,:,:] = Tw

# position of the potato
xap = b/2 - pw/2
xbp = b/2 + pw/2
yap = d/2 - pw/2 
ybp = d/2 + pw/2

# initialise the tempearture of the potato
for i in range(0,Nx):
    for j in range(0,Ny):
        if (xap<=xn[i]<=xbp) and (yap<=yn[j]<=ybp):
            T[j,i,0] = Tpot

#iterate through each time step
for p in range (1,Nt):
    #iterate through each x co-ordinate
    for i in range (1,Nx-1):
        x = i*dx
        for j in range (1,Ny-1):
            y = j*dy
            alpha = alphaA
            if (xap<= x <=xbp) and (yap <=y <= ybp): #if in potato
                alpha = alphaP
            cx = alpha*dt/(dx**2)
            cy = alpha*dt/(dy**2)
            T[j,i,p] = (1 - 2*cx - 2*cy)* T[j,i,p-1] + \
            cx * (T[j,i+1,p-1]+T[j,i-1,p-1]) + \
            cy * (T[j+1,i,p-1]+T[j-1,i,p-1])

xv, yv = np.meshgrid(xn,yn)
print (min(T[:,20,tEnd]))
plt.contour(xv,yv,T[:,:,tEnd] )

plt.colorbar()