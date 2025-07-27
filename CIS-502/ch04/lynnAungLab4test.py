##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab # 4 - Your Course Grade Calculator
#  Application: Your Course Grade Calculator
#  Description: This program will reads in an indeterminate number lab 
#               scores from the user at the keyboard into a list. Then,
#               we will then calculate the average of the scores (write
#               a user-defined function to calculate this metric). Then, 
#               it will determine if the average lab score is larger 
#               than the lowest lab score.  If so, report the 'bump up' 
#               achieved by replacing this score with the average.
#  Testing Validation: A copy of my test run from console 
#  Development Environment:  Anaconda
#  Version: Python 3.7
#  Solution File:  lynnAungLab4.py
#  Test File: lynnAungLab4test.py
#  Date: 02/18/25

from lynnAungLab4 import (
    validate_score,
    calculate_average,
    get_score_iterator,
    calculate_bonus_impact,
    MIN_SCORE,
    MAX_SCORE
)

def test_score_validation():
    """Test score validation function"""
    print("\nTesting score validation:")
    test_scores = [0, 20, 15.5, -1, 21]
    for score in test_scores:
        result = validate_score(score)
        print(f"Score {score}: {'Valid' if result else 'Invalid'}")

def test_average_calculation():
    """Test average calculation with various inputs"""
    print("\nTesting average calculation:")
    test_cases = [
        [10, 15, 20],
        [0],
        [17.5, 18.5],
        []
    ]
    for scores in test_cases:
        avg = calculate_average(*scores)
        print(f"Scores {scores}: Average = {avg}")

def test_score_iterator():
    """Test score iterator creation and usage"""
    print("\nTesting score iterator:")
    scores = [10, 15, 20]
    iterator = get_score_iterator(scores)
    print("Original scores:", scores)
    print("Iterator values:", list(iterator))

def test_bonus_impact():
    """Test bonus impact calculations"""
    print("\nTesting bonus impact calculations:")
    
    # Test case 1: Normal scores
    scores = [15.0, 17.0, 19.0, 14.0]
    print("\nTest case 1 - Normal scores:", scores)
    results = calculate_bonus_impact(scores)
    for key, value in results.items():
        print(f"{key}: {value}")
    
    # Test case 2: Perfect scores
    scores = [20.0, 20.0, 20.0]
    print("\nTest case 2 - Perfect scores:", scores)
    results = calculate_bonus_impact(scores)
    for key, value in results.items():
        print(f"{key}: {value}")
    
    # Test case 3: Empty list
    scores = []
    print("\nTest case 3 - Empty list:", scores)
    results = calculate_bonus_impact(scores)
    for key, value in results.items():
        print(f"{key}: {value}")

def main():
    """Run all tests"""
    print("Starting Grade Calculator Tests")
    print("=" * 50)
    
    test_score_validation()
    test_average_calculation()
    test_score_iterator()
    test_bonus_impact()
    
    print("\nAll tests completed.")

if __name__ == "__main__":
    main()

"""
Starting Grade Calculator Tests
==================================================

Testing score validation:
Score 0: Valid
Score 20: Valid
Score 15.5: Valid
Score -1: Invalid
Score 21: Invalid

Testing average calculation:
Scores [10, 15, 20]: Average = 15.0
Scores [0]: Average = 0.0
Scores [17.5, 18.5]: Average = 18.0
Scores []: Average = 0.0

Testing score iterator:
Original scores: [10, 15, 20]
Iterator values: [10, 15, 20]

Testing bonus impact calculations:

Test case 1 - Normal scores: [15.0, 17.0, 19.0, 14.0]
average: 16.25
variance: 4.92
std_dev: 2.22
min_score: 14.0
potential_bump: 2.25

Test case 2 - Perfect scores: [20.0, 20.0, 20.0]
average: 20.0
variance: 0.0
std_dev: 0.0
min_score: 20.0
potential_bump: 0.0

Test case 3 - Empty list: []
average: 0.0
variance: 0.0
std_dev: 0.0
min_score: 0.0
potential_bump: 0.0

All tests completed.
"""
