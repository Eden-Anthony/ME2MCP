# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 18:05:43 2022

@author: TonyE
"""

import matplotlib.pyplot as plt

#Image reading

im = plt.imread('Banksy.jpg')
dim = im.shape

#iterate through each pixel
for x in range (dim[1]):
    for y in range (dim[0]):
        # check if within upper triangle
        #lead diagonal line
        y1 = lambda x1: -((dim[0]-1)/(dim[1]-1))*x1 + dim[0]-1
        #reverse diagonal line
        y2 = lambda x2: ((dim[0]-1)/(dim[1]-1))*x2
        #make em blue
        if (y< y1(x)) and (y< y2(x)):
            im[y,x,:] = [0,0,im[y,x,2]]
            #print('yuh')
        #make em red
        elif (y > y1(x)) and (y > y2(x)):
            im[y,x,:] = [im[y,x,0],0,0]
            #print (im[x,y,:])
            
plt.imshow(im)
plt.show()