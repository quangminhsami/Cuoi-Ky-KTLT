import numpy as np
import sys

from Basic_operator_matrix import *
from File_matrix import *

# 5. Tính ma trận nghịch đảo của ma trận vuông khả nghịch

# 5.1 Dùng phương pháp Gauss-Jordan
def invGaussJordanMatrix(mat):

    mat = file_Matrix()

    # Kiểm tra điều kiện ma trận khả nghịch
    if np.linalg.det(mat) != 0:
        n = mat.shape[0]

        # tìm ma trận bổ sung 
        a = np.zeros((n,2*n))

        for i in range(n):        
            for j in range(n):
                if i == j:
                    a[i][j+n] = 1

        for i in range(n):        
            for j in range(n):
                a[i][j] = mat[i][j]

        #Biến đổi Gauss Jordan

        for i in range(n):
            if a[i][i] == 0.0:
                sys.exit('ERROR')
            for j in range(n):
                if i != j:
                    ratio = a[j][i] / a[i][i]

                    for k in range(2*n):
                        a[j][k] = a[j][k] - ratio * a[i][k]

        # Cho vế trái thành mt đơn vị

        for i in range(n):
            temp = a[i][i]
            for j in range(2*n):
                a[i][j] = a[i][j] / temp

        print("ma trận nghịch đảo:")
        for i in range(n):
            for j in range(n, 2*n):
                print(round(a[i][j], 3), end='\t')
            print()

        print("==================================================================== \n")
    else:
        print("Ma trận ko khả nghịch, ko tồn tại ma trận nghịch đảo!")

# 5.2. Dùng thư viện Numpy 
def invNumpyMatrix(mat):
    nRows = mat.shape[0]
    nCols = mat.shape[1]
    if nRows != nCols :
        print("Không phải ma trận vuông !, không thể tính định thức và ma trận nghịch đảo \n")
    else:
        if detMatrix(mat) == 0:
            print("Định thức của ma trận bằng 0, nên ma trận không khả nghịch! \n")
        else:
            return np.linalg.inv(mat)

# 16. Giải hệ đại số tuyến tính 

# 16.1 Giải hệ đại số tuyến tính bằng phương pháp gauss
def solveLinearGauss(mat, b):

    print("PP Gauss")
    print("=========================================")
    # Nhập ma trận bổ sung/ liên kết a 

    mat = file_Matrix() # chọn mat 4 mới giải đc hệ

    # Hạng của ma trận a
    rank_a = np.linalg.matrix_rank(mat)
                
    print("1.INPUT: \n")
    print("Ma trận mat: \n", mat)

    n = mat.shape[0]

    # Ma trận hệ số b
    b = np.zeros((n,n),float)

    for i in range(n):        
        for j in range(n):
            b[i][j] = mat[i][j]

    # hạng của ma trận b
    rank_b = np.linalg.matrix_rank(b)

    # Tạo ma trận 0
    x = np.zeros(n,float)

    # Biến đổi Gauss 
    for i in range(n):
        if mat[i][i] == 0.0:
            sys.exit('ERROR')
            
        for j in range(i+1, n):
            ratio = mat[j][i] / mat[i][i]
        
            for k in range(n+1):
                mat[j][k] = mat[j][k] - ratio * mat[i][k]

    print("Vay ta thu duoc ma tran \n", mat)

    # Tìm nghiệm
    x[n-1] = mat[n-1][n] / mat[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = mat[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - mat[i][j] * x[j]
        
        x[i] = x[i] / mat[i][i]

    print("\nKet qua:")
    for i in range(n):
        print('X%d = %0.7f' %(i,x[i]), end = '\t')
    

    # Đánh giá
    if rank_a == rank_b:
        if rank_a == n:
            print("\n2.OUTPUT: Co nghiem duy nhat\n")
        else:
            print("\n2.OUTPUT: Co vo so nghiem \n")
    else:
        print("\n2.OUTPUT: Vo nghiem \n")

        # return np.linalg.solve(mat, b)

# 16.2 : Giải hệ đại số tuyến tính bằng thư viện numpy