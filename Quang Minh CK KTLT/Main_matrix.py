import numpy as np

from File_matrix import *
from IO_matrix import *
from Basic_operator_matrix import *
from Basic_matrix import *
from Check_matrix import *
from Decomposition_matrix import *
from Find_matrix import *
from Eigen_matrix import *

# main
# ============================================================================
while True:
    print("_" * 87 + "\n")
    print("\t" * 2 + "CHÀO MỪNG CÁC BẠN ĐẾN VỚI THƯ VIỆN VỀ MA TRẬN" + "\t" * 2)
    print("_" * 87 + "\n")

    print("\n Chọn 1 để nhập ma trận từ bàn phím \n")
    print("Chọn 2 để nhập ma trận từ file \n")

    select = int(input())

    if select == 1:
        # Nhập ma trận từ bàn phím
        print("Nhập ma trận mat  từ bàn phím : \n")
        mat = ioMatrix()
        print("Nhập ma trận mat 1 từ bàn phím : \n")
        mat1 = ioMatrix()
        print("Nhập ma trận mat 2 từ bàn phím : \n")
        mat2 = ioMatrix()
        print("Nhập ma trận mat 3 từ bàn phím : \n")
        mat3 = ioMatrix()
        print("Nhập ma trận mat 4 từ bàn phím : \n")
        mat4 = ioMatrix()

    if select == 2:
        # nhập ma trận từ file
        mat = file_Matrix()
        mat1 = file_Matrix()
        mat2 = file_Matrix()
        mat3 = file_Matrix()
        mat4 = file_Matrix()
        b = np.array([1,2,3])

        print("\n Chọn '1' để thực hiện các phép toán cơ bản với ma trận \n")
        print("Chọn '2' để thức hiện các thao tác cơ bản với ma trận \n")
        print("Chọn '3' để kiểm tra tính chất của ma trận \n")
        print("Chọn '4' để tìm nghiệm hệ đại số tuyến tính, ma trận nghịch đảo \n")
        print("Chọn '5' để tìm giá trị riêng, vector riêng \n")
        print("Chọn '6' để phân tách ma trận \n")

        choose = int(input())

        if choose == 1:

            # Các phép toán cơ bản với ma trận
            print("Chọn '1' để cộng 2 ma trận \n")
            print("Chọn '2' để trừ 2 ma trận \n")
            print("Chọn '3' để nhân 2 ma trận \n")
            print("Chọn '4' để tính định thức ma trận \n")
            print("Chọn '5' để tính chuẩn 1 ma trận \n")
            print("Chọn '6' để tính chuẩn 2  ma trận \n")
            print("Chọn '7' để tính chuẩn vô cùng ma trận \n")

            choose1 = int(input())

            if choose1 == 1:
                add = addMatrix(mat1, mat2)
                print("Tổng của 2 ma trận mat 1 và mat 2 là : \n", add)

            if choose1 == 2:
                sub = subMatrix(mat1, mat2)
                print("Hiệu của 2 ma trận mat 1 và mat 2 là : \n", sub)

            if choose1 == 3:
                mul = mulMatrix(mat1, mat2)
                print("Tích của 2 ma trận mat 1 và mat 2 là : \n", mul) 

            if choose1 == 4:
                det = detMatrix(mat)
                print("Đinh thức của ma trận mat là :", round(det, 2))

            if choose1 == 5:
                norm1 = norm1Matrix(mat)
                print("Chuẩn 1 của ma trận mat : \n", norm1)

            if choose1 == 6:
                norm2 = norm2Matrix2(mat)
                print("Chuẩn 2 của ma trận mat : \n", norm2)

            if choose1 == 7:
                norm_inf = normInfMatrix(mat)
                print("Chuẩn vô cùng của ma trận mat : \n", norm_inf)

        elif choose == 2:

            # Thao tác cơ bản với ma trận
            print("Chọn '1' để đưa ra kích thước của ma trận \n")
            print("Chọn '2' để đưa ra kích thước của ma trận \n")
            print("Chọn '3' để đưa ra ma trận đơn vị của ma trận \n")
            print("Chọn '4' để đưa ra ma trận tam giác trên của ma trận \n")
            print("Chọn '5' để đưa ra ma trận tam giác dưới của ma trận \n")
            print("Chọn '6' để đưa ra ma trận đường chéo của ma trận \n")
            print("Chọn '7' để đưa ra hạng của ma trận \n")
            
            choose2 = int(input())

            if choose2 == 1:
                shapeMatrix(mat)

            if choose2 == 2:
                trans = transMatrix(mat)
                print("Ma trận chuyển vị của ma trận mat là: \n", trans)

            if choose2 == 3:
                id = idMatrix(mat)
                print("Ma trận đơn vị của ma trận mat là : \n", id)

            if choose2 == 4:
                upper = upperMatrix(mat)
                print("Ma trận tam giác trên của ma trận mat là : \n", upper)

            if choose2 == 5:
                lower = lowerMatrix(mat)
                print("Ma trận tam giác dưới của ma trận mat là : \n", lower)

            if choose2 == 6:
                diag = diagMatrix(mat)
                print("Ma trận đường chéo của ma trận mat là : \n", diag)

            if choose2 == 7:
                rank = rankMatrix(mat)
                print("Hạng của ma trận mat là : ", rank)

        elif choose == 3:
            
        # Kiểm tra 1 vài tính chất của ma trận
            print("Chọn '1' để kiểm tra ma trận đối xứng \n")
            print("Chọn '2' để kiểm tra ma trận xác định dương \n")
            print("Chọn '3' để kiểm tra ma trận chéo trội \n")

            choose3 = int(input())

            if choose3 == 1:
                if symMatrix(mat) == True:
                    print("Ma trận mat đối xứng \n")
                else:
                    print("Ma trận mat không đối xứng \n")
            
            if choose3 == 2:
                defposMatrix(mat3)

            if choose3 == 3:
                dominantMatrix(mat)

        elif choose == 4:

            print("Chọn '1' để tìm ma trận nghịch đảo \n")
            print("Chọn '2' để tìm nghiệm đại số tuyến tính \n")

            choose4 = int(input())
            # Tìm nghiệm hệ đại số tuyến tính và ma trận nghịch đảo

            if choose4 == 1:
                inv = invGaussJordanMatrix(mat)

            if choose4 == 2:
                solveLinearGauss(mat, b)


        elif choose == 5:
            # Giá trị riêng, vector riêng
            eig = eigen(mat1)

        elif choose == 6:
            # Phân tách ma trận
            print("Chọn 1 để phân tách cholesky")
            print("Chọn 2 để phân tách SVD")

            choose6 = int(input())

            if choose6 == 1:
        
                cho = choleskyDecompostion(mat3)
            print(cho)

            if choose6 == 2:
                svd(mat)    
        
        else:
            print("Bạn có muốn tiếp tục chương trình không ? (Bấm Y để tiếp tục, Bấm N để dừng lại) \n")
            choose5 = str(input())
            if choose5 == 'Y':
                continue
            else:
                break


