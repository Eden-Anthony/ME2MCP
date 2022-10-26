# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:16:08 2022

@author: TonyE
"""

import numpy as np

def StrainGaugeRosette(en1, theta1, en2, theta2, en3, theta3):
    principalstrains = np.array([en1, en2, en3])
    A1 = [0.5+0.5*np.cos(2*theta1*np.pi/180), 0.5-0.5*np.cos(2*theta1*np.pi/180), 0.5*np.sin(2*theta1*np.pi/180)]
    A2 = [0.5+0.5*np.cos(2*theta2*np.pi/180), 0.5-0.5*np.cos(2*theta2*np.pi/180), 0.5*np.sin(2*theta2*np.pi/180)]
    A3 = [0.5+0.5*np.cos(2*theta3*np.pi/180), 0.5-0.5*np.cos(2*theta3*np.pi/180), 0.5*np.sin(2*theta3*np.pi/180)]
    A = np.array([A1, A2, A3])
    Ainv = np.linalg.inv(A)
    referencestrains = Ainv.dot(principalstrains)
    return(referencestrains)

def ConstitutiveEquations(ex, ey, Yxy, E, G, v):
    σx = E*(ex+v*ey)/(1-v**2)*10**-3 #MPa
    σy = E*(ey+v*ex)/(1-v**2)*10**-3 #MPa
    τxy = G*Yxy*10**-3 #MPa
    return(σx,σy,τxy)

def NormalStrain(ex, ey, Yxy, theta):
    en = 0.5*(ex+ey)+0.5*(ex-ey)*np.cos(2*theta*np.pi/180)+\
    0.5*Yxy*np.sin(2*theta*np.pi/180)
    round(en,2)
    return(en)

def PrincipalStrain(ex, ey, Yxy):
    e1 = 0.5*(ex+ey) + 0.5*((ex-ey)**2+Yxy**2)**0.5
    e2 = 0.5*(ex+ey) - 0.5*((ex-ey)**2+Yxy**2)**0.5
    ang1 = 0.5*np.arctan(Yxy/(ex-ey))
    ang2 = ang1+np.pi/2
    ang1 *= 180/np.pi
    ang2 *= 180/np.pi
    x = NormalStrain(ex, ey, Yxy, ang1)
    if round(e1, 2) == round(x, 2):
        val = [[round(e1,2),round(ang1,2)], [round(e2,2),round(ang2,2)]]
    else:
        val = [[round(e1,2),round(ang2,2)], [round(e2,2),round(ang1,2)]]
    return(val)

# aluminium alloy properties
E = 55.73 #GPa
G = 21.43 #GPa
v = 0.3
# all strains are listed in units of microstrain

# strain gauges 4,5,6
en4 = -0.4157
en5 = -6.0902
en6 = 19.0546
theta4 = 90
theta5 = 45
theta6 = 0
(ex,ey,Yxy) = StrainGaugeRosette(en4, theta4, en5, theta5, en6, theta6) #μm/m
print (ConstitutiveEquations(ex, ey, Yxy, E, G, v)) #MPa