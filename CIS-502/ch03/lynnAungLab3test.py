##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab # 3 Test - Test For Generating Mathematical Sequences (Hailstone Sequence)
#  Application: Test For Generating Mathematical Sequences (Hailstone Sequence)
#  Description: This program will test the program lynnAungLab3.py, which computes 
#               a hailstone sequence of 'length' steps beginning with a given 
#               'start' value. Additionally, it will also output the minimum and 
#               the maximum value.
#  Testing Validation: A copy of my test run from console 
#  Development Environment:  Anaconda
#  Version: Python 3.7
#  Solution File:  lynnAungLab3.py
#  Test File: lynnAungLab3test.py
#  Date: 02/11/25

import lynnAungLab3 as lab3

test = [(7, 10), (7, 20), (-2, -10)]

for start, length in test:

    # I added this try-except so that when the user puts negative 
    # values and the main source file returns None, this program wouldn't
    # try to get the sequence, minNum and maxNum.
    sequence, minNum, maxNum = lab3.hailstone(start, length)

    print(f"Starting Value (Initial Seed): {start}\n" + 
          f"Sequence Length: {length}")
    print(f"Hailstone Sequence: ", end=" ")

    # Print out the numbers in the sequence cleanly.
    for num in range(len(sequence)):
        if (num == len(sequence) - 1):
            print(f"{sequence[num]}")
        else:
            print(f"{sequence[num]}, ", end = " ")

    print(f"Mininum value in the sequence: {minNum}\n" + 
          f"Maximum value in the sequence: {maxNum}\n")
    

'''
Test Values

- Test 1
(7, 10)
- Test 2
(7, 20)

Copy of my test runs console outut

Starting Value (Initial Seed): 7
Sequence Length: 10
Hailstone Sequence:  7,  22,  11,  34,  17,  52,  26,  13,  40,  20
Mininum value in the sequence: 52
Maximum value in the sequence: 7

Starting Value (Initial Seed): 7
Sequence Length: 20
Hailstone Sequence:  7,  22,  11,  34,  17,  52,  26,  13,  40,  20,  10,  5,  16,  8,  4,  2,  1,  4,  2,  1
Mininum value in the sequence: 52
Maximum value in the sequence: 1

'''