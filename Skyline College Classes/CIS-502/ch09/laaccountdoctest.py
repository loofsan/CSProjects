##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab # 9 - Object Oriented Application 
#  Application: Managing Customer Bank Accounts 
#  Description: Account Doctest Example
#  Development Environment: Anaconda 
#  Version: Python 3.7
#  File: laaccountdoctest.py
#  Date: 4/14/2025
##

"""Account class definition for doctest demonstration."""
from decimal import Decimal

class Account:
    """Account class for demonstrating doctest."""
    
    def __init__(self, name, balance):
        """Initialize an Account object.
        
        >>> account1 = Account('John Green', Decimal('50.00'))
        >>> account1.name
        'John Green'
        >>> account1.balance
        Decimal('50.00')
        
        The balance argument must be greater than or equal to 0.
        >>> account2 = Account('John Green', Decimal('-50.00'))
        Traceback (most recent call last):
        ...
        ValueError: Initial balance must be >= to 0.00.
        """
        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')
            
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        """Deposit money to the account.
        
        >>> from decimal import Decimal
        >>> account1 = Account('John Green', Decimal('50.00'))
        >>> account1.deposit(Decimal('25.00'))
        >>> account1.balance
        Decimal('75.00')
        
        >>> account1.deposit(Decimal('-25.00'))
        Traceback (most recent call last):
        ...
        ValueError: amount must be positive.
        """
        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')
            
        self.balance += amount
        
    def withdraw(self, amount):
        """Withdraw money from the account.
        
        >>> from decimal import Decimal
        >>> account1 = Account('John Green', Decimal('50.00'))
        >>> account1.withdraw(Decimal('25.00'))
        >>> account1.balance
        Decimal('25.00')
        
        >>> account1.withdraw(Decimal('-5.00'))
        Traceback (most recent call last):
        ...
        ValueError: amount must be positive.
        
        >>> account1.withdraw(Decimal('100.00'))
        Traceback (most recent call last):
        ...
        ValueError: amount must be <= to balance.
        """
        # if amount is greater than balance, raise an exception
        if amount > self.balance:
            raise ValueError('amount must be <= to balance.')
        elif amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')
            
        self.balance -= amount

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
'''
Trying:
    account1 = Account('John Green', Decimal('50.00'))
Expecting nothing
ok
Trying:
    account1.name
Expecting:
    'John Green'
ok
Trying:
    account1.balance
Expecting:
    Decimal('50.00')
ok
Trying:
    account2 = Account('John Green', Decimal('-50.00'))
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: Initial balance must be >= to 0.00.
ok
Trying:
    from decimal import Decimal
Expecting nothing
ok
Trying:
    account1 = Account('John Green', Decimal('50.00'))
Expecting nothing
ok
Trying:
    account1.deposit(Decimal('25.00'))
Expecting nothing
ok
Trying:
    account1.balance
Expecting:
    Decimal('75.00')
ok
Trying:
    account1.deposit(Decimal('-25.00'))
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: amount must be positive.
ok
Trying:
    from decimal import Decimal
Expecting nothing
ok
Trying:
    account1 = Account('John Green', Decimal('50.00'))
Expecting nothing
ok
Trying:
    account1.withdraw(Decimal('25.00'))
Expecting nothing
ok
Trying:
    account1.balance
Expecting:
    Decimal('25.00')
ok
Trying:
    account1.withdraw(Decimal('-5.00'))
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: amount must be positive.
ok
Trying:
    account1.withdraw(Decimal('100.00'))
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: amount must be <= to balance.
ok
1 items had no tests:
    __main__
3 items passed all tests:
    3 tests in __main__.Account.deposit
    5 tests in __main__.Account.__init__
    5 tests in __main__.Account.withdraw
13 tests in 4 items.
13 passed and 0 failed.
Test passed.
'''