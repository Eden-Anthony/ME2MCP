# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:07:38 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

def func(x):
    y = np.sin(x)
    return y

def Riemann(x,y, kind='left'):
    
    plt.plot(x,y)
    
    area = 0
    
    if kind == 'left':
        
        for i in range(0,len(x)-1):
            
            width = x[i+1] - x[i]
            area += width * y[i]
            
            plt.bar(x[i], y[i], width = width, alpha = 0.5,align='edge')
            
        plt.plot(x[:-1], y[:-1], 'b.', markersize=10)

    elif kind == 'right':
                      
        for i in range(0,len(x)-1):
            
            width = x[i+1] - x[i]
            area += (x[i+1] - x[i])* y[i+1]
            
            plt.bar(x[i], y[i+1], width = width, alpha = 0.5, align='edge')
            
        plt.plot(x[1:], y[1:], 'b.', markersize=10)
                      
    elif kind == 'middle':
        
        for i in range(0,len(x)-1):
            
            x_middle = (x[i+1] + x[i])/2
            y_middle = func(x_middle)
            width = x[i+1] - x[i]
            area += y_middle * width
            
            plt.bar(x_middle, y_middle, width = width, alpha = 0.5)
            plt.plot(x_middle, y_middle, 'b.', markersize=10)
            
    plt.show()
            
    return 'The {} Riemann sum approximation gives the following area: {}'.format(kind, area)

x = np.linspace(0, np.pi/2, 10)
y = func(x)


print(Riemann(x,y, kind='left'))