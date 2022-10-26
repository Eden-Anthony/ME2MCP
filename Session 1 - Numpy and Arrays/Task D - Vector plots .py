# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 17:16:29 2021

@author: TonyE
"""

import numpy as np
import math
import matplotlib.pyplot as plt

#part C

dx = 0.1
x = np.arange(-5,5+dx,dx)

dy = 0.1
y = np.arange(-5,5+dy,dy)

X,Y = np.meshgrid(x,y)

U = Y/(X**2 + Y**2)
V = -X/(X**2 + Y**2)

plt.quiver (X,Y,U,V, scale = 100)
#plt.streamplot(X, Y, U, V)
plt.show()