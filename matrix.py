from display import *

"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

m = [[1, 2, 3, 1], [2, 3, 4, 1], [3, 3, 2, 1]]

# print the matrix such that it looks like
# the template in the top comment
def print_matrix( matrix ):
    if len(matrix) == 0:
        return
    ctr = 0
    while ctr < len(matrix[0]):        
        s = ""
        for i in matrix:
            s += str( i[ctr]) + " "
        print(s)
        ctr += 1

# turn the paramter matrix into an identity matrix
# you may assume matrix is square
def ident( matrix ):
    ctr = 0
    while ctr < len(matrix):
        for i in range(0, len(matrix)):
            matrix[ctr][i] = 0
        matrix[ctr][ctr] = 1
        ctr += 1
    return matrix


# returns list containing num col of matrix
def get_col(matrix , num):
    retL = []
    for i in matrix[num]:
        retL.append(i)
    return retL

# returns list containing num row of matrix
def get_row (matrix, num):
    retL = []
    for i in matrix:
        retL.append(i[num])
    return retL


# multiply m1 by m2, modifying m2 to be the product
# m1 * m2 -> m2
# assuming m1 is a square
def matrix_mult( m1, m2 ):
    numcols = len(m2)
    numrows = len(m1[0])
    cctr = 0
    while (cctr < numcols):
        col = get_col(m2, cctr)
        rctr = 0
        while rctr < numrows:
            row = get_row(m1, rctr)
            n = 0
            s = 0
            while n < len(row):
                s += (row[n] * col[n])
                n += 1
            m2[cctr][rctr] = s
            rctr += 1
        #row = get_row(m1, cctr)
        cctr += 1
    return m2

m1 = [[3, 2, 1], [5, 7, 4], [2, 2, 1]]
m2 = [[1, 1, 1], [1, 1, 1]]
print("m1:")
print_matrix(m1)
print("m2:")
print_matrix(m2)
print("mult m1 * m2:")
print_matrix(matrix_mult(m1, m2))
#print_matrix(m2)

# new matrix function
def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m


# add edge to matrix
# edges is a list of edges
def add_edge(edges, matrix):
    for i in edges:
        e = i
        if len(e) == 3:
            e.append(1)
        matrix.append(e)
    return matrix

# testing add
print("Testing add...")

m3 = [[1, 2, 2, 1], [3, 2, 2, 1], [4,4,4,1]]
print("m3:")
print_matrix(m3)
add_edge([[3, 3, 3], [3, 4, 4, 1]], m3)
print("Adding edges to m3")
print_matrix(m3)


