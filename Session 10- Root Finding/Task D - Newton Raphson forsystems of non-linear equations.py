# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 15:39:56 2022

@author: TonyE
"""
import numpy as np

# u(x,y), v(x,y), e = error, vals = [x,y]
"""def newtonSolve (u, v, e, vals):
    x,y = vals[0],vals[1]
    J = np.array ([[xDeriv(u,x,y),yDeriv(u, x, y)],[xDeriv(v,x,y),yDeriv(v, x, y)]], dtype = 'float')
    funcVals = np.array([u(x,y),v(x,y)], dtype = 'float')
    nextVals = vals - np.matmul(np.linalg.inv(J),funcVals)
    if np.amin(abs(nextVals-vals))> e:
        return newtonSolve(u,v,e,nextVals)
    return nextVals

#central difference derivative approx
dh = 0.75
xDeriv = lambda f,x,y: (f(x+dh,y)-f(x-dh,y))/2*dh
yDeriv = lambda f,x,y: (f(x, y+dh)-f(x, y-dh))/2*dh

f1 = lambda x,y: x**2 + 1 -y
f2 = lambda x,y: 2*np.cos(x) - y
x0 = np.array([0.2,1.8], dtype = 'float')
error = 0.001

print(newtonSolve(f1,f2,error, x0))"""

# set of functions of the system
def sysfuncs(X):
    # X is a one dimensional vector with as many elements as the number of functions, i.e. u, v, etc.
    # define a vector for the output
    UV = np.ndarray(len(X))
    # evaluate all the functions at point X
    # X is a vector long as the number of independent variables, i.e. x, y, etc.
    # alter and write here the various functions
    UV[0] = X[0]**2 + 1 - X[1]
    UV[1] = 2*np.cos(X[0]) - X[1]
    return UV
# this function computes the Jacobian of a set of functions
def Jacobian(X,Dx):
    # establish how many functions/independent variables, aka the size of the Jacobian
    N = len(X)
    # set an empty array N x N
    Jac = np.ndarray((N,N))
    # calculate and fill column by column, i.e. derivative of each function with respect to the same
    # independent variable
    # We will apply the central difference scheme for the derivative:
    # df/dx = (f at successive point - f at previous point) / dx
    for i in range(N):
        # set the successive point for the independend variable in question
        X[i] += Dx[i]
        # evaluate all the functions at this point
        Fplus = sysfuncs(X)
        # set the precedent point for the independend variable in question
        X[i] -= 2*Dx[i]
        # evaluate all the functions at this point
        Fminus = sysfuncs(X)
        # determine the derivatives for the column ith
        Jac[:,i] = (Fplus - Fminus) / (2*Dx[i])
    return Jac
def MatVect(A,b):
    # this function performs matrix-vector multiplication
    N = A.shape[0]
    y = np.zeros(N)
    for i in range(N):
        for k in range(N):
            y[i] += A[i,k] * b[k]
    return y
# solve a set of non linear equations
# set the accuracy requested
eps = 0.001
# set the initial guess
X0 = np.array([0.2, 1.8])

# set dx (of the order of or smaller than eps)
Dx = np.array([0.5*eps, 0.5*eps])
# set initial guess as solution
Xn = X0
# set the error large enough, to enter the loop once
err = 10*eps
# repeat while the error is too large
while err > eps:
    # set the current solution as old solution
    Xp = Xn
    # compute teh Jacobian
    J = Jacobian(Xn,Dx)
    # invert the Jacobian
    Jinv = np.linalg.inv(J)
    # apply Newton's methods
    Xn = Xp - MatVect(Jinv,sysfuncs(Xn))
    # assess the error: consider the maximum error, amongst errors for all variables
    err = np.max(np.abs(Xn-Xp))


print(Xn)