##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab # 9 - Object Oriented Application 
#  Application: Managing Customer Bank Accounts 
#  Description: Checking Account Class Definition
#  Development Environment: Anaconda
#  Version: Python 3.7
#  File: lacheckingaccount.py
#  Date: 4/14/2025
##

from decimal import Decimal
from laaccount import Account  # Make sure this matches your account class filename

class CheckingAccount(Account):
    """CheckingAccount class inherits from Account and adds transaction fees."""
    
    def __init__(self, name, balance, fee):
        """Initialize a CheckingAccount object.
        
        >>> from decimal import Decimal
        >>> from laaccount import Account
        >>> checking1 = CheckingAccount('Bob Johnson', Decimal('1500.00'), Decimal('1.50'))
        >>> checking1.name
        'Bob Johnson'
        >>> checking1.balance
        Decimal('1500.00')
        >>> checking1.fee
        Decimal('1.50')
        """
        super().__init__(name, balance)
        self._fee = Decimal(fee)
    
    @property
    def fee(self):
        """Return the transaction fee."""
        return self._fee
    
    def deposit(self, amount):
        """Deposit money to the account and deduct the transaction fee.
        
        >>> from decimal import Decimal
        >>> from laaccount import Account
        >>> checking1 = CheckingAccount('Bob Johnson', Decimal('1500.00'), Decimal('1.50'))
        >>> checking1.deposit(Decimal('500.00'))
        >>> checking1.balance
        Decimal('1998.50')
        """
        super().deposit(amount)
        super().withdraw(self._fee)  # Deduct fee after successful deposit
    
    def withdraw(self, amount):
        """Withdraw money from the account and deduct the transaction fee if withdrawal is successful.
        
        >>> from decimal import Decimal
        >>> from laaccount import Account
        >>> checking1 = CheckingAccount('Bob Johnson', Decimal('1500.00'), Decimal('1.50'))
        >>> checking1.withdraw(Decimal('300.00'))
        >>> checking1.balance
        Decimal('1198.50')
        
        >>> try:
        ...     checking1.withdraw(Decimal('2000.00'))
        ... except ValueError as e:
        ...     print(e)
        amount must be <= to balance.
        """
        if amount > self.balance:
            raise ValueError('amount must be <= to balance.')
        elif amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')
            
        # If we get here, withdrawal is valid, so proceed and charge fee
        super().withdraw(amount)
        
        # Only charge fee if there's enough balance remaining
        if self._fee <= self.balance:
            super().withdraw(self._fee)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)