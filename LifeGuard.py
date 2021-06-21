import numpy as np
import os
import math

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
correct_ratings_input_path = os.path.join(THIS_FOLDER, 'CorrectRatingsInput.csv')

f = open("1.in", "r")
numbers = []
nb_pairs = 0
i = 0
for num in f.read():
    if num != '\n' and num != ' ':
        # print(int(num))
        if i == 0:
            nb_pairs = int(num)
        else:
            numbers.append(int(num))
        i += 1

print(i)
print(nb_pairs)
print(numbers)

#matrix = np.zeros((nb_pairs, 2))
matrix = np.array(numbers)
matrix = matrix.reshape((nb_pairs, 2))
print(matrix)














# input = np.loadtxt("1.in", dtype='int', delimiter='\n')
# print(input)

# with open('1.in', 'r') as f:
#    l = [[int(num) for num in line.split('\n')] for line in f if line.strip() != " " ]
# print(l)
