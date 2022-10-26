# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 19:09:26 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

y = lambda x,n: 5 * (np.sin(2*n*np.pi/13) ) * np.exp(-x/10)
N = np.array([0,1,8,5,3,2,1,9])
dx = 0.01
xn = np.arange (0,13+dx, dx)

yc = np.sqrt(abs(np.sqrt(10)- (xn-3)**2))

#trapezium rule function
def trapzeqd (x,y):
    #equidistant nodes
    h = x[1]-x[0]
    I = 0.5*h*(y[0]+y[-1])
    for i in range (1,len(x)-1):
        I += h*y[i]
    return (I)

Area = np.array(len(N)-1)
#needa split integral into multiple parts
for n in range (0,len(N)-1):
    yn = y(xn, n)
    nRoots = 2*n +1
    wavelength = 13/nRoots
    deltaIndex = int(len(xn)/nRoots)
    on = True
    for i in range(0,nRoots):
        a = i*deltaIndex
        b = i*deltaIndex + deltaIndex
        if on: 
            on = False
            #add area under circle - area under curve
            Area[n] += trapzeqd(xn[a:b], yc[a:b])- \
                trapzeqd(xn[a:b], y(xn[a:b],n))
        else:
            #just add area under circle
            trapzeqd(xn[a:b], yc[a:b])
            on = True

for area in Area:
    plt.plot(xn,area)
        
    