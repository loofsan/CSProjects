##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab # 3 - Generating Mathematical Sequences (Hailstone Sequence)
#  Application: Generating Mathematical Sequences (Hailstone Sequence)
#  Description: This program will compute a hailstone sequence of 'length'
#               steps beginning with a given 'start' value. Additionally,
#               it will also output the minimum and the maximum value.
#  Testing Validation: A copy of my test run from console in the test file
#  Development Environment:  Anaconda
#  Version: Python 3.7
#  Solution File:  lynnAungLab3.py
#  Test File: lynnAungLab3test.py
#  Date: 02/11/25

def hailstone(startNum: int, seqLength: int):
    '''
    This program will compute a hailstone sequence of 'length'
    steps beginning with a given 'start' value. Additionally,
    it will also output the minimum and the maximum value.

    Parameters
    -------------------------
    startNum: int
        This is the starting value to compute the 
        hailstone sequence on. The starting seed.

    seqLength: int
        This is the length of the hailstone sequence. 

    Returns
    -------------------------
    list
        The hailstone sequence as a list of integers.

    int (max value)
        The maximum number in the sequence.

    int (min value)
        The minimum number in the sequence.

    '''
    # Raise error flag when the input is a negative number
    if startNum <= 0:
        raise ValueError("Start value must be a positive integer.\n" + 
                         "Start value cannot be 0.")
    if seqLength <= 0:
        raise ValueError("Sequence Length must be a positive integer.\n" + 
                         "Sequence Length cannot be 0.")

    hailstoneArr = [startNum]

    # Loop through the sequence length range 
    # to add all the numbers to the hailstone array
    # -1 from the sequence length because we already added the 
    # starting value. 
    for x in range(seqLength - 1):
        # I used the startNum variable to compute on because I didn't need 
        # to make another variable
        if (startNum % 2 == 0):
            startNum //= 2
        else:
            startNum = (startNum * 3) + 1
        hailstoneArr.append(startNum)

    # Loop through the hailstone array to print all
    # the values cleanly
    return hailstoneArr, max(hailstoneArr), min(hailstoneArr)

'''

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
