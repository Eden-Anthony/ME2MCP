# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 17:49:39 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as pl

# Langrangian polynomial
# compute the Lagrangian polynomials j, given nodes xn at a given point xp
def Lagrangian(j,xn,xp):
    # establish the number of nodes
    n = len(xn)
    # the order of the polynomial will then be n-1
    
    # set the initial value of the polynomial to 1
    L = 1
    # range of k is from 0 to n-1 (the order of the polynomial)
    for k in range(0,n):
        # exclude the case k == j
        if k != j:
            L *= (xp-xn[k]) / (xn[j]-xn[k])
    return L
def LagInterp(xn,yn,x):
    N = len(xn)
    # establish the order of the interpolating polynomial, N-1
    n = N - 1
    y = np.ndarray(len(x))
    # interpolate for all the values of x in the interpolating range
    for i in range(len(x)):
        # evaluate pn(xp)
        yp = 0
        # use Langrangian polynomial up to n, included
        for j in range(0,n+1):
            yp += yn[j] * Lagrangian(j,xn,x[i])
        # add the curren value of yp to the list of y
        y[i] = yp
    return y

def mybisectiondiscrete(a,b,eps,xn,yn):
    # repeat the split of teh interval until the bracketing intervla becomes smaller than the accuracy
    while abs(a-b)>eps:
        # calculate the mid point
        xm = (a + b) / 2
        # establish in which subinterval the solution lies
        # compute f(a) * f(xm)
        ff = LagInterp(xn,yn,[a]) * LagInterp(xn,yn,[xm])
        #ff = funcint(a,xn,yn) * funcint(xm,xn,yn)
        if ff < 0: 
            # the solution lies in the left interval
            # set the upper bracket as xm
            b = xm
        else:
            # the solution lies in the right interval
            # set the lower bracket as xm
            a = xm
            
    # the true solution is bracketed within the latest interval [a,b]
    # we can approximate it with the midpoint
    sol = (a + b) / 2
    
    return sol
# read the files
f = open('x.txt','r')
v = f.readlines()
xn = np.ndarray(len(v))
i = 0
for value in v:
    xn[i] = float(v[i])
    i += 1
f.close()
f = open('fx.txt','r')
v = f.readlines()
yn = np.ndarray(len(v))
i = 0
for value in v:
    yn[i] = float(v[i])
    i += 1
f.close()
# plot the values
pl.scatter(xn,yn)
pl.grid()


sol = mybisectiondiscrete(-5,8,0.001,xn,yn)
print(sol)