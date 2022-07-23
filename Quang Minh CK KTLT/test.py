nRows = int(input("Nhập số hàng : \n"))
nCols = int(input("Nhập số cột : \n"))

mat = [[]]
for i in range(nRows):
    for j in range(nCols):
        x = float(input("Nhập Mat[{0}][{1}] = ".format(i,j)))
        mat.append(x)

