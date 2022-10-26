# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 19:49:20 2022

@author: TonyE
"""
import numpy as np
import matplotlib.pyplot as plt

def RightReimann (x,y):
    h = x[1]-x[0]
    I = h*np.sum(y)- h*y[0]
    return I

def LeftReimann (x,y):
    h = x[1]-x[0]
    I = h* np.sum(y)- h*y[-1]
    return I

def trapzeqd (x,y):
    #equidistant nodes
    h = x[1]-x[0]
    I = 0.5*h*(y[0]+y[-1])
    for i in range (1,len(x)-1):
        I += h*y[i]
    return (I)

step = 0.1
x = np.arange (5,9+step,step)
y = np.sin(2*x)

print (RightReimann(x,y), LeftReimann(x, y))
plt.plot(x,y)