import numpy as np
import os
import time
import math

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
matrix1_path = os.path.join(THIS_FOLDER, '1.txt')
matrix2_path = os.path.join(THIS_FOLDER, '2.txt')
matrix3_path = os.path.join(THIS_FOLDER, '3.txt')
matrix4_path = os.path.join(THIS_FOLDER, '4.txt')
matrix5_path = os.path.join(THIS_FOLDER, '5.txt')
matrix6_path = os.path.join(THIS_FOLDER, '6.txt')
matrix7_path = os.path.join(THIS_FOLDER, '7.txt')
matrix8_path = os.path.join(THIS_FOLDER, '8.txt')
matrix9_path = os.path.join(THIS_FOLDER, '9.txt')
matrix10_path = os.path.join(THIS_FOLDER, '10.txt')



def fire_lifeguard(mat):
    min_loss = 1000000000
    covered_time = 0
    mat = np.sort(mat, axis=0)
    (a1, b1) = mat[0, :]
    # print(a1, b1)
    for i in range(mat.shape[0]-1):
        a2 = mat[i + 1, 0]
        b2 = mat[i+1, 1]
        if b2 <= b1:
            min_loss = 0
            print(b1, b2)
            continue
        elif a2 <= b1:
            b1 = b2
            if (b2 - b1) < min_loss:
                min_loss = b2 - b1
        else:
            covered_time += (b1 - a1)
            a1 = a2
            b1 = b2
    if covered_time == 0:
        covered_time = b1 - a1 - min_loss
    else:
        covered_time = max(0, covered_time-min_loss)
    print(min_loss)
    print(covered_time)




matrix = np.loadtxt(matrix1_path, dtype=int)
# print(matrix.shape[0])

t0 = time.time()
fire_lifeguard(matrix)
t1 = time.time()
print('runtime: ', (t1 - t0))


