# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:12:10 2022

@author: TonyE
"""

import numpy as np

# Newton-Raphson method
def myNewton(x0,eps,func):
    # set a dx step
    dx = 0.1
    # set initial guess as solution
    xn = x0
    # set the error large enough, to enter the loop once
    err = 10*eps
    # repeat while the error is too large
    while err>eps:
        # set the current solution as old solution
        xp = xn
        # evaluate the function at xn and xn+dx
        fxn = func(xn)
        fxndx = func(xn+dx)
        # compute derivative
        dfxn = (fxndx - fxn)/ dx
        # apply NR method
        xn = xp - fxn/dfxn
        # assess the error
        err = abs(xn-xp)
    return xn
        
def f(x):
    y = x**2 + (x-2)**3 - 4
    return y

x0 = 1
error = 0.01
print(myNewton(x0,error,f))