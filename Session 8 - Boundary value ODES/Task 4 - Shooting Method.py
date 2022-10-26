# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:26:12 2022

@author: TonyE
"""
import numpy as np
import matplotlib.pyplot as pl

#Shooting Method

def func1(t,y):
    # Blasius
    f = y[1]
    return f
def func2(t,y):
    # Blasius
    f = y[2]
    return f
def func3(t,y):
    # Blasius
    f = -0.5*y[0]*y[2]
    return f

def FwEulerThree(Y0,t0,tend,h):
    # compose nodal times
    t = np.arange(t0,tend+h,h)
    # determine the number of time steps
    N = len(t)
    # allocate output array
    Y = np.ndarray((3,N))
    # initialise the solution
    t[0] = t0
    Y[0,0] = Y0[0]
    Y[1,0] = Y0[1]
    Y[2,0] = Y0[2]
    # compute the solution incrementally at subsequent time steps
    for n in range(1,N):
        Y[0,n] = Y[0,n-1] + func1(t[n-1],Y[:,n-1]) * h
        Y[1,n] = Y[1,n-1] + func2(t[n-1],Y[:,n-1]) * h
        Y[2,n] = Y[2,n-1] + func3(t[n-1],Y[:,n-1]) * h
    return (t,Y)

# Lagrangian interpolation functions, copied and pasted from Session 4

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

# Numerical integration with Trapezium rule, copied and pasted from Session 3

def trapz(x,y):
    # get the number of subintervals
    N = len(x) - 1
    # compute the integral
    # set range for the trapezia: there are as many trapezia as the number of intervals
    R = range(0,N)
    S = 0
    for i in R:
        # compute the area of this single trapezium (remind yourself the area of a trapezium)
        S += 0.5 * (y[i+1] + y[i]) * (x[i+1] - x[i])
    return S

# Blasius
Nitmax = 1000 # we need to stop iteration if they become too large: the solution is diverging
tol = 1.0e-5 # desired tolerance for the error

# set the initial conditions
Y0 = np.ndarray(3)
# Y[0] contains f(at 0); Y[1] contains g(at 0); Y[2] contains h(at 0)
Y0[0] = 0 # f(at 0)
Y0[1] = 0 # g(at 0) ie velocity at 0
gfinal = 1 # g(at eta_max) ie velocity at eta_max
# Y0[0], Y0[1] and gfinal are the three physical boundary conditions, as specified by the problem

# this is the initial condition for the marching direct scheme. It is not a condition imposed by the problem
Y0[2] = 1 # h(at 0)acceleration at 0: this is a guess. it will readjusted during iterations

# set the domain
eta0 = 0 # lower boundary
etamax = 10 # upper boundary
Deta = (etamax-eta0)/1000  # eta step

# initialisations
err = 100  # set the error to a large value
Nit = 0    # count the iterations
hOld = 0  # h(at 0)
gOld = 0  # g(at 0) 

# iterate until reaching desired tolerance or exceed too many iterations
while err > tol and Nit<Nitmax:
    Nit += 1 # count iterations
    
    # solve with Forward Euler with current Y0 initial conditions. Y0[0], Y0[1] are given
    # by the problem specs, Y0[2] has been guessed
    (eta,Y) = FwEulerThree(Y0,eta0,etamax,Deta)
    # Y[0,:] contains the solution f across the domain
    # Y[1,:] contains the velocity g across the domain
    # Y[2,:] contains the acceleration h across the domain
    
    g = np.array([gOld,Y[1,-1]]) # set the two points of g for interpolation: the old g and the value just computed
    h = np.array([hOld,Y0[2]])   # set the two points of h for interpolation: the old h and the value just computed
    hInterp = LagInterp(g,h,np.array([gfinal])) # calculate the new guess for h at gfinal
    # update old points with current values
    gOld = Y[1,-1]
    hOld = Y0[2]
    
    # set the new estimated value for h(at 0)
    Y0[2] = hInterp[0]
    
    # assess the error
    err = abs(Y[1,-1]-gfinal)

print('Iterations needed: '+str(Nit))


# plotting section

f = Y[0,:]  # displacement
u = Y[1,:]  # velocity
v = 0.5*(eta*u-f) #

# calculate thicknesses
diff = abs(u-0.99*max(u))
eta99 = diff.argmin()
# displacement thickness delta1 = int 0->infinity of 1-u(eta)
d1 = trapz(eta,max(u)-u)
# momentum thickness delta2 = int 0->infinity of u(eta)*(1-u(eta))
d2 = trapz(eta,u*(max(u)-u))
print('d99: '+str(eta[eta99])+'   d1: '+str(d1)+'   d2: '+str(d2))

# plot u and thicknesses
pl.plot(u,eta)
pl.grid()
pl.plot([0,max(u)],[eta[eta99],eta[eta99]])
pl.plot([0,max(u)],[d1,d1])
pl.plot([0,max(u)],[d2,d2])
pl.xlabel('normalised u')
pl.ylabel('eta')
pl.show()

# plot v
pl.plot(v,eta)
pl.grid()
pl.xlabel('normalised v')
pl.ylabel('eta')
pl.show()
