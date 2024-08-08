from hashlib import new
import numpy as np

arr1 = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(arr1)

new2DArray = np.delete(arr1, 1, axis=1)
print(new2DArray)
