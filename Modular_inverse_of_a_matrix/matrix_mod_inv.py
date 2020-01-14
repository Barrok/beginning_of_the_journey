from sympy import *
from numpy import linalg
import numpy as np

#Function that finds modular inverse of number x
def modinv(x, mod):
    for y in range(mod):
        z = x * y
        if (z % mod) == 1:
            break
    else:
        raise ValueError('%d has no inverse mod %d' % (x, mod))
    return  y

#Let our matrix be 2x2
M = np.array('your list/matrix').reshape(2,2).T

#Determinant of M matrix
detM = np.linalg.det(M) % mod

#Modular inverse of determinant of M matrix
invdetM = modinv(int(detM))

#Adjugate matrix of M matrix
adjM = Matrix(M).adjugate()

#The rest is simple multiplication in modulo
invM = (invdet * adjM) % mod

#If you want to check if matrix was inversed right:
#We need unit matrix, our matrix is 2x2, so unit has to be the same order
unit_m = [[1, 0],
          [0, 1]]

#If it says true, then algorithm works right
print((np.dot(invM, M) % mod == unit_m).all())