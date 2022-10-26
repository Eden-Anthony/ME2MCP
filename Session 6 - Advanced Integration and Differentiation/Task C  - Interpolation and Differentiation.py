# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:26:14 2022

@author: TonyE
"""


import math
import numpy as np
import matplotlib.pyplot as plt

def Lagrangian (xn,xp,j):
    #inner product of all Lj
    innerProduct = 1
    for k in range (0, len(xn)):
        if (k != j): 
            innerProduct *= (xp-xn[k])/(xn[j]-xn[k])
    return (innerProduct)

def LagrInterp (xn,yn,x):
    y = np.zeros(len(x))
    #iterate through values of x that we want to find interpolations of
    for i in range (0,len(x)):
        outerSum = 0
            #outer sum of  yj x Lj
        for j in range (0,len(xn)):
            outerSum += yn[j]*Lagrangian (xn,x[i],j)
        y[i] = outerSum
        #print (outerSum)
    #print (x,y)
    return(y)
        

def nCr(n,r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))

def kthderiv (xn,yn,k): # k = 1 is the first derivative, etc
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

xn = np.linspace (0,np.pi,10)
yn = np.sin(xn)
xnew = np.linspace (0,np.pi, 100)
ynew = LagrInterp (xn,yn,xnew)
k = 1
derivatives = kthderiv(xnew, ynew, k)

plt.scatter (xn,yn, c = 'red' , label = 'Orgional Points')
plt.scatter(xnew,derivatives, s= 1, label = 'Derivative Using Interpolation')
plt.scatter(xn,kthderiv(xn,yn,k), s= 3, c = 'purple', label = 'Derivative Without Interpolation')
#plt.plot (xnew,np.cos(xnew), c = 'orange', label = 'Actual derivative')
plt.legend()