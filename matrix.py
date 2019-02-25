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

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    rows = []
    for i in range(len(matrix[0])):
        cols = []
        for col in range(len(matrix)):
            cols.append(str(matrix[col][i]))
            row = " ".join(cols)
            rows.append(row)
        newmatrix = "\n".join(rows)
    print(newmatrix)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult(m1, m2):
    oldrow = []
    oldcol = []
    for i in range(4):
        row = [c[i] for c in m1]
        oldrow.append(row)
    for c in range(len(m2)):
        col = m2[c][:]
        oldcol.append(col)
    rows = len(oldrow)
    cols = len(oldcol)
    for i in range(rows):
        for j in range(cols):
            m2[j][i] = dproduct(oldrow[i], oldcol[j])

def dproduct(r,c):
    return sum([r[z] * c[z] for z in range(len(r))])



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
