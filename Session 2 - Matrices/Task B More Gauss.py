# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:59:42 2021

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

# Gaussian Elimination

def Gauss (A, b):
    #Make A into an upper triangular
    newA = A
    newb = b
    shape = np.shape(A)
    rows = shape[0]
    columns = shape[1]
    currentRow = 0
    for colNum in range (0, columns):
        quotient = newA[currentRow,colNum]
        pivotRow = np.array(newA[currentRow,:])
        for rowNum in range (currentRow+1, rows):
            row = np.array(newA[rowNum,:])
            pivot = A[rowNum, colNum]
            #print (row,"\n", quotient,"\n", rowAbove,"\n", pivot)
            row = row - (pivot/quotient)*pivotRow
            newb[rowNum] = newb[rowNum] - (pivot/quotient)*b[rowNum-1]
            newA[rowNum,:] = row
        currentRow += 1
    #solve for x
    x = b
    for xi in range (x.size-1, 0, -1):
        total = b[xi]/ A[xi,xi]
        for j in range (xi, x.size-1):
            total -= -(A[xi, j] /A[xi,xi])
        x[xi] = total
        # print (x)
    return x

#1
# f1 = lambda x: -(4/3)*x +0.5
# f2 = lambda x: -(4/3)*x + 1/8

# x = np.linspace (0,1,100)
# y1 = f1(x)
# y2 = f2(x)

# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.show()

# A = np.array([[4,3],[8,6]])
# b = np.array([[1],[2]])

# print (Gauss(A,b), np.linalg.det(A))

#2
A1 = np.array([[400,-201],[-800,401]])
b1 = np.array([[200],[-200]])

A2 = np.array([[401,-201],[-800,401]])
b2 = np.array([[200],[-200]])

print (Gauss (A1,b1),Gauss (A2,b2))