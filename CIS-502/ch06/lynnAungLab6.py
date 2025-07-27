##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab # 6 - Pandas
#  Application: Frequency Distributions
#  Description: This program will get me started
#               using the methods for getting the 
#               data into a DataFrame and for analyzing 
#               the data.
#  Development Environment:  Anaconda
#  Version: Python 3.7
#  Solution File:  lynnAungLab6.py
#  Testing Validation: Pasted Tested Output 
#  Date: 03/11/25

import pandas as pd

temps = {
    'Maxine': [98.6, 96.9, 97.7], 
    'James': [98.9, 100.3, 101.1], 
    'Amanda': [98.5, 98.3, 98.7]
}

# Create a dataframe
dataFrame = pd.DataFrame(temps, index=["Morning", "Afternoon", "Evening"])

# Print Maxine's column only
print("\nPrinting the column of temperature readings for 'Maxine'") 
print(dataFrame.Maxine)
print("\n\n")

# Print 'Morning' row only
print("Printing the row of 'Morning' temperature readings")
print(dataFrame.loc["Morning"])
print("\n\n")

# Print 'Morning' and 'Evening'
print("Printing the rows for 'Morning' and 'Evening' temperature readings")
print(dataFrame.loc[["Morning", "Evening"]])
print("\n\n")

# Print columns for 'Amanda' and 'Maxine'
print("Printing the columns of temperature readings for 'Amanda' and 'Maxine'")
print(dataFrame[["Amanda", "Maxine"]])
print("\n\n")

# Print 'Amanda' and 'Maxine' for 'Morning' and 'Afternoon'
print("Printing the elements for 'Amanda', and 'Maxine', in the 'Morning' and 'Afternoon'")
print(dataFrame[["Amanda", "Maxine"]].loc[['Morning', 'Afternoon']])
print("\n\n")

# Use dataframe's describe method()
print("Using the describe method to provide temperatures' descriptive statistics.")
print(dataFrame.describe())
print("\n\n")

# Transpose the dataframe and print out a transposed version
print("Printing transposed temperatures")
print(dataFrame.T)
print("\n\n")

# Print out the dataframe with the columns sorted
print("Printing temperatures with sorted columns")
print(dataFrame.sort_index(axis=1))
print("\n\n")



'''
Testing Run Validation


Printing the column of temperature readings for 'Maxine'
Morning      98.6
Afternoon    96.9
Evening      97.7
Name: Maxine, dtype: float64



Printing the row of 'Morning' temperature readings
Maxine    98.6
James     98.9
Amanda    98.5
Name: Morning, dtype: float64



Printing the rows for 'Morning' and 'Evening' temperature readings
         Maxine  James  Amanda
Morning    98.6   98.9    98.5
Evening    97.7  101.1    98.7



Printing the columns of temperature readings for 'Amanda' and 'Maxine'
           Amanda  Maxine
Morning      98.5    98.6
Afternoon    98.3    96.9
Evening      98.7    97.7



Printing the elements for 'Amanda', and 'Maxine', in the 'Morning' and 'Afternoon'
           Amanda  Maxine
Morning      98.5    98.6
Afternoon    98.3    96.9



Using the describe method to provide temperatures' descriptive statistics.
          Maxine       James  Amanda
count   3.000000    3.000000     3.0
mean   97.733333  100.100000    98.5
std     0.850490    1.113553     0.2
min    96.900000   98.900000    98.3
25%    97.300000   99.600000    98.4
50%    97.700000  100.300000    98.5
75%    98.150000  100.700000    98.6
max    98.600000  101.100000    98.7



Printing transposed temperatures
        Morning  Afternoon  Evening
Maxine     98.6       96.9     97.7
James      98.9      100.3    101.1
Amanda     98.5       98.3     98.7



Printing temperatures with sorted columns
           Amanda  James  Maxine
Morning      98.5   98.9    98.6
Afternoon    98.3  100.3    96.9
Evening      98.7  101.1    97.7
'''