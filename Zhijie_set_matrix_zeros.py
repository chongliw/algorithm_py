__author__ = "Zhijie Huang"

import numpy as np


# this function sets those columns or rows contaning zero to be zeros.

def setmatrixzeros(matrix):
    m = len(matrix)
    n = len(matrix[0])
    firstrow = False
    firstcolumn = False
    for j in range(n):
        if matrix[0][j] == 0:
            firstrow = True
    for i in range(m):
        if matrix[i][0] == 0:
            firstcolumn = True
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, m):
        if matrix[i][0] == 0:
            matrix[i][:] = 0
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(m):
                matrix[i][j] = 0
    if firstrow:
        matrix[0][:] = 0
    if firstcolumn:
        for i in range(m):
            matrix[i][0] = 0
    return matrix


if __name__ == "__main__":
    #    matrix  = np.array( [[ 1,2,4,0,5], [0,1,2,3,4], [ 2,3,4,5,6]] )
    matrix = np.array(
        [[1, 2, 3, 4, 0, 3, 4, 5], [2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 0, 6, 8], [2, 3, 4, 5, 6, 9, 0, 7],
         [1, 2, 3, 4, 5, 6, 7, 8]])
    print(matrix)
    newmatrix = setmatrixzeros(matrix)
    print(newmatrix)
