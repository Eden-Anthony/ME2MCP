# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:49:53 2021

@author: ae1220
"""
import numpy as np
import math

def TrBaryc(r,f,rp):
    # form matrix A
    # the first two rows of A are the x and y coordinates of the three vertices
    A = np.copy(np.transpose(r))
    # third row of A is made of ones
    A = np.append(A,[[1,1,1]], axis=0)
    # form d
    # first two rows of d are the x and y coordinate of rp, third row is a one
    d = np.append(rp,1)
    # invert A and multiply by d to find the lambdas
    l = np.dot(np.linalg.inv(A),d)
    # interpolate with the lambdas
    frp = l[0]*f[0] + l[1]*f[1] + l[2]*f[2]
    return frp

N = 9
R = 5
f = np.empty([N,1])
nodes = np.empty([N,2])
connected = np.empty([N-1,3], dtype = int)
f[N-1] = [0]
nodes[N-1] = [0,0]

#find perimeter nodes
for i in range (0,N-1):
    fi = i * 2*math.pi/N
    x = R * np.cos(fi)
    y = R * np.sin(fi)
    nodes[i] = [x,y]
    f[i] = fi 
    #connect nodes, i ,i-1 and the centre node, index N-1
    if i == N-2:
        #want to connect first and last perimeter nodes
        connected[i] = [i, 0, N-1]
    else:
        connected[i] = [i, i+1 ,N-1]
        
#print ()
#interpedVals = np.ndarray([N-1,1])
interpedVals = np.empty (N-1)

#find midpoints and interpolate
for i in range (0,connected.shape[0]):
    r0 = nodes[connected[i,0]]
    r1 = nodes[connected[i,1]]
    r2 = nodes[connected[i,2]]
    # xp = (x0 + x1 + x2)/3
    xp = (r0[0] + r1[0] + r2[0])/3
    # yp = (y0 + y1 + y2)/3
    yp = (r0[1] + r1[1] + r2[1])/3
    rp = np.array ([xp,yp])
    r = np.array ([r0,r1,r2])
    ftemp = [f[connected[i,0]][0],f[connected[i,1]][0],f[connected[i,2]][0]]
    #print (r)
    #TrBaryc(r,ftemp,rp)
    interpedVals[i] = TrBaryc(r,ftemp, rp)

print (interpedVals)