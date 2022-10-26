# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:02:01 2021

@author: ae1220
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

dx = 0.1
x = np.linspace (-5,5,int(10/dx))
y = np.linspace (-5,5,int(10/dx))

xg, yg = np.meshgrid(x,y)

#f1
plt.quiver (x, y, xg,yg)
plt.show()

#f2
plt.quiver (x,y, yg, -1*xg)
plt.show()

#f3

fx = yg/((xg**2 + yg**2))
fy = -xg/((xg**2+yg**2))
plt.quiver (x,y, fx, -1*fy)