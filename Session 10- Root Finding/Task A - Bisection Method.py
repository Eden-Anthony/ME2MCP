# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 17:25:28 2022

@author: TonyE
"""
import numpy as np
import matplotlib.pyplot as plt

# function f, interval [a,b], error e
def mybisection (func,a,b,e):
    ya = func(a)
    yb = func(b)
    xmid = 0.5*(a+b)
    ymid = func(xmid)
    # check if the root we've found is adequately preicise
    if b-xmid > e:
        #print (a,b)
        #check which interval the function changes sign
        if ya*ymid <0: 
            return(mybisection(func,a, xmid, e))
        else:
            return(mybisection(func,xmid,b,e))
    return xmid

def f(x):
    return (x**2+(x-2)**3-4)

errors = [0.1,0.01,0.001]

for error in errors:
    print ('root = ', mybisection(f,-10,40,error) , ' | error = ', error)