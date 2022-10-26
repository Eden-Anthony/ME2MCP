# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 09:48:36 2022

@author: TonyE
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def nCr(n,r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))

def kthderiv (xn,yn,k): #k = 1 is the second derivative
    h = xn[1]-xn[0]
    dydx = np.zeros (len(xn))
    #find derivative for each n point
    for n in range (0, len(yn)):
        deltakyn = 0
        if n+k <= len(xn)-1: #last n points cannot be found with forward scheme
            for i in range (0,k+1):
                deltakyn += (-1)**i * nCr(k,i) * yn[n+(k-i)]
            dydx[n]= deltakyn/(h**k)
    return dydx

xn = np.linspace (0,np.pi,100)
yn = np.sin(xn)
k = 2
derivatives = kthderiv(xn, yn, k)

plt.plot (xn,yn, c = 'red')
plt.scatter(xn,derivatives, s= 1)