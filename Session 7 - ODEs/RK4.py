# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 21:59:13 2022

@author: TonyE
"""

import numpy as np
import math
import matplotlib.pyplot as plt

def RK4 (t0,y0,h,f,tmax):
    N = int(tmax/h)+1
    t = np.empty(N, dtype = float)
    y = np.empty(N, dtype = float)
    t[0] = t0
    y[0] = y0
    for i in range (1, N):
        t[i] = t[i-1]+h
        k1 = h* f(t[i-1],y[i-1])
        k2 = h* f(t[i-1]+0.5*h, y[i-1]+0.5*k1)
        k3 = h* f(t[i-1]+0.5*h, y[i-1]+0.5*k2)
        k4 =  h* f(t[i-1]+0.5*h, y[i-1]+0.5*k1)
        y[i]= y[i-1] + (k1+2*k2+ 2*k3 +k4)/6
    return (t,y)

def func (t,y): 
    return (-2*y*t - 2*math.pow(t,3) )

def yTrue (t):
    return (1- t**2 + 100* np.exp(-t**2))

h = 0.1
t,y = RK4 (0,100,h,func,4)

plt.plot (t,y)
plt.plot (t, yTrue(t))
plt.legend(["h = " + str (h) ])