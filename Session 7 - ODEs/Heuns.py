# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 21:52:54 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

def Heun (t0,y0,h,f,tmax):
    N = int(tmax/h)
    t = np.empty([N,1])
    y = np.empty([N,1])
    t[0] = t0
    y[0] = y0
    for i in range (1, N):
        t[i] = t[i-1]+h
        k1 = h* f(t[i-1], y[i-1])
        k2 = h* f(t[i], y[i-1]+k1)
        y[i]= y[i-1] + 0.5*(k1+k2)
    return (t,y)

def func (t,y): 
    return -0.1*y

h = 2
t,y = Heun (0,100,h,func,50)

plt.plot (t,y)
plt.legend(["h = " + str (h) ])