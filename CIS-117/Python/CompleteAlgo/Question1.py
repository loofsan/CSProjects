#Solution 1

myList = [1,2,3,5,5]

def solution():
    hashSet = set()
    for num in myList:
        if num in hashSet:
            return True
        hashSet.add(num)
    return False

#Solution 2
def solution2():
    return len(myList) != len(set(myList))
    

