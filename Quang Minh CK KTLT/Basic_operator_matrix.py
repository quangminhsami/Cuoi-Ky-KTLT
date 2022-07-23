import numpy as np

# 1. Cộng 2 ma trận
def addMatrix(mat1, mat2):
    n1Rows = mat1.shape[0]
    n2Rows = mat2.shape[0]
    n1Cols = mat1.shape[1]
    n2Cols = mat2.shape[1]

    if n1Rows != n2Rows or n1Cols != n2Cols:
        print("Không thể cộng 2 ma trận!")
    else:
        return mat1 + mat2 

# 2. Trừ 2 ma trận
def subMatrix(mat1, mat2):
    n1Rows = mat1.shape[0]
    n2Rows = mat2.shape[0]
    n1Cols = mat1.shape[1]
    n2Cols = mat2.shape[1]

    if n1Rows != n2Rows or n1Cols != n2Cols:
        print("Không thể trừ 2 ma trận! \n")
    else:
        return mat1 - mat2

# 3. Nhân 2 ma trận
def mulMatrix(mat1, mat2):
    n1Rows = mat1.shape[0]
    n2Rows = mat2.shape[0]
    n1Cols = mat1.shape[1]
    n2Cols = mat2.shape[1]

    if n1Cols != n2Rows or n1Rows != n2Cols:
        print("Không thể nhân 2 ma trận! \n")
    else:
        return mat1 @ mat2

# 4. Tính định thức của ma trận vuông (cần làm thuật toán)
def detMatrix(mat):
    nRows = mat.shape[0]
    nCols = mat.shape[1]
    if nRows != nCols :
        print("Không phải ma trận vuông !, không thể tính định thức \n")
    else:
        count = 0
        B = np.arange(nRows ** 2)
        B = B.reshape((nRows,nRows))
        B = np.zeros_like(B, dtype = float)
        
        for i in range(nRows):
            for j in range(nCols):
                B[i,j] = mat[i,j]
        
        for k in range(nRows):
            imax = k
            vmax = abs(B[imax, k])
            for i in range(k+1, nRows):
                if B[i,k] > vmax:
                    vmax = abs(B[i,k])
                    imax = i

            if imax != k:
                for i in range(nRows):
                    temp = B[imax, i]
                    B[imax, i] = B[k,i]
                    B[k,i] = temp
                
                count += 1

            for i in range(k+1, nRows):
                f = B[i,k] / B[k,k]
                for j in range(k+1,nCols):
                    B[i,j] -= B[k,j] * f
                B[i,k] = 0

        det = -1 ** count 
        for i in range(nRows):
            det *= B[i,i]

        return det 
            

# 4.2 Dùng thứ viện Numpy
def detNumpyMatrix(mat):
    nRows = mat.shape[0]
    nCols = mat.shape[1]
    if nRows != nCols :
        print("Không phải ma trận vuông !, không thể tính định thức \n")
    else:
        return np.linalg.det(mat)

# 13. Tính chuẩn của ma trận

# 13.1 Chuẩn 1
def norm1Matrix(mat):
    return np.linalg.norm(mat, 1)

# 13.2 Chuẩn 2
def norm2Matrix2(mat):
    return np.linalg.norm(mat, 2)

# 13.3 Chuẩn vô cùng
def normInfMatrix(mat):
    return np.linalg.norm(mat, np.inf)
