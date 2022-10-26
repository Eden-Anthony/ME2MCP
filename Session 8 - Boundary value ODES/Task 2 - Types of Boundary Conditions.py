# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 16:30:48 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

# y'' + f(x)y' + g(x)y = p(x)
#function that determines f(x), g(x) and p(x)
def myfunc (x):
    f = x
    g = 1
    p = 5*x
    return ([f,g,p])
# c0y'(a) + c1y(a) = BCa , c2y'(b) + c3y(b) = BCb
#for Dirichlet, c0 = c2 = 0
#for Neumann, c1 = c3 = 0
def myodebc (a,b,BCa, BCb,N, c):
    # Matrix equation of the form: Ay = B
    xVals = np.linspace(a, b, N+1)
    B = np.zeros (N+1, dtype = 'float')
    h = xVals[1]-xVals[0]
    #populate matrices with boundary values
    B[0]  = BCa
    B[-1] = BCb
    A = np.zeros ((N+1,N+1), dtype = 'float')
    #bondary conditions for the big matrix A
    A[0,0]  = c[1] - c[0]/h
    A[0,1]  = c[0]/h
    A[-1,-1] = c[2]/h +c[3]
    A[-1,-2] = -c[2]/h
    #populate A matrix using the central difference scheme and rearranging 
    for i in range (1, N):
        coeffs = myfunc(xVals[i])
        a = (1/h**2) - coeffs[0]/(2*h)
        b = coeffs[1] - 2/(h**2)
        c = 1/(h**2) + coeffs[0]/ (2*h)
        A[i,i-1] = a
        A[i,i] = b
        A[i,i+1] = c
        B[i]= coeffs[2]
    # y = inverse(A) * B
    y = np.dot(np.linalg.inv(A) , B)
    return y 

a = 0
b = 2
BCa = 0
BCb = -1
N = 50
c = [1,0,1,0]
y = myodebc(a, b, 0,-1, N,c)
x = np.linspace(a, b, N+1 )
plt.plot (x, y)
