# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:17:44 2021

@author: ae1220
"""

import numpy as np
import math
import matplotlib.pyplot as plt


dx = 0.5*100
x = np.array([])
for i in range (-5*100, -2*100 + int(dx) , int(dx)):
    x = np.append(x, i/100)

dx = 0.05*100
for i in range (-2*100 +int(dx), 3*100 , int(dx)):
    x = np.append(x, i/100)

dx = 0.5*100
for i in range (3*100 , 5*100 +int(dx), int(dx)):
    x = np.append(x, i/100)

y = np.array([])
for xVal in x:
    y = np.append (y,math.sin(xVal))

plt.scatter (x,y)

