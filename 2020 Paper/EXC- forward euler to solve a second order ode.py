# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 18:44:59 2022

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

def func1 (t,y1,y2): # f1 = dy1/dx
    return y2

def func2 (t,y1,y2): #f2 = dy2/dx
    return -5*t*y2 - (t+7)*np.sin(t)

h = 0.02
t,y = FwdEulerTwo (0,3,8,h,func1,func2,15)
plt.plot(t,y[0])
