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
        if i == 0:
            nb_pairs = int(num)
        else:
            numbers.append(int(num))
        i += 1



matrix = np.array(numbers)
matrix = matrix.reshape((nb_pairs, 2))














