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
#  Development Environment:  Anaconda
#  Version: Python 3.7
#  Solution File:  lynnAungLab4.py
#  Test File: lynnAungLab4test.py
#  Date: 02/18/25


from statistics import variance, stdev
from typing import List, Iterator

# Constants
MIN_SCORE = 0
MAX_SCORE = 20
DECIMAL_PLACES = 2

def validate_score(score: float) -> bool:
    """
    Check user input

    Parameters
    -------------------------
    float
        Scores to check

    Returns
    -------------------------
    bool
        True if scores are valid, false if not.
    """
    return MIN_SCORE <= score <= MAX_SCORE

def calculate_average(*scores: float, round_to: int = DECIMAL_PLACES) -> float:
    '''
    Calculate average.

    Parameters
    -------------------------
    int
        *scores: Variable number of score arguments
    int
        round_to: Number of decimal places to round to (default: DECIMAL_PLACES)

    Returns
    -------------------------
    float
        The average value from the input

    '''
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), round_to)

def get_score_iterator(scores: List[float]) -> Iterator[float]:
    '''
    Converts a list of scores into an iterator.

    Parameters
    -------------------------
    list
        scores (List[float]): List of scores

    Returns
    -------------------------
    Iterator Object
        Iterator[float]: Iterator object for the scores
    
    '''
    return iter(scores)

def calculate_bonus_impact(scores: List[float]) -> dict:
    '''
    Calculates statistics and potential bonus impact for a set of scores.

    Parameters
    -------------------------
    list
        scores (List[float]): List of lab scores

    Returns
    -------------------------
    Dictionary
        Dictionary containing calculated statistics and bonus impact
    '''
    if not scores:
        return {
            "average": 0.0,
            "variance": 0.0,
            "std_dev": 0.0,
            "min_score": 0.0,
            "potential_bump": 0.0
        }
    
    # Use lambda for finding minimum score
    min_score = min(scores, key=lambda x: float(x))
    avg_score = calculate_average(*scores)
    
    # Calculate potential improvement
    potential_bump = round(avg_score - min_score, DECIMAL_PLACES) if avg_score > min_score else 0.0
    
    return {
        "average": avg_score,
        "variance": round(variance(scores), DECIMAL_PLACES),
        "std_dev": round(stdev(scores), DECIMAL_PLACES),
        "min_score": min_score,
        "potential_bump": potential_bump
    }

def get_user_scores() -> List[float]:
    """
    Prompts user for lab scores until they're done entering values.

    Parameters
    -------------------------
    None

    Returns
    -------------------------
    list
        List[float]: List of valid lab scores entered by user
    """
    scores = []
    while True:
        try:
            score_input = input("Enter lab score (or press Enter to finish): ").strip()
            if not score_input:
                break
                
            score = float(score_input)
            if not validate_score(score):
                print(f"Score must be between {MIN_SCORE} and {MAX_SCORE}")
                continue
                
            scores.append(score)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    return scores

def main():
    # Main program
    print("Welcome to the Course Grade Calculator!")
    print(f"Enter lab scores between {MIN_SCORE} and {MAX_SCORE}")
    
    scores = get_user_scores()
    if not scores:
        print("No scores entered.")
        return
        
    # Create score iterator for display
    score_iter = get_score_iterator(scores)
    print("\nScores entered:", ", ".join(str(score) for score in score_iter))
    
    # Calculate and display statistics
    results = calculate_bonus_impact(scores)
    
    print(f"\nStatistics:")
    print(f"Average Score: {results['average']}")
    print(f"Variance: {results['variance']}")
    print(f"Standard Deviation: {results['std_dev']}")
    print(f"Minimum Score: {results['min_score']}")
    
    if results['potential_bump'] > 0:
        print(f"\nPotential bonus impact:")
        print(f"By replacing your lowest score ({results['min_score']}) with")
        print(f"your average ({results['average']}), you could improve by {results['potential_bump']} points!")
    else:
        print("\nYour lowest score is already at or above your average.")
        print("A bonus assignment may not improve your overall score.")

if __name__ == "__main__":
    main()