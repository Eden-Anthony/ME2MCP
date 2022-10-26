# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:44:08 2021

@author: ae1220
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

delta = 0.1
pi = math.pi
x= np.linspace (-2*pi, 2*pi, int(((4*pi)/delta)))
y = np.linspace ( -1* pi, 2*pi, int(((3*pi)/delta)))
xg, yg = np.meshgrid (x,y)
print( xg,yg)

f = np.sin(xg) *np.cos (yg)
g = np.cos(xg) *np.sin (yg)

s = f + g
p = np.multiply(f, g)

#Task C
#surface plot for s(x,y)
ax = plt.axes (projection ='3d' )
ax.plot_surface (xg,yg, s)
plt.show()
#contour plot for s(x,y)
plt.contour (xg,yg, s)
plt.show()

#surface plot for p (x,y)
ax3 = plt.axes (projection ='3d' )
ax3.plot_surface (xg,yg, p)
plt.show()
#contour plot for p (x,y)
plt.contour (xg,yg, p)
plt.show()

t = 0
r = f * math.exp(-0.5 *t)
ax4 = plt.axes (projection ='3d' )
ax4.plot_surface (xg,yg, r)
plt.show()

t = 5
r = f * math.exp(-0.5 *t)
ax5 = plt.axes (projection ='3d' )
ax5.plot_surface (xg,yg, r)
plt.show()