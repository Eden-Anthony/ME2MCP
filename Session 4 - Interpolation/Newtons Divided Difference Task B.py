# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:26:21 2021

@author: ae1220
"""
# Task B1
import numpy as np
import matplotlib.pyplot as plt

def NewtDivDiff(xn,yn):
    # recursive form
    # determine number of points
    N = len(xn)
    # set the order: 1 node -> f0; 2 nodes -> f1, etc.
    N = N - 1
    if N == 0:
        # f is the point itself
        f = yn[0]
    else:
        # f is defined recursively as (slide 64):
        # f = ( f[x0,...x(n-1)] - f[x1,...xn] ) / ( x0 - xn)
        f = ( NewtDivDiff(xn[:-1],yn[:-1]) - NewtDivDiff(xn[1:],yn[1:]) ) / ( xn[0] - xn[-1] )
    return f

def NewtDivDiffIt(xn,yn):
    # iterative form
    
    # determine number of points
    N = len(xn)
    # set the order: 1 node -> f0; 2 nodes -> f1, etc.
    n = N - 1
    f = np.copy(yn)
    for j in range(0,n):
        for i in range(0,n-j):
            f[i] = (f[i+1]-f[i]) / (xn[i+j+1]-xn[i])
             
    return f[0]

def NewtonInterp(xn,yn,x):
    Nx = len(xn)
    # determine order
    k = Nx - 1
    y = []
    for xp in x:
        # determine pn at x = xp
        yp = yn[0]
        for i in range(1,k+1):
            prod = 1
            for j in range(0,i):
                prod *= (xp-xn[j])
            yp += prod * NewtDivDiff(xn[0:i+1],yn[0:i+1])
        y += [yp]
    y = np.array(y)
    return y

# Task B3

# func1 = lambda x : np.sin(x)

# # main
# a = 1 # lower interval
# b = 2 # upper interval
# Nx = 2 # number of nodes
# #xn = np.linspace(a,b,Nx)
# #yn = func1(xn)
# # determine order
# k = Nx - 1

# # set the domain of interpolation
# #x = np.linspace(0,3,60)

# #y = NewtonInterp(xn,yn,x)

# # convert list into array
# #y = np.array(y)   
# # plot polynomial in the interpolating range
# #plt.plot(x,y,c='Red')
# # plot the initial nodal info only
# #plt.scatter(xn,yn,c='Blue')
# # plot the actual function
# #plt.plot(x,func(x),c='Green')
# #plt.show()


# Task B4

func2 = lambda x: 1 / (1+25*x**2)

dx = 0.01
x = np.arange(-1,1+dx, dx)
N = np.arange(1,16,1)
xn = np.linspace(-1,1,4)
yn = func2(xn)
plt.plot(x,NewtonInterp(xn,yn,x))
#plt.plot (x, func2(x))


#for n in N:
    #xn = np.linspace(-1,1,n+1)
    #yn = func(xn)
    #y = NewtonInterp (xn,yn,x)
    #pl.plot (x,y)
    