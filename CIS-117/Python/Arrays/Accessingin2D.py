import numpy as np

arr1 = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(arr1)

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array(0)):
        print("Incorrect Index")
    else:
        print(array[rowIndex][colIndex])

accessElements(arr1, 1, 2)
