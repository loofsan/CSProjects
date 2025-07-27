##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab # 5 - Frequency Distributions
#  Application: Frequency Distributions
#  Description: This program will use lists and dictionaries to organize, 
#               process and analyze data
#  Testing Validation: A copy of my test run from console 
#  Development Environment:  Anaconda
#  Version: Python 3.7
#  Solution File:  lynnAungLab5.py
#  Test File: lynnAungLab5test.py
#  Date: 03/04/25

from lynnAungLab5 import compute_frequency

def main():
    print("Computing Frequency Distributions Tests")
    print("==================================================\n")

    testDataSequences = [
        [3,1,1,5,3,1,2,2,3,5,3,5,4,4,6,7,6,7,5,7,8,3,8,2,3,4,1,5,6,7],
        ["alice", "bob", "alice", "charlie", "dave", "eve", "alice", "frank",
        "grace", "heidi", "bob", "judy", "alice", "eve", "frank", "grace", 
        "heidi", "ivan", "judy", "bob", "charlie", "dave", "eve", "frank", 
        "grace", "heidi", "ivan", "judy", "alice", "bob"]
    ]
    testRanges = [
        [0,9],
        {"alice", "bob", "charlie", "dave", "eve", "frank", "grace", "heidi", "ivan", "judy"}
    ]

    for i in range(2):
        print(f"Test {i + 1}: \n")
        compute_frequency(testDataSequences[i], testRanges[i])
        print("Testing Finished\n\n")



if __name__ == "__main__":
    main()


"""
Computing Frequency Distributions Tests
==================================================

Test 1: 

ITEM  FREQUENCY
1         4
2         3
3         6
4         3
5         5
6         3
7         4
8         2
Testing Finished


Test 2: 

ITEM  FREQUENCY
alice     5
bob       4
charlie   2
dave      2
eve       3
frank     3
grace     3
heidi     3
ivan      2
judy      3
Testing Finished
"""