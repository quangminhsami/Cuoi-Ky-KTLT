def ioMatrix():
    nRows = int(input("Nhập số hàng: "))
    nCols = int(input("Nhập số cột: "))
 
    mat = []

    for i in range(nRows):		 
        a = []
        for j in range(nCols):	
            a.append(float(input()))
        mat.append(a)


    for i in range(nRows):
        for j in range(nCols):
            print(mat[i][j], end = " ")
        print()
