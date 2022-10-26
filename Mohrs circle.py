# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:24:37 2021

@author: TonyE
"""

import math

def Mohrs(sx,sy):
    s1 = 0.5*(sx[0]+sy[0])+0.5*math.sqrt((sx[0]-sy[0])**2+4*(sx[1])**2)
    s2 = 0.5*(sx[0]+sy[0])-0.5*math.sqrt((sx[0]-sy[0])**2+4*(sx[1])**2)
    tmax = (s1-s2)/2
    theta = math.degrees(2*sx[1]/(sx[0]-sy[0]))/2
    print ("s1 = ", s1, "\ns2 = ",s2, "\ntmax = ", tmax, "\ntheta = ", theta , " " , str(theta+90))
    
Mohrs ([20,-30],[10,30])