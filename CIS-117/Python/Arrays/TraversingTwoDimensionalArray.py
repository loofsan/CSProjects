# Traversing Two Dimensional Array

import numpy as np

arr1 = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(arr1)

def traverseArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverseArray(arr1)
