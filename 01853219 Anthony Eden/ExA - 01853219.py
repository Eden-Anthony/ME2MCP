# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 10:00:00 2022

@author: Anthony Eden
CID: 01853219
"""
import numpy as np
import matplotlib.pyplot as plt

# function f, interval [a,b], error e
def mybisection (func,a,b,e):
    za = func(a)
    zb = func(b)
    xmid = 0.5*(a+b)
    zmid = func(xmid)
    # check if the root we've found is adequately preicise
    if b-xmid > e:
        #print (a,b)
        #check which interval the function changes sign
        if za*zmid <0: 
            return(mybisection(func,a, xmid, e))
        else:
            return(mybisection(func,xmid,b,e))
    return xmid

def f(x):
    return np.sqrt(30**2-x**2)- x*np.sqrt(3)

xCoord = mybisection(f,0,30,0.001)
zCoord = xCoord*np.sqrt(3) +30
print (xCoord, zCoord)