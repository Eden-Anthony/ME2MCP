# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:44:08 2021

@author: ae1220
"""

import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

delta = 0.1
pi = math.pi
x= np.linspace (-2*pi, 2*pi, int(((4*pi)/delta)))
y = np.linspace ( -1* pi, 2*pi, int(((3*pi)/delta)))
xg, yg = np.meshgrid (x,y)

#f = np.array (len(x), len(y))
f = np.sin(xg) *np.cos (yg)
g = np.cos(xg) *np.sin (yg)

s = f + g
p = np.multiply(f, g)

print (p)

ax = plt.axes (projection ='3d' )
ax.plot_surface (xg,yg, s)

ax2 = plt.axes (projection ='3d' )
ax2.plot_surface (xg,yg, p)