# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 13:16:46 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

#RS-455PA-15205
Vnom = 14.4
wNoLoad = 20200*np.pi/60
TStall = 863*10**-3
INoLoad = 2.7
IStall = 125



T = np.linspace(0,TStall, 1000)
I = np.zeros(1000)
n = np.zeros(1000)
w = np.zeros(1000)

gradTw = -wNoLoad/TStall
gradTI = IStall/ TStall

I = T * gradTI + INoLoad
w = T * gradTw + wNoLoad
P = w* T

for i in range (0,1000):
    n[i] = P[i]/(Vnom*I[i]) *100
        


plt.plot(T,I)
plt.plot(T,w)
plt.plot (T,P)
plt.plot (T,n)

maxPower = max(P)
natMaxPower = n[np.argmax(P)+1]
PatMaxn = P[np.argmax(n)+1]
TatMaxn = T[np.argmax(n)+1]
watMaxn = w [np.argmax(n)+1]