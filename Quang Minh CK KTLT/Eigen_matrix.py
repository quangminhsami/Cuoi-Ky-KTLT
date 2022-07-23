import numpy as np

# 12. Giá trị riêng, vector riêng 

def eigen(mat):
    eigenvalue, eigenvector = np.linalg.eig(mat)

    eigen_vector = eigenvector.T

    # giá trị riêng
    print("giá trị riêng : \n ", eigenvalue)

    # vector riêng
    for i in range(eigenvector.shape[0]):
        print("vector riêng ứng với trị riêng {0} là : {1}".format(eigenvalue[i], eigen_vector[i]))
