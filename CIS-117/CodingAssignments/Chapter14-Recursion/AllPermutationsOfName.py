def print_all_permutations(permList, nameList):
    if len(nameList) == 0:
        # Base case: If nameList is empty, print the permutation list
        print(", ".join(permList))
    else:
        # Recursive case: Generate permutations by fixing each name in turn
        for i in range(len(nameList)):
            # Choose the i-th name to be added to the permutation list
            newPermList = permList + [nameList[i]]
            # Remaining names after removing the chosen name
            remainingNames = nameList[:i] + nameList[i+1:]
            # Recursively generate permutations with remaining names
            print_all_permutations(newPermList, remainingNames)

if __name__ == "__main__": 
    nameList = input().split(' ')
    permList = []
    print_all_permutations(permList, nameList)