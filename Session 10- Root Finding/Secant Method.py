# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:04:17 2022

@author: TonyE
"""
import numpy as np

def f(x):
    
    return 25 - ((6*np.pi*(x**2)) - (np.pi*(x**3)))/3

def f_prime(x, dx):
    
    return (f(x+dx)-f(x))/dx

def secant(x0,x1, e):
    
    dx = 0.1
    error = 10*e
    
    i = 0
    while error > e:
        
        i += 1
        
        xn1 = x1 - (f(x1)*(x0- x1))/(f(x0)-f(x1))

        error = abs((xn1 - x1)/x1)
        print(xn1)
        
        x0 = x1
        #calculated position becomes other point
        x1 = xn1

        
    print(i)
        
    return xn1