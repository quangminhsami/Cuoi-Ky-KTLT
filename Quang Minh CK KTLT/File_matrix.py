import numpy as np

# nhập ma trận từ file
def file_Matrix():
    print("Chọn 0 để nhập ma trận mat từ file \n")
    print("Chọn 1 để nhập ma trận mat1 từ file \n")
    print("Chọn 2 để nhập ma trận mat2 từ file \n")
    print("Chọn 3 để nhập ma trận mat3 từ file \n")
    print("Chọn 4 để nhập ma trận mat4 từ file \n")
    choose = int(input(""))

    if choose == 0:
        mat = np.loadtxt('B:/KTLT thầy Nam/Quang Minh CK KTLT/matrix.txt', dtype = float)
        print("Ma trận mat : \n ", mat)
        return mat

    if choose == 1:
        mat1 = np.loadtxt('B:/KTLT thầy Nam/Quang Minh CK KTLT/matrix 1.txt', dtype = float)
        print("Ma trận mat 1 : \n ", mat1)
        return mat1

    if choose == 2:
        mat2 = np.loadtxt('B:/KTLT thầy Nam/Quang Minh CK KTLT/matrix 2.txt', dtype = float)
        print("Ma trận mat 2 : \n ", mat2)
        return mat2
    
    if choose == 3:
        mat3 = np.loadtxt('B:/KTLT thầy Nam/Quang Minh CK KTLT/matrix 3.txt', dtype = float)
        print("Ma trận mat 3 : \n ", mat3)
        return mat3
    
    if choose == 4:
        mat4 = np.loadtxt('B:/KTLT thầy Nam/Quang Minh CK KTLT/matrix 4.txt', dtype = float)
        print("Ma trận mat 4 : \n ", mat4)
        return mat4
    
    b = np.array([1,2,3])

