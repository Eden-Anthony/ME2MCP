# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 09:26:39 2022

@author: TonyE
"""

import numpy as np

def AdaptiveSimpsons (a,b,h,f,tolerance):
    #create arrays of known points
    xn = np.arange (a,b+h,h)
    yn = f(xn)
    h = (b-a)/len(xn)
    #calculate the area using the simpsons rule
    total = yn[0] + yn[-1]
    for i in range (1, len(xn)-1):
        if  i%2 == 0:
            total += 2*yn[i]
        else:
            total += 4*yn[i]
    total *= h/3
    #if tolerance = -1, we are only using the function to calculate errors
    if tolerance != -1:
        total2 = AdaptiveSimpsons(a, b, h/2, f, -1)
        error = abs((1/15)*(total2-total))
        #error checking
        if error > tolerance:
            total = AdaptiveSimpsons(a, b, h/2, f, tolerance)
    return total

func = lambda x: x**3
tolerance = 0.1
a = 0 
b = 2*np.pi
h = np.pi/4

print (AdaptiveSimpsons(a,b,h,func, tolerance))
    