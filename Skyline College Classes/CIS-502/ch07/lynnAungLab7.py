##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab Assignment 7 - Data Munging
#  Application: Regular Expressions
#  Description: This program will use regex
#               expressions to check whether 
#               a string is valid or not.
#  Development Environment:  Anaconda
#  Version: Python 3.7
#  Solution File:  lynnAungLab7.py
#  Testing Validation: Pasted Tested Output 
#  Date: 03/18/25

import re
import sys

# Named constants
NUM_DATES = 5
MIN_YEAR = 1000
MAX_YEAR = 2999

def is_leap_year(year):
    """
    Determine if the given year is a leap year.
    
    Parameters
    -------------------------
        year (int): The year to check
        
    Returns
    -------------------------
        bool: True if it's a leap year, False otherwise
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_valid_date(month, day, year):
    """
    Validate if the given date is valid according to the Gregorian calendar.
    
    Parameters
    -------------------------
        month (int): Month (1-12)
        day (int): Day
        year (int): Year
        
    Returns
    -------------------------
        bool: True if the date is valid, False otherwise
    """
    # Check year range
    if not (MIN_YEAR <= year <= MAX_YEAR):
        return False
    
    # Days in each month (index 0 is a placeholder)
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Adjust February for leap years
    if is_leap_year(year):
        days_in_month[2] = 29
    
    # Check if day is valid for the given month
    return 1 <= month <= 12 and 1 <= day <= days_in_month[month]

def convert_date(date_string):
    """
    Convert a date from mm/dd/yyyy format to month day, year format.
    
    Parameters
    -------------------------
        date_string (str): Date in mm/dd/yyyy format
        
    Returns
    -------------------------
        str: Converted date in 'month day, year' format
        
    Raises
    -------------------------
        SystemExit: If the date format is invalid
    """
    # Regex to check the date
    date_pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/([1-9]\d{3})$'
    
    # Check if the date matches the required format
    match = re.match(date_pattern, date_string)
    if not match:
        print(f"Error: Invalid date format. Please use mm/dd/yyyy format.")
        raise SystemExit("Invalid date format")
    
    # Get month, day, and year components
    month_str, day_str, year_str = match.groups()
    
    # Convert strings to integers to check easily
    month = int(month_str)
    day = int(day_str)
    year = int(year_str)
    
    # Check the date
    if not is_valid_date(month, day, year):
        print(f"Error: {month_str}/{day_str}/{year_str} is not a valid date.")
        raise SystemExit("Invalid date")
    
    # List of month names 
    month_names = [
        "", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    # Get the month name based on the month number
    month_name = month_names[month]
    
    # Format cleanly
    converted_date = f"{month_name} {day_str}, {year_str}"
    
    return converted_date


"""Main function to run the date converter program."""
print("Date Format Converter")
print("-------------------------")
print("This program converts dates from mm/dd/yyyy format to month day, year format.")
print("This program require 2 digits be supplied for mm and dd.")
print("\n")

# Use a for loop rocess multiple dates
for i in range(1, NUM_DATES + 1):
    try:
        print(f"Test Case {i}:")
        date_input = input("Enter a date (mm/dd/yyyy): ")
        
        # Convert the date
        converted_date = convert_date(date_input)
        
        # Display the result
        print(f"The converted date is: {converted_date}")
        print()
        
    except SystemExit as e:
        print(f"Program terminated: {e}")
        print()
        # For the last test case, we allow the program to continue
        if i < NUM_DATES:
            continue
        else:
            break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print()


'''
Date Format Converter
-------------------------
This program converts dates from mm/dd/yyyy format to month day, year format.
This program require 2 digits be supplied for mm and dd.

Test Case 1:
Enter a date (mm/dd/yyyy): 01/01/2018
The converted date is: January 01, 2018

Test Case 2:
Enter a date (mm/dd/yyyy): 03/18/2025
The converted date is: March 18, 2025

Test Case 3:
Enter a date (mm/dd/yyyy): 10/08/2005
The converted date is: October 08, 2005

Test Case 4:
Enter a date (mm/dd/yyyy): 02/29/2028
The converted date is: February 29, 2028

Test Case 5:
Enter a date (mm/dd/yyyy): 51/03/1997
Error: Invalid date format. Please use mm/dd/yyyy format.
Program terminated: Invalid date format
'''
