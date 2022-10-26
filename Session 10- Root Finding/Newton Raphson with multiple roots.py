# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:06:02 2022

@author: TonyE
"""
import numpy as np
import matplotlib.pyplot as plt

#note that for this function, f(x) and f'(x) have to be pre-programmed
def f(x):
    
    #return 25 - ((6*np.pi*(x**2)) - (np.pi*(x**3)))/3
    
    return (x**3) - (2*(x**2)) - (4*x) + 8

""""def f(x):
    
    return (x**2) + ((x-2)**3) - 4"""

def f_prime(x, dx):
    
    return (f(x+dx)-f(x))/dx

def myNewton(x0, dx, m, e):
    
    #create an artificial error to start the loop
    error = 10*e
    xn = x0
    
    x = np.linspace(x0-10,x0+20,int((x0+10)*10))
    y = f(x)
    
    #plot f(x) against f(x)
    plt.figure(figsize=(15,10))
    plt.plot(x, y,'g')
    
    #draw x axis
    plt.axhline(0, color='black')
    
    i = 0
    
    while error > e:
        
        i += 1
        #need to store previous x coordinate
        xp = xn
        
        if f_prime(xn,dx)== 0:
            
            return xn
        
        else:
            
            xn = xp - (m*(f(xp)/f_prime(xp,dx)))
            
            #visualise what Newton Raphson is doing
            plt.plot([xp,xn],[f(xp), 0],'r')
            plt.plot([xp,xp], [0, f(xp)], 'b--')
        
        #error is difference between new and old x
        error = abs((xn-xp)/xp)
    
    plt.show()
    
    return 'The Newton Raphson approximates the following as the root of the function: {} after {} iterations'.format(xn, i)
    
x0 = 1.2
m = 2
e = 0.001
myNewton(x0,0.1, m, e)