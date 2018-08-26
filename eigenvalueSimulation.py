##Write a simple script that takes a matrix, and finds the tropical Eigenvalue of said matrixsize
##Within this script, we choose the size of the original random matrix, and then we run this simulation 10,000 times to find the mean eigenvalue,
##and the standard deviation of this eigenvalue

import math
import random

MATRIX_SIZE = 2
MAX_INT = 1 #(excluseive)
MIN_INT = 0 #(inclusive)

class Node(object):
    """Node class"""
    def __init__(self, data = None, children_weights = None):
        self.data = data #we will label the data corresponding to the original index of the matrix
        self.children_weights = next_node #this should be an array pointing to itself



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
    result = [[MAX_INT * MAX_INT] * MATRIX_SIZE for i in range(MATRIX_SIZE)]
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
    λ(A), the minimumnormalized cycle length.
    """
    ##todo create a graph class with nodes

    length = len(A)
    candidate_values_set = set()

    return min(candidate_values_set)

if __name__ == "__main__":
    A = genMatrix()
    print(A)
    B = genMatrix()
    print(B)
    C = tropExp(A,2)
    D = tropExp(A,3)
    print(C)
    print(D)
    print(len(C))
