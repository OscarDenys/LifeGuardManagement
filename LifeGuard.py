import numpy as np
import os
import math

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
correct_ratings_input_path = os.path.join(THIS_FOLDER, 'CorrectRatingsInput.csv')

f = open("1.in", "r")
numbers1 = []
nb_pairs1 = 0
i = 0
for num in f.read():
    if num != '\n' and num != ' ':
        if i == 0:
            nb_pairs1 = int(num)
        else:
            numbers1.append(int(num))
        i += 1

matrix1 = np.array(numbers1)
matrix1 = matrix1.reshape((nb_pairs1, 2))


def find_next_a(mat, a, loss):
    overlap = mat[(mat[:, 1] >= a) & (mat[:, 0] < a)]
    print(overlap)
    while overlap.size != 0:
        loss.append(a - max(overlap[:, 0]))
        a = min(overlap[:, 0])
        overlap = mat[(mat[:, 1] >= a) & (mat[:, 0] < a)]
        print(overlap)
    return a


def find_next_b(mat, a):
    


# check case of complete overlap


def fire_lifeguard(mat):
    loss = []
    covered_time = 0
    b = max(mat[:, 1])
    b_row_ind = np.argmax(mat[:, 1])
    a = mat[b_row_ind, 0]
    #  print(b, b_ind, a)

    a = find_next_a(mat, a, loss)
    covered_time += (b - a)












fire_lifeguard(matrix1)




