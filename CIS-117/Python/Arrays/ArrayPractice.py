from array import *
# 1. Create an array and traverse

arr1 = array("i", [1,2,3,4,5,6,7,8,9])

print("Step 1")
for i in arr1:
    print(i)

# 2. Access individual elements through indexes

print("Step 2")
print(arr1[0])

# 3. Append any value to the array using append() method
#Append only adds value to the end of the array

print("Step 3")
arr1.append(10)
print(arr1)

# 4. Insert value in an array using insert() method

print("Step 4")
arr1.insert(10, 11)
print(arr1)

# 5. Extend python array using extend() method

print("Step 5")
arr2 = array("i", [12,13,14])
arr1.extend(arr2)
print(arr1)

# 6. Add items from list into array using fromlist() method

print("Step 6")
tempList = [20, 21, 22]
arr1.fromlist(tempList)
print(arr1)

# 7. Remove any array element using remove() method

print("Step 7")
arr1.remove(21)
print(arr1)

# 8. Remove last array element using pop() method

print("Step 8")
arr1.pop()
print(arr1)

# 9. Fetch any element through its index using index() method

print("Step 9")
print(arr1.index(4))

# 10. Reverse a python array using reverse() method

print("Step 10")
arr1.reverse()
print(arr1)

# 11. Get array buffer information through buffer_info() method

print('Step 11')
print(arr1.buffer_info())

# 12. Check for number of occurrences of an element using count() method
#Counting how many times an element appears in an array

print("Step 12")
print(arr1.count(2))

# 13. Convert array to string using tostring() method

print("Step 13")
strTemp = arr1.tobytes()
print(strTemp)

ints = array('i')
ints.frombytes(strTemp)
print(ints)

# 14. Convert array to a python list with same elements using tolist() method

print('Step 14')
print(arr1.tolist())

# 15. Append a string to char array using fromstring() method

print("Step 15")

# 16. Slice Elements from an array
print("Step 16")
print(arr1[0:4])
