# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 19:35:17 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

def Simpsons (xn,yn):
    h = xn[1]-xn[0]
    total = yn[0] + yn[-1]
    for i in range (1, len(xn)-1):
        if  i%2 == 0:
            total += 2*yn[i]
        else:
            total += 4*yn[i]
    total *= h/3
    return total

xn = np.linspace(1,5,5)
yn = np.array([0.3,10.289025,81.365379,352.880135,1101.20529])
xn2 = np.linspace (1,5,3)
yn2 = np.array([0.3,81.356379,1101.205259])
print (xn2)
error = (Simpsons (xn,yn)-Simpsons(xn2,yn2))/15
print (error)

plt.plot (xn,yn,xn2,yn2)

