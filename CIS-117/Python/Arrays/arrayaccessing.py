from array import *

#Array Traversal
arr1 = array('i', [1,2,3,4,5,6])

def accessElement(array, index):
    if index >= len(array):
        print("There is not enough element.")
    else:
        print(array[index])


accessElement()