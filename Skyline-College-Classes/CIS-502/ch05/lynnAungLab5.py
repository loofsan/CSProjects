##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab # 5 - Frequency Distributions
#  Application: Frequency Distributions
#  Description: This program will use lists and dictionaries to organize, 
#               process and analyze data
#  Development Environment:  Anaconda
#  Version: Python 3.7
#  Solution File:  lynnAungLab5.py
#  Test File: lynnAungLab5test.py
#  Date: 03/04/25

def compute_frequency(data, valid_range):
    """
    Computes the frequency distribution of the given data sequence.

    Parameters
    -------------------------
    array
        Data sequence 

    array (int) / set (string)
        If (int), then valid_range must have two elements, the start of the range
        and the end of the range

        If (string), then valid_range can have a set of string elements,
        e.g. {"alice", "bob", "charlie", ...}

    Returns
    -------------------------
    void
        Prints the distributed frequency in a clean format
    """
    frequency = {}

    # Check if the valid_range is already a range of items or not
    # if it is not, and they are numbers, like [0, 2], make it into a set
    # Otherwise, use it as its own set
    if isinstance(valid_range, list) and len(valid_range) == 2 and all(isinstance(i, int) for i in valid_range):
        valid_range = set(range(valid_range[0], valid_range[1] + 1))
    elif isinstance(valid_range, set):
        pass  
    else:
        raise ValueError("valid_range must be either a set of strings or a list of two integers defining a numeric range")    
    
    # Traverse through the data sequence and check if each element is valid
    # if it is, count++ but if it isn't print out of range
    for elem in data:
        if elem in valid_range:
            frequency[elem] = frequency.get(elem, 0) + 1
        else:
            print(f"Warning: {elem} is out of the valid range {valid_range}")
    
    # Sort the items
    sortedDict = dict(sorted(frequency.items()))

    # Print with format
    print(f"ITEM  FREQUENCY")
    for item, count in sortedDict.items():
        print(f"{item:<9} {count}")

