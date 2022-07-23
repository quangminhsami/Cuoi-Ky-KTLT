import numpy as np
import math

from Check_matrix import *

# 15. Phân tách ma trận

# 15.1 Phân tách Cholesky (cần làm thuật toán)

# 15.1.1 Thuật toán
def choleskyDecompostion(mat):
    nRows = mat.shape[0]
    nCols = mat.shape[1]
    if nRows != nCols :
        print("Không là ma trận vuông ! \n")
    else:
        if defposMatrix(mat) == True:
            n = mat.shape[0]
            sum = 0
            S = np.arange(n**2)
            S = S.reshape((n,n))
            S = np.zeros_like(S, dtype = float)

            for i in range(n):
                for j in range(i+1):
                    sum = 0
                    for k in range(j):
                        sum += S[k,i] * S[k,j]
                    if sum == mat[i,i]:
                        break
                    if i == j:
                        S[j,i] = math.sqrt(mat[i,i] - sum)
                    else:
                        S[j,i] = (mat[j,i] - sum) / (S[j,j])
                if S[i,i] == 0:
                    break 
            return S
        else:
            print("Không tồn tại phân tách cholesky! \n")
    

# 15.1.2 Dùng thư viện Numpy
def choleskyNumpyDecompostion(mat):
    nRows = mat.shape[0]
    nCols = mat.shape[1]
    if nRows != nCols :
        print("Không là ma trận vuông ! \n")
    else:
        if defposMatrix(mat) == True:
            return np.linalg.cholesky(mat)
        else:
            print("Không tồn tại phân tách cholesky! \n")

# 15.2 Phân tách SVD (cần làm thuật toán)
def svd(mat):
    U, s, VT = np.linalg.svd(mat)

    print("Thành phần 1: \n", U)

    print("Thành phần 2: \n", s)

    print("Thành phần 3: \n", VT)
