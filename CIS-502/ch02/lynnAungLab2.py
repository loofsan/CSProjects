##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab # 2 - Generating Measures of Central Tendency
#  Application: Generating Measures of Central Tendency
#  Description: This program will be using Python's statistics
#               module to generate and visualize some commonly 
#               used measures of central tendency to provide 
#               insight on user-supplied runtime revenue values. 
#  Testing Validation: A copy of my test run from console
#  Development Environment:  Anaconda
#  Version: Python 3.7
#  Solution File:  lynnAungLab2.py
#  Date: 02/02/25

from decimal import *
import statistics


def revenueAnalysis():
    '''
    This function is meant to ask the user for 
    inputs and calculate the mean, median, mode, 
    and the standard deviation off of the inputted values.

    Parameters
    -------------------------
    None

    Returns
    -------------------------
    str
        The printed statement of revenue analytics
    '''
    rev_array = []
    user_input = ''


    print("--------Revenue Analytics--------")
    print("This program will be using Python's statistics\n" + 
        "module to generate and visualize some commonly\n" + 
        "used measures of central tendency to provide insight\n" + 
        "on user-supplied runtime revenue values.")

    while(user_input != "stop"):

        user_input = input("\n(Make sure the entered value is >= 0)\n(If you " + 
                    "would like to stop, please enter 'stop')\nPlease " + 
                    "insert a revenue value to analyze: ")
        
        # if user_input is 'stop', stop the program
        if (user_input != "stop"):
            try: # try converting the user_ipnut which is str -> float
                check_input = float(user_input)
            except(ValueError):
                print("\nYou have not entered a number. Please enter a valid value.")
                continue
            # if float > 0, convert it to Decimal to round it
            if (check_input >= 0):
                decimal_input = Decimal(str(check_input))
                decimal_input = decimal_input.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                rev_array.append(decimal_input)
            else:
                print("\nYou have entered a negative value.\nPlease re-enter a valid value.")

    print("\nYou have stopped the program.\n")

    # Do the calculations for the array with decimals to find the analytics
    if rev_array:
        revenues = []
        # Change the decimal array to a normal float array to print the array out in a nice 
        # fashion
        for i in rev_array:
            i = float(i)
            revenues.append(i)
        rev_mean = statistics.mean(rev_array)
        rev_median = statistics.median(rev_array)
        rev_mode = statistics.mode(rev_array)
        rev_stdDev = statistics.stdev(rev_array)
        print("\nHere are the analytics:\n")
        print("---------------------------------\n")
        print(f"Revenues: {revenues}")
        print(f"Mean: {rev_mean:.2f}")
        print(f"Median: {rev_median:.2f}")
        print(f"Mode: {rev_mode:.2f}")
        print(f"Standard Deviation: {rev_stdDev:.2f}")
        print("\n---------------------------------")

def main():
    NUM_RUNS = 2
    i = 0 
    for i in range(NUM_RUNS):
        print(f"\nTest Run {i+1} Started\n\n\n")
        revenueAnalysis()
        print(f"\nTest Run {i+1} Over\n\n\n")
    
if __name__ == '__main__':
    main()

'''
Test Values

- Test 1
company,state,revenue
Haddad's,CA,239.5
Westfield,NJ,53.9
The Store,AZ,211.5
Hipster's,MY,11.98
Dothraki Fashions,MN,5.98
Awful's,VA,23.95
The Clothiers,TX,115.2

- Test 2
username,platform,revenue  
@GamerX,YouTube,65.57  
@FitFluencer,Instagram,142.51  
@CryptoKing,TikTok,198.44  
@FoodieQueen,Facebook,227.31  
@TechGuru,Twitch,124.38  
@VlogVoyager,YouTube,136.66  



Copy of my test runs console outut


Test Run 1 Started



--------Revenue Analytics--------
This program will be using Python's statistics
module to generate and visualize some commonly
used measures of central tendency to provide insight
on user-supplied runtime revenue values.

(Make sure the entered value is >= 0)
(If you would like to stop, please enter 'stop')
Please insert a revenue value to analyze: 239.5                                              

(Make sure the entered value is >= 0)
(If you would like to stop, please enter 'stop')
Please insert a revenue value to analyze: 53.9                                           

(Make sure the entered value is >= 0)
(If you would like to stop, please enter 'stop')
Please insert a revenue value to analyze: 211.5                                          

(Make sure the entered value is >= 0)
(If you would like to stop, please enter 'stop')
Please insert a revenue value to analyze: 11.98                                          

(Make sure the entered value is >= 0)
(If you would like to stop, please enter 'stop')
Please insert a revenue value to analyze: 5.98                                           

(Make sure the entered value is >= 0)
(If you would like to stop, please enter 'stop')
Please insert a revenue value to analyze: 23.95                                          

(Make sure the entered value is >= 0)
(If you would like to stop, please enter 'stop')
Please insert a revenue value to analyze: 115.2                                          

(Make sure the entered value is >= 0)
(If you would like to stop, please enter 'stop')
Please insert a revenue value to analyze: stop

You have stopped the program.


Here are the analytics:

---------------------------------

Revenues: [239.5, 53.9, 211.5, 11.98, 5.98, 23.95, 115.2]
Mean: 94.57
Median: 53.90
Mode: 239.50
Standard Deviation: 96.97

---------------------------------

Test Run 1 Over




Test Run 2 Started



--------Revenue Analytics--------
This program will be using Python's statistics
module to generate and visualize some commonly
used measures of central tendency to provide insight
on user-supplied runtime revenue values.

(Make sure the entered value is >= 0)
(If you would like to stop, please enter 'stop')
Please insert a revenue value to analyze: 65.57

(Make sure the entered value is >= 0)
(If you would like to stop, please enter 'stop')
Please insert a revenue value to analyze: 142.51

(Make sure the entered value is >= 0)
(If you would like to stop, please enter 'stop')
Please insert a revenue value to analyze: 198.44

(Make sure the entered value is >= 0)
(If you would like to stop, please enter 'stop')
Please insert a revenue value to analyze: 227.31

(Make sure the entered value is >= 0)
(If you would like to stop, please enter 'stop')
Please insert a revenue value to analyze: 124.38

(Make sure the entered value is >= 0)
(If you would like to stop, please enter 'stop')
Please insert a revenue value to analyze: 136.66

(Make sure the entered value is >= 0)
(If you would like to stop, please enter 'stop')
Please insert a revenue value to analyze: stop

You have stopped the program.


Here are the analytics:

---------------------------------

Revenues: [65.57, 142.51, 198.44, 227.31, 124.38, 136.66]
Mean: 149.14
Median: 139.58
Mode: 65.57
Standard Deviation: 57.16

---------------------------------

Test Run 2 Over



'''