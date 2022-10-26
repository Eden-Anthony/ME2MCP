# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 09:36:14 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

def FwdEuler (t0,y0,h,f,tmax):
    N = int(tmax/h)+1
    t = np.empty(N, dtype = float)
    y = np.empty(N, dtype = float)
    t[0] = t0
    y[0] = y0
    for i in range (1, N):
        y[i]= y[i-1] + h* f (t[i-1],y[i-1])
        t[i] = t[i-1]+h
    return (t,y)

def FwdEulerTwo (t0,y10,y20,h,f1,f2,tmax):
    N = int(tmax/h)+1
    t = np.empty(N, dtype = float)
    y1 = np.empty(N, dtype = float)
    y2 = np.empty(N, dtype = float)
    t[0] = t0
    y1[0] = y10
    y2[0] = y20
    for i in range (1, N): # Calculating values of y1 and y2 using Fwd Euler
        y1[i]= y1[i-1] + h* func1 (t[i-1],y1[i-1],y2[i-1])
        y2[i]= y2[i-1] + h* func2 (t[i-1],y1[i-1],y2[i-1])
        t[i] = t[i-1]+h
    return (t,[y1,y2])

def func1 (t,y1,y2): #Using ODE for a numerical approach
    return (0.3*y1*y2 -0.8*y1)

def func2 (t,y1,y2): #Using ODE for a numerical approach
    return (1.1*y2 - y1*y2)

h = 0.019
t,y = FwdEulerTwo (0,0.8,7,h,func1,func2,40)

#using the analytical solution y = 100e^(-0.1x)
tanalytic = np.arange(0,50,0.01)
fanalytic = lambda x: 100* np.exp(-0.1*x)
yanalytic = fanalytic(tanalytic)

fig, ax = plt.subplots(2)
ax[0].plot (t,y[0], label = "£")
ax[0].plot (t,y[1], label = "N")
ax[1].plot (y[0],y[1])
#plt.plot (tanalytic,yanalytic, label = "Analytic", c = "red", linestyle = "dotted")

ax[0].legend()