# searching for an element in an array
from array import *
from multiprocessing.dummy import Array

arr1 = array("i", [1,2,3,4,5,6])

def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The element does not exist in this array."
