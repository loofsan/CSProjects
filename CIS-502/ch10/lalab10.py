##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab Assignment 10 - Metaclass Usage Application
#  Application: Interpolating camelCase into snake_case
#  Description: This program will use metaclasses 
#               and use Python's __prepare__() method 
#               of every object type.
#  Development Environment:  Anaconda
#  Version: Python 3.7
#  Solution File:  lalab10.py
#  Testing Validation: Pasted Tested Output 
#  Date: 04/20/25



from case_user import User

user = User("Lynn", "T. Aung")

print(user.getDisplayName())
print(user.get_display_name())
print(user.greetUser())
print(user.greet_user())


'''
Testing Run Validation

Lynn T. Aung
Lynn T. Aung
Hello Lynn T. Aung!
Hello Lynn T. Aung!
'''