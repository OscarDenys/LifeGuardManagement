import numpy as np
import os
import time

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Input files where converted to '.txt' because '.in' did not work.
# Thus it seemed better to include the adapted input files in the git.
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
    t0 = time.time()
    min_loss = 1000000000
    a3 = 1000000000
    b3 = 1000000000
    covered_time = 0
    mat = np.sort(mat, axis=0)
    (a1, b1) = mat[0, :]
    last_iter = False
    zero_loss = False

    for i in range(mat.shape[0]-1):
        a2 = mat[i + 1, 0]
        b2 = mat[i+1, 1]
        if i+2 == mat.shape[0]:
            last_iter = True
        else:
            a3 = mat[i + 2, 0]
            b3 = mat[i + 2, 1]

        if b2 <= b1:  # element (contiguous intervals were not assumed)
            if not zero_loss:
                min_loss = 0
                zero_loss = True

        elif a2 <= b1:  # overlap
            if not last_iter:
                if a3 <= b1:
                    if (b2 <= b3) and (not zero_loss):
                        min_loss = 0
                        zero_loss = True
                elif (a3 - b1) < min_loss:
                    min_loss = a3 - b1
            elif (b2 - b1) < min_loss:
                min_loss = b2 - b1
            b1 = b2

        else:  # jump
            covered_time += (b1 - a1)
            if (a2 - b1) < min_loss:
                min_loss = a2 - b1
            a1 = a2
            b1 = b2

    if covered_time == 0:
        covered_time = b1 - a1 - min_loss
    else:
        covered_time = max(0, covered_time-min_loss)
    t1 = time.time()
    print('     runtime: ', (t1 - t0))
    return str(covered_time)



matrix = np.loadtxt(matrix1_path, dtype=int)
print('Matrix 1 is loaded.')
out = fire_lifeguard(matrix)
outF = open("1.out", "w")
outF.write(out)
outF.write("\n")
outF.close()

matrix = np.loadtxt(matrix2_path, dtype=int)
print('Matrix 2 is loaded.')
out = fire_lifeguard(matrix)
outF = open("2.out", "w")
outF.write(out)
outF.write("\n")
outF.close()

matrix = np.loadtxt(matrix3_path, dtype=int)
print('Matrix 3 is loaded.')
out = fire_lifeguard(matrix)
outF = open("3.out", "w")
outF.write(out)
outF.write("\n")
outF.close()

matrix = np.loadtxt(matrix4_path, dtype=int)
print('Matrix 4 is loaded.')
out = fire_lifeguard(matrix)
outF = open("4.out", "w")
outF.write(out)
outF.write("\n")
outF.close()

matrix = np.loadtxt(matrix5_path, dtype=int)
print('Matrix 5 is loaded.')
out = fire_lifeguard(matrix)
outF = open("5.out", "w")
outF.write(out)
outF.write("\n")
outF.close()

matrix = np.loadtxt(matrix6_path, dtype=int)
print('Matrix 6 is loaded.')
out = fire_lifeguard(matrix)
outF = open("6.out", "w")
outF.write(out)
outF.write("\n")
outF.close()

matrix = np.loadtxt(matrix7_path, dtype=int)
print('Matrix 7 is loaded.')
out = fire_lifeguard(matrix)
outF = open("7.out", "w")
outF.write(out)
outF.write("\n")
outF.close()

matrix = np.loadtxt(matrix8_path, dtype=int)
print('Matrix 8 is loaded.')
out = fire_lifeguard(matrix)
outF = open("8.out", "w")
outF.write(out)
outF.write("\n")
outF.close()

matrix = np.loadtxt(matrix9_path, dtype=int)
print('Matrix 9 is loaded.')
out = fire_lifeguard(matrix)
outF = open("9.out", "w")
outF.write(out)
outF.write("\n")
outF.close()

matrix = np.loadtxt(matrix10_path, dtype=int)
print('Matrix 10 is loaded.')
out = fire_lifeguard(matrix)
outF = open("10.out", "w")
outF.write(out)
outF.write("\n")
outF.close()

