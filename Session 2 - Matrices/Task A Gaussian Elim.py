# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 09:32:44 2021

@author: ae1220
"""
import numpy as np
# Gaussian Elimination

# Task A
def Gauss(A,b):
    # number of equations
    n = len(b)
    # eliminate the unknowns, from first to (n-1)th unknown, to form an upper triangular matrix
    for i in range(0,n-1):
        # eliminate the i-th unknown from the (i+1)th row downwards
        # i.e. set the zeros in column i.
        for j in range(i+1,n):
            # eliminate on row j
            # A(i,i) is the pivot coefficient
            p = A[j,i] / A[i,i]
            # compute the new elements of row j in matrix A
            # use slicing
            #A[j,:] = A[j,:] - p * A[i,:]
            # or, alternatively, loop for every cell of row j
            for k in range(i,n):
                A[j,k] = A[j,k] - p * A[i,k]
            # compute the new element of row j in vector b
            b[j] = b[j] - p * b[i]
    # verify A has been reduced to a triangular matrix
    #print(A)
    # evauate, by back substitution the solution
    # start from the last unknown and go upward till the first unknown
    x = np.zeros(n)
    for i in range(n-1,-1,-1):
        # contribution from b (right hand side of the equation)
        x[i] = b[i] / A[i,i]
        # contribution from the other (already evaluated) unknowns
        # (within the left hand side of the equation)
        for k in range(i+1,n):
            x[i] = x[i] - A[i,k] * x[k] / A[i,i]

    return x

A = np.array([[8, -2, 1, 3], [1, -5, 2, 1],[-1, 2, 7, 2],[2 ,-1, 3, 8]],dtype=float)
b = np.array([9, -7, -1, 5],dtype=float)

print(Gauss(A,b))

"""def Gauss (A, b):
    # Make A into an upper triangular
    newA = np.copy(A).astype(float)
    newb = np.copy(b).astype(float)
    shape = np.shape(A)
    rows = shape[0]
    columns = shape[1]
    currentRow = 0
    for colNum in range (0, columns-1):
        quotient = newA[currentRow,colNum]
        pivotRow = np.array(newA[currentRow,:])
        for rowNum in range (currentRow+1, rows):
            row = np.array(newA[rowNum,:])
            pivot = newA[rowNum, colNum]
            #print (row,"\n", quotient,"\n", rowAbove,"\n", pivot)
            row = row - (pivot/quotient)*pivotRow
            newb[rowNum] = newb[rowNum] - (pivot/quotient)*b[rowNum-1]
            newA[rowNum,:] = row
        currentRow += 1
    # solve for x
    x = b.copy().astype(float)
    for xi in range (x.size-1, -1, -1):
        total = b[xi]/ newA[xi,xi]
        for j in range (xi+1, x.size-1):
            total -= -(newA[xi, j] /newA[xi,xi])
        x[xi] = total
        # print (x)
    return x"""
   


