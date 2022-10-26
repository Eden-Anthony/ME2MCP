# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:07:18 2021

@author: ae1220
"""

import numpy as np

def trapz (x,y):
    I = 0
    for i in range (0,len(x)-1):
        I += 0.5*(y[i]+y[i+1])*(x[i+1]-x[i])
    return (I)

x= np.array([0,1.5,6,7,16])
def f(x):
    return (1/(x+1))

y= f(x)
print (trapz(x,y))
        