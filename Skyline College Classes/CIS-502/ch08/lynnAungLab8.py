##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab Assignment 8 - Data Science - Working
#                     with CSV Files
#  Application: Class Average
#  Description: This program will use be able to read 
#               and write CSV (comma-separated values) 
#               files, a common file format for data 
#               science datasets and demonstrate CSV 
#               file processing with a Python Standard 
#               Library module.
#  Development Environment:  Anaconda
#  Version: Python 3.7
#  Solution File:  lynnAungLab8.py
#  Testing Validation: Pasted Tested Output 
#  Date: 03/23/25

import csv
from statistics import mean
import os.path

def createCSV():
    """
    Creates a CSV file with student records with first name, 
    last name, and three exam grades.
    """
    print("\n=== Create Student Records ===")
    print("==============================")
    records = []

    isValid = True
    while isValid:

        firstname = input("\nEnter student's first name: ")
        lastname = input("Enter student's last name: ")
        
        # Handle both integer and float inputs for grades
        try:
            exam1 = float(input("Enter exam 1 grade: "))
            exam2 = float(input("Enter exam 2 grade: "))
            exam3 = float(input("Enter exam 3 grade: "))
            
            # Convert to int if the grade is a whole number
            exam1 = int(exam1) if exam1.is_integer() else exam1
            exam2 = int(exam2) if exam2.is_integer() else exam2
            exam3 = int(exam3) if exam3.is_integer() else exam3
            
            records.append([firstname, lastname, exam1, exam2, exam3])
            
            # Ask if user wants to add another student
            add_more = input("Add another student? (y/n): ").lower()
            if (add_more == 'y'):
                isValid = True
            else:
                isValid = False

        except ValueError:
            print("Error: Grades must be numbers. Please try again.")
    
    # Write records to my CSV file
    with open('lagrades.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['firstname', 'lastname', 'exam1grade', 'exam2grade', 'exam3grade'])
        writer.writerows(records)

def displayData():
    """
    Reads the lagrades.csv file and displays the data 
    in a tabular format.
    """
    # Check if the csv file exists or not
    if not os.path.exists('lagrades.csv'):
        print("Error: grades.csv file not found. Please create it first.")
        return
    
    print("\n=== Student Records ===")
    print("=======================")
    
    # Read the CSV file
    with open('lagrades.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Get the header row
        
        # Calculate column widths for proper formatting
        col_widths = [max(15, len(header) + 2) for header in headers]
        
        # Display header row
        header_format = "".join(f"{header:<{col_widths[i]}}" for i, header in enumerate(headers))
        print(header_format)
        print("-" * sum(col_widths))
        
        # Display data rows
        for row in reader:
            row_format = "".join(f"{item:<{col_widths[i]}}" for i, item in enumerate(row))
            print(row_format)

def gradeReport():
    """
    Reads the grades.csv file and generates a grade report with individual and class averages.
    """
    if not os.path.exists('lagrades.csv'):
        print("Error: grades.csv file not found. Please create it first.")
        return
    
    print("\n=== Grade Report ===")
    print("====================")
    
    # Read the CSV file
    with open('lagrades.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Get the header 
        
        # Add 'average' column to the right of each student
        report_headers = headers + ['average']
        
        # Proper formatting
        col_widths = [max(15, len(header) + 2) for header in 
                      report_headers]
        
        # Output header row
        header_format = "".join(f"{header:<{col_widths[i]}}" for 
                                i, header in enumerate(report_headers))
        print(header_format)
        print("-" * sum(col_widths))
        
        # Initialize lists for calculating class average
        exam1grades = []
        exam2grades = []
        exam3grades = []
        
        # Display student data with their averages
        for row in reader:
            # Convert grade strings to numbers
            exam1 = float(row[2])
            exam2 = float(row[3])
            exam3 = float(row[4])
            
            # Add grades to lists for class average
            exam1grades.append(exam1)
            exam2grades.append(exam2)
            exam3grades.append(exam3)
            
            # Find individual average
            individual_avg = mean([exam1, exam2, exam3])
            
            # Format display \
            display_row = row + [f"{individual_avg:.2f}"]
            row_format = "".join(f"{item:<{col_widths[i]}}" for 
                                 i, item in enumerate(display_row))
            print(row_format)
        
        # Display separator
        print("-" * sum(col_widths))
        
        # Calculate and display class averages
        class_avg_row = ["Class Average", ""] 
        class_avg_row.append(f"{mean(exam1grades):.2f}")
        class_avg_row.append(f"{mean(exam2grades):.2f}")
        class_avg_row.append(f"{mean(exam3grades):.2f}")
        class_avg_row.append(f"{mean(exam1grades + exam2grades + 
                                     exam3grades) / 3:.2f}")
        
        class_avg_format = "".join(f"{item:<{col_widths[i]}}" for 
                                   i, item in enumerate(class_avg_row))
        print(class_avg_format)



"""Main function to run the class average program."""
print("Student Records CSV File")
print("-------------------------")
print("This program will Be able to read and write CSV "
"(comma-separated values) files, a common file format for "
"data science datasets.")
print("This program will demonstrate CSV file processing with"
" a Python Standard Library module.")
print("\n")

createCSV()
displayData()
gradeReport()


'''
Student Records CSV File
-------------------------
This program will Be able to read and write CSV (comma-separated values) files, a common file format for data science datasets.
This program will demonstrate CSV file processing with a Python Standard Library module.



=== Create Student Records ===
==============================

Enter student's first name: Bob
Enter student's last name: Jones
Enter exam 1 grade: 86
Enter exam 2 grade: 75
Enter exam 3 grade: 84
Add another student? (y/n): y

Enter student's first name: Sue
Enter student's last name: Smith
Enter exam 1 grade: 99
Enter exam 2 grade: 77
Enter exam 3 grade: 88
Add another student? (y/n): y

Enter student's first name: Karen
Enter student's last name: Doe
Enter exam 1 grade: 83
Enter exam 2 grade: 88
Enter exam 3 grade: 92
Add another student? (y/n): n

=== Student Records ===
=======================
firstname      lastname       exam1grade     exam2grade     exam3grade
---------------------------------------------------------------------------
Bob            Jones          86             75             84
Sue            Smith          99             77             88
Karen          Doe            83             88             92

=== Grade Report ===
====================
firstname      lastname       exam1grade     exam2grade     exam3grade     average
------------------------------------------------------------------------------------------
Bob            Jones          86             75             84             81.67
Sue            Smith          99             77             88             88.00
Karen          Doe            83             88             92             87.67
------------------------------------------------------------------------------------------
Class Average                 89.33          80.00          88.00          28.59
'''