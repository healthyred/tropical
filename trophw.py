import random
import math
import fileinput

MATRIX_SIZE = 2
MAX_INT = 100#1000000000
MIN_INT = 0
MAX_COEFF = 9#1000
MIN_COEFF = 0
MAX_DEGREE = 10
MIN_DEGREE = 1

def genMatrix():
    return [[random.randint(MIN_INT, MAX_INT) for y in range(0,MATRIX_SIZE)] for x in range(0,MATRIX_SIZE)]

def genPoly():
    degree = random.randint(MIN_DEGREE, MAX_DEGREE)
    poly = []
    for i in range(0, degree + 1):
        coeff = [[random.randint(MIN_COEFF, MAX_COEFF) for y in range(0,MATRIX_SIZE)] for x in range(0,MATRIX_SIZE)]
        poly.append(coeff)
    return poly

def evalPoly(poly, mat, add, mul):
    result = [[MAX_INT * MAX_INT] * MATRIX_SIZE] * MATRIX_SIZE
    for i in range(0, len(poly)):
        coeff = poly[i]
        powMat = matExp(mat, i, mul)
        term = mul(coeff, powMat)
        result = add(result, term)
    return result

def matExp(mat, power, mul):
    if(power == 0):
        return mat
    elif(power % 2 == 0):
        return mul(matExp(mat, power/2, mul), matExp(mat, power/2, mul))
    else:
        return mul(matExp(mat, power-1, mul), mat)

def tropAdd(A, B):
    return [[min(A[x][y], B[x][y]) for y in range(0, MATRIX_SIZE)] for x in range(0, MATRIX_SIZE)]

def matAdd(A, B):
    return [[(A[x][y] + B[x][y]) for y in range(0, MATRIX_SIZE)] for x in range(0, MATRIX_SIZE)]

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

def strToMat(msg):
    msg = msg.strip()
    msg = msg[:100]
    msgPad = msg + ('a' * (MATRIX_SIZE*MATRIX_SIZE - len(msg)))
    msgMat = [[ord(msgPad[(MATRIX_SIZE*x):(MATRIX_SIZE*x) + MATRIX_SIZE][y]) for y in range(0,MATRIX_SIZE)] for x in range(0,MATRIX_SIZE)]
    return msgMat

def matToStr(mat):
    chrMat = [[chr((mat[x][y] % 128)) for y in range(0, MATRIX_SIZE)] for x in range(0,MATRIX_SIZE)]
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

def encodeMsg(msg):
    print("Step 1: Choose two public matrices.\n")
    A = genMatrix()
    print("Matrix A:\n" + matToPrint(A))
    B = genMatrix()
    print("Matrix B:\n" + matToPrint(B))

    p1 = genPoly()
    p2 = genPoly()
    print("\nStep 2: Each party generates two private polynomials.\n")
    print("Alice generates the polynomials:\nP1:\n" + polyToPrint(p1) +"\nP2:\n" + polyToPrint(p2))

    q1 = genPoly()
    q2 = genPoly()
    print("Bob generates the polynomials:\nQ1:\n" + polyToPrint(q1) + "\nQ2:\n" + polyToPrint(q2))

    msg = msg[:100]

    p1a = evalPoly(p1, A, tropAdd, tropMul)
    p2b = evalPoly(p2, B, tropAdd, tropMul)
    q1a = evalPoly(q1, A, tropAdd, tropMul)
    q2b = evalPoly(q2, B, tropAdd, tropMul)

    aliceSend = tropMul(p1a, p2b)
    bobSend = tropMul(q1a, q2b)

    print("\nStep 3: Each party computes the value of their first polynomial at A, and second polynomial at B.\n")
    print("Alice sends the matrix P1(A)P2(B):\n" + matToPrint(aliceSend));
    print("Bob sends the matrix Q1(A)Q2(B):\n" + matToPrint(bobSend));

    Ka = tropMul(tropMul(p1a, bobSend), p2b)
    Kb = tropMul(tropMul(q1a, aliceSend), q2b)

    print("\nStep 4: Each part computes the shared matrix:\n")
    print("Alice computes P1(A)Q1(A)Q2(B)P2(B):\nBob computes Q1(A)P1(A)P2(B)Q2(B):\nSince tropical matrix multiplication is commutative this results in the shared matrix:\n" + matToPrint(Ka))

    negKa = [[-y for y in x] for x in Ka]

    msgMat = strToMat(msg)
    sent = matAdd(msgMat, Ka)
    recieved = matAdd(sent, negKa)
    recStr = matToStr(recieved)

    print("The matrix sent is:\n" + matToPrint(sent))
    print("Ciphertext:\n" + str(matToStr(sent)))
    print("Plaintext:\n" + recStr)

if __name__ == "__main__":
    for line in fileinput.input():
        encodeMsg(line)
