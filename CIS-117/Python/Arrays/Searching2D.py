import numpy as np

arr1 = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(arr1)


def search2DArary(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return f"The value is located at index({i} {j})."
    
    return "The element is not found."

print(search2DArary(arr1, 10))