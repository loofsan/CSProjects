##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab # 9 - Object Oriented Application 
#  Application: Managing Customer Bank Accounts 
#  Description: Account Class Definition
#  Development Environment: Anaconda
#  Version: Python 3.7
#  File: laaccount.py
#  Date: 4/14/2025
##


from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""
    
    def __init__(self, name, balance):
        """Initialize an Account object."""

        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self._name = name
        self._balance = balance
        
    @property
    def name(self):
        """Return the account name."""
        return self._name
    
    @property
    def balance(self):
        """Return the account balance."""
        return self._balance

    def deposit(self, amount):
        """Deposit money to the account."""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self._balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account."""

        # if amount is greater than balance, raise an exception
        if amount > self._balance:
            raise ValueError('amount must be <= to balance.')
        elif amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self._balance -= amount

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)