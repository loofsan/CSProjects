##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab # 9 - Object Oriented Application 
#  Application: Managing Customer Bank Accounts 
#  Description: Test driver for Account, SavingsAccount and 
# CheckingAccount classes
#  Development Environment: Anaconda
#  Version: Python 3.7
#  File: lalab9.py
#  Date: 4/14/2025
##

"""
Test driver for Account, SavingsAccount and CheckingAccount classes.

This module provides testing for the Account class hierarchy implementation,
demonstrating the inheritance relationship between Account and its subclasses.

>>> from decimal import Decimal
>>> # Import with the correct file names that include your initials
>>> from laaccount import Account
>>> from lasavingsaccount import SavingsAccount
>>> from lacheckingaccount import CheckingAccount

# Test the base Account class
>>> account1 = Account("John Doe", Decimal('1000.00'))
>>> account1.name
'John Doe'
>>> account1.balance
Decimal('1000.00')
>>> account1.deposit(Decimal('500.00'))
>>> account1.balance
Decimal('1500.00')
>>> account1.withdraw(Decimal('200.00'))
>>> account1.balance
Decimal('1300.00')

# Test the SavingsAccount class
>>> savings1 = SavingsAccount("Jane Smith", Decimal('2000.00'), Decimal('0.05'))
>>> savings1.name
'Jane Smith'
>>> savings1.balance
Decimal('2000.00')
>>> savings1.interest_rate
Decimal('0.05')
>>> interest = savings1.calculate_interest()
>>> interest
Decimal('100.00')
>>> savings1.deposit(interest)  # Add interest to the account
>>> savings1.balance
Decimal('2100.00')

# Test the CheckingAccount class
>>> checking1 = CheckingAccount("Bob Johnson", Decimal('1500.00'), Decimal('1.50'))
>>> checking1.name
'Bob Johnson'
>>> checking1.balance
Decimal('1500.00')
>>> checking1.fee
Decimal('1.50')
>>> checking1.deposit(Decimal('500.00'))  # Should charge a fee
>>> checking1.balance  # 1500 + 500 - 1.50 = 1998.50
Decimal('1998.50')
>>> checking1.withdraw(Decimal('300.00'))  # Should charge a fee
>>> checking1.balance  # 1998.50 - 300 - 1.50 = 1697.00
Decimal('1697.00')

# Test error handling
>>> try:
...     account2 = Account("Test User", Decimal('-100.00'))
... except ValueError as e:
...     print(e)
Initial balance must be >= to 0.00.

>>> try:
...     account1.deposit(Decimal('-50.00'))
... except ValueError as e:
...     print(e)
amount must be positive.

>>> try:
...     account1.withdraw(Decimal('5000.00'))  # More than balance
... except ValueError as e:
...     print(e)
amount must be <= to balance.
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Test run validation output (commented out):
'''
Trying:
    from decimal import Decimal
Expecting nothing
ok
Trying:
    from laaccount import Account
Expecting nothing
ok
Trying:
    from lasavingsaccount import SavingsAccount
Expecting nothing
ok
Trying:
    from lacheckingaccount import CheckingAccount
Expecting nothing
ok
Trying:
    account1 = Account("John Doe", Decimal('1000.00'))
Expecting nothing
ok
Trying:
    account1.name
Expecting:
    'John Doe'
ok
Trying:
    account1.balance
Expecting:
    Decimal('1000.00')
ok
Trying:
    account1.deposit(Decimal('500.00'))
Expecting nothing
ok
Trying:
    account1.balance
Expecting:
    Decimal('1500.00')
ok
Trying:
    account1.withdraw(Decimal('200.00'))
Expecting nothing
ok
Trying:
    account1.balance
Expecting:
    Decimal('1300.00')
ok
Trying:
    savings1 = SavingsAccount("Jane Smith", Decimal('2000.00'), Decimal('0.05'))
Expecting nothing
ok
Trying:
    savings1.name
Expecting:
    'Jane Smith'
ok
Trying:
    savings1.balance
Expecting:
    Decimal('2000.00')
ok
Trying:
    savings1.interest_rate
Expecting:
    Decimal('0.05')
ok
Trying:
    interest = savings1.calculate_interest()
Expecting nothing
ok
Trying:
    interest
Expecting:
    Decimal('100.00')
ok
Trying:
    savings1.deposit(interest)
Expecting nothing
ok
Trying:
    savings1.balance
Expecting:
    Decimal('2100.00')
ok
Trying:
    checking1 = CheckingAccount("Bob Johnson", Decimal('1500.00'), Decimal('1.50'))
Expecting nothing
ok
Trying:
    checking1.name
Expecting:
    'Bob Johnson'
ok
Trying:
    checking1.balance
Expecting:
    Decimal('1500.00')
ok
Trying:
    checking1.fee
Expecting:
    Decimal('1.50')
ok
Trying:
    checking1.deposit(Decimal('500.00'))
Expecting nothing
ok
Trying:
    checking1.balance
Expecting:
    Decimal('1998.50')
ok
Trying:
    checking1.withdraw(Decimal('300.00'))
Expecting nothing
ok
Trying:
    checking1.balance
Expecting:
    Decimal('1697.00')
ok
Trying:
    try:
        account2 = Account("Test User", Decimal('-100.00'))
    except ValueError as e:
        print(e)
Expecting:
    Initial balance must be >= to 0.00.
ok
Trying:
    try:
        account1.deposit(Decimal('-50.00'))
    except ValueError as e:
        print(e)
Expecting:
    amount must be positive.
ok
Trying:
    try:
        account1.withdraw(Decimal('5000.00'))
    except ValueError as e:
        print(e)
Expecting:
    amount must be <= to balance.
ok
1 items had no tests:
    __main__
1 items passed all tests:
   30 tests in __main__.__doc__
30 tests in 2 items.
30 passed and 0 failed.
Test passed.
'''