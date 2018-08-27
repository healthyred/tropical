##Write a simple script that takes a matrix, and finds the tropical Eigenvalue of said matrixsize
##Within this script, we choose the size of the original random matrix, and then we run this simulation 10,000 times to find the mean eigenvalue,
##and the standard deviation of this eigenvalue

import math
import random

MATRIX_SIZE = 2
INF = float('inf')
MAX_INT = 1 #(excluseive)
MIN_INT = 0 #(inclusive)

def genMatrix():
    return [[random.random() for y in range(0, MATRIX_SIZE)] for x in range(0, MATRIX_SIZE)]

def tropAdd(A, B):
    return [[min(A[x][y], B[x][y]) for y in range(0, MATRIX_SIZE)] for x in range(0, MATRIX_SIZE)]

def matAdd(A, B):
    return [[(A[x][y] + B[x][y]) for y in range(0, MATRIX_SIZE)] for x in range(0, MATRIX_SIZE)]

def tropExp(A,n):
    #takes in a matrix and multplies it by itself n times
    A_updated = A
    for i in range(n):
        A_updated = tropMul(A_updated,A)
    return A_updated

def tropMul(A, B):
    #result should be the size of the resulting matrix
    result = [[INF] * len(B[0]) for i in range(len(B))]
    #a is a matrix, b is a matrix, assuming a and b are able to be multiplied".
    # iterate through rows of X
    for i in range(len(A)):
        #iterate through the columes of Y
        for j in range(len(B[0])):
            #iterate through rows of Y
            for k in range(len(B)):
                currentMin = result[i][j]
                candidateMin = A[i][k] + B[k][j]
                if (candidateMin < currentMin):
                    result[i][j] = candidateMin
    return result

def findEigen(A):
    """Uses linear programming algorithm to return the eigenvalue,
    λ(A), the minimumnormalized cycle length. Implements using Karp's algorithm
    """
    ##todo create a graph class with nodes
    length = len(A)
    #arbitrary J in G(A)
    j = 3
    #construct an arbitrary identity element matrix of MATRIX_SIZE of A, and then arbitraily choose the jth column
    identity_jth = identityVector(j,length) #this is the x(0)

    ##initializes the set of candidates for the eigenvalues
    candidate_values_set = []
    ##Then loop through matrix an equivalent number of times to find the columns from x(0), x(1), ... x(n)
    #print(identity_jth)

    minimum_weight_matrix = [[] for i in range(length)] #a filler column
    minimum_weight_matrix[0] = tropMul(A,identity_jth) #finds the x(1)

    for i in range(length-1):
        minimum_weight_matrix[i+1] = tropMul(A,minimum_weight_matrix[i])

    minimum_weight_matrix.insert(0,identity_jth)
    #print(minimum_weight_matrix)
    eigen = maximize(minimum_weight_matrix)
    #for i in range(len(to_min)):
        #candidate_values_set.add(max(to_min[i]))
    return eigen

def identityVector(j,n):
    """Takes in a number j, and the length of a matrix n, and returns of the jth column of an n x n
    sized identiy matrix. Note that we start counting at 1."""
    result = [[INF] for i in range(n)]
    result[j-1] = [0]
    return result

def maximize(column_matrix):
    """Takes in a minimum_weight_matrix and the first x_0, and returns a list of the possible values"""
    maxed_weighted_lengths = []
    length = len(column_matrix)
    to_manipulate = column_matrix[length-1]

    to_max = [[[] for i in range(length-1)] for j in range(length-1)]
    for i in range(len(to_manipulate)):
        for j in range(len(column_matrix[0])):
            #print(to_manipulate[i][0])
            #print(column_matrix[j][i][0])
            #print(length-1-j)
            to_max[i][j] = (to_manipulate[i][0] - column_matrix[j][i][0])/ (length-1 - j)
            #print(to_max)
    #print(max(to_max[0]))
    for i in range(len(to_max)):
        maxed_weighted_lengths.append(max(to_max[i]))
    #print(min(maxed_weighted_lengths))
    return min(maxed_weighted_lengths)

if __name__ == "__main__":

    A = [[6, 7, INF, INF],[1, 4, INF, 6],[INF, 2, 4, 5],[INF, INF, 3, 6]]

    testcase = identityVector(3,len(A))
    #print(testcase)
    x_1 = tropMul(A,testcase)
    #print(x_1)
    """
    x_2 = tropMul(A,x_1)
    print(x_2)
    x_3 = tropMul(A,x_2)
    x_4 = tropMul(A,x_3)
    print(x_3)
    print(x_4)
    """
    #print((20 - float('inf'))/4)
    print(findEigen(A))
