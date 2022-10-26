# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:27:35 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

#function that determines f(x), g(x) and p(x)
def myfunc (x):
    f = 2*x
    g = 2
    p = np.cos(3*x)
    return ([f,g,p])

def myodebc (a,b,ya,yb,N):
    # Matrix equation of the form: Ay = B
    xvals = np.linspace(a, b, N+1)
    B = np.zeros (N+1, dtype = 'float')
    h = (b-a)/N
    #populate matrices with boundary values
    B[0]  = ya
    B[-1] = yb
    A = np.zeros ((N+1,N+1), dtype = 'float')
    #bondary conditions for the big matrix A
    A[0,0]  = 1
    A[-1,-1] = 1
    #populate A matrix using the central difference scheme and rearranging 
    for i in range (1, N):
        coeffs = myfunc(xvals[i])
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
b = np.pi
N = 100
y = myodebc(a, b, 1.5, 0, N)
x = np.linspace(a, b, N+1)
plt.plot (x, y)

