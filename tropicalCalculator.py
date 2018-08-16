import random
import math
import fileinput

class tropicalMatrix(object):
    """classfor Tropical generator"""

    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
        self.matrix = matrix
        self.matrixsize = matrixsize
        self.min_int = MIN_INT
        self.max_int = MAX_INT

    def genMatrix():
        return [[random.randint(self.min_int, self.max_int) for y in range(0, self.matrixsize)] for x in range(0,self.matrixsize)]

    def tropAdd(A, B):
        """Tropical matrix addition function"""
        return [[min(A[x][y], B[x][y]) for y in range(0, self.matrixsize)] for x in range(0, self.matrixsize)]

    def matAdd(A, B):
        """Under the minimum convention"""
        return [[(A[x][y] + B[x][y]) for y in range(0, self.matrixsize)] for x in range(0, self.matrixsize)]

    def tropMul(A, B):
        """Tropical matrix multiplication under minimum function"""
        result = [self.max_int * self.max_int] * self.matrixsize for i in range(self.matrixsize)]
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

    def strToMat(msg):
        msg = msg.strip()
        msg = msg[:100]
        msgPad = msg + ('a' * (self.matrixsize*self.matrixsize - len(msg)))
        msgMat = [[ord(msgPad[(self.matrixsize*x):(self.matrixsize*x) + self.matrixsize][y]) for y in range(0,self.matrixsize)] for x in range(0,self.matrixsize)]
        return msgMat

    def matToStr(mat):
        chrMat = [[chr((mat[x][y] % 128)) for y in range(0, self.matrixsize)] for x in range(0,self.matrixsize)]
        msgPad = "".join(reduce(lambda x,y: x + y, chrMat))
        msg = msgPad.rstrip("a")
        return msg

    def matToPrint(mat):
        return "\n".join([" ".join([str(y) for y in x]) for x in mat])

    def polyToPrint(poly):
        result = ""
        for i in range(0, len(poly)):
            result += matToPrint(poly[i]) + "x^" + str(i) + "\n"
        return result

if __name__ == "__main__":
    for line in fileinput.input():
        encodeMsg(line)
