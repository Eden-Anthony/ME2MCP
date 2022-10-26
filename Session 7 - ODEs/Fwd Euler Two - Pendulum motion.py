# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:17:42 2022

@author: TonyE
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 09:36:14 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

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
    return (y2)

def func2 (t,y1,y2): #Using ODE for a numerical approach
    #Constants as defined by the problem for pendulum swinging
    c = 0.18 #damping coef
    g = 9.81
    m = 0.5
    L = 1
    return (-c/m * y2 -g/L *np.sin(y1))

h = 0.005
t,y = FwdEulerTwo (0,np.pi/4,0,h,func1,func2,15)


plt.plot(t,y[0], label = "displacement")
plt.plot (t,y[1], label = "velocity")

plt.legend()