import numpy as np

# 6. Kích thước của ma trận
def shapeMatrix(mat):
    nRows = mat.shape[0]
    nCols = mat.shape[1]
    print("Ma trận mat có kích thước {0} x {1} \n".format(nRows, nCols))

# 7. Tìm hạng của ma trận 
def rankMatrix(mat):
    return np.linalg.matrix_rank(mat)

# 8. Chuyển vị của ma trận 
def transMatrix(mat):
    return mat.T

# 9.Ma trận đặc biệt

# 9.1 Ma trận đơn vị của ma trận vuông
def idMatrix(mat):
    nRows = mat.shape[0]
    nCols = mat.shape[1]
    if nRows != nCols :
        print("Không là ma trận vuông ! \n")
    else:
        return np.eye(nRows)

# 9.2 Ma trận tam giác trên
def upperMatrix(mat):
    nRows = mat.shape[0]
    nCols = mat.shape[1]
    if nRows != nCols :
        print("Không là ma trận vuông ! \n")
    else:
        return np.triu(mat)   

# 9.3 Ma trận tam giác dưới
def lowerMatrix(mat):
    nRows = mat.shape[0]
    nCols = mat.shape[1]
    if nRows != nCols :
        print("Không là ma trận vuông ! \n")
    else:
        return np.tril(mat)   

# 9.4 Ma trận đường chéo
def diagMatrix(mat):
    nRows = mat.shape[0]
    nCols = mat.shape[1]
    if nRows != nCols :
        print("Không là ma trận vuông ! \n")
    else:
        return np.diag(np.diag(mat))


