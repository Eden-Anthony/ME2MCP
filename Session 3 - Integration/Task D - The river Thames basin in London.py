# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:11:44 2021

@author: ae1220
"""

import matplotlib.pyplot as plt

#read files
xnFile = open('xn.txt','r')
xn = xnFile.readlines()
ynFile = open('yn.txt','r')
yn = ynFile.readlines()
xsFile = open('xs.txt','r')
xs = xsFile.readlines()
ysFile = open('ys.txt','r')
ys = ysFile.readlines()

#clean files
xn = [x.strip() for x in xn]
yn = [y.strip() for y in yn]
xs = [x.strip() for x in xs]
ys = [y.strip() for y in ys]

#map to float
xn = list(map (float,xn))
yn = list(map (float,yn))
xs = list(map (float,xs))
ys = list(map (float,ys))


xnFile.close(); ynFile.close(); xsFile.close(); ysFile.close()

plt.plot (xn,yn,xs,ys)
plt.axis('equal')

#trapezium rule from previous task
def trapz (x,y):
    I = 0
    for i in range (0,len(x)-1):
        I += 0.5*(y[i]+y[i+1])*(x[i+1]-x[i])
    return (I)

area = (trapz(xn,yn)-trapz(xs,ys))/10**6

print(area , " Km^2")