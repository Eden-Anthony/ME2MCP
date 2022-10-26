# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 20:26:44 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

def Simpsons (yn,h):
    # number of nodal pointa
    N = len(yn)
    # initialise sum
    S = 0
    # loop every two points, and use the three points for Simpson rule
    # current point yn[i] and successive two points yn[i+1], yn[i+2]
    for i in range(0,N-2,2):
        S += h/3 * ( yn[i] + 4*yn[i+1] + yn[i+2] )
    return S

fy = lambda x: -x + np.pi

dx = 0.05
dy = 0.04
x = np.arange(0, np.pi+ dx,dx)
G = np.zeros(len(x))

#iterate thru x
for i in range (0, len(x)):
    ymax = fy(x[i])
    y = np.arange (0, ymax+dy,dy)
    z = y.copy()
    #calculate z(x,y) at each y value for this x
    for j in range (0, len(y)):
        z[j] = np.sin(x[i]*y[j]) * np.cos(x[i]+y[j])
    
    G[i] = Simpsons(z,dy)
    
print (Simpsons(G,dx))