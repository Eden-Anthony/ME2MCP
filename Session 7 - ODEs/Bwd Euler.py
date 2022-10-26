# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 09:27:22 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

# This will of course not work as it requires a value you haven't calculated
# Must be solved analytically - need a bespoke solution for each equation (must rearrange)
def BwdEuler (t0,y0,h,f,tmax):
    N = int(tmax/h)+1
    t = np.empty([N,1], dtype = float)
    y = np.empty([N,1], dtype = float)
    t[0] = t0
    y[0] = y0
    for i in range (1, N):
        t[i] = t[i-1]+h
        y[i]= (y[i-1]-2*h*t[i]**3)/(1 + 2*h*t[i])
    return (t,y)

def func (t,y): #Using ODE for a numerical approach
    return (-2*y*t - 2*t**3)

h = 0.01
t,y = BwdEuler (0,100,h,func,50)

#using the analytical solution y = 100e^(-0.1x)
tanalytic = np.arange(0,50,0.01)
fanalytic = lambda x: 1- x**2 + 100* np.exp(-x**2)
yanalytic = fanalytic(tanalytic)
plt.plot (t,y, label = "Numeric")
plt.plot (tanalytic,yanalytic, label = "Analytic", c = "red", linestyle = "dotted")

plt.legend()