import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

#First parameter is the position of the column or row
#Second parameter is the elements
#Third Parameter is defining if it will be added as column or row
#row: axis=0, column = axis=1

# newTwoDArray = np.insert(twoDArray, 3, [[1,2,3,4]], axis=0)
# print(newTwoDArray)

newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)