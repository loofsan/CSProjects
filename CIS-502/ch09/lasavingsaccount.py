##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab # 9 - Object Oriented Application 
#  Application: Managing Customer Bank Accounts 
#  Description: Savings Account Class Definition
#  Development Environment: Anaconda
#  Version: Python 3.7
#  File: lasavingsaccount.py
#  Date: 4/14/2025
##


from decimal import Decimal
from laaccount import Account 

class SavingsAccount(Account):
    """SavingsAccount class inherits from Account and adds interest calculation."""
    
    def __init__(self, name, balance, interest_rate):
        """Initialize a SavingsAccount object.
        
        >>> from decimal import Decimal
        >>> from laaccount import Account
        >>> savings1 = SavingsAccount('Jane Smith', Decimal('2000.00'), Decimal('0.05'))
        >>> savings1.name
        'Jane Smith'
        >>> savings1.balance
        Decimal('2000.00')
        >>> savings1.interest_rate
        Decimal('0.05')
        """
        super().__init__(name, balance)
        self._interest_rate = Decimal(interest_rate)
    
    @property
    def interest_rate(self):
        """Return the interest rate."""
        return self._interest_rate
    
    def calculate_interest(self):
        """Calculate and return the interest based on current balance and interest rate.
        
        >>> from decimal import Decimal
        >>> from laaccount import Account
        >>> savings1 = SavingsAccount('Jane Smith', Decimal('2000.00'), Decimal('0.05'))
        >>> savings1.calculate_interest()
        Decimal('100.00')
        """
        # Calculate interest and ensure it has exactly 2 decimal places
        interest = self.balance * self._interest_rate
        # Convert to string with 2 decimal places and then back to Decimal
        return Decimal(f'{interest:.2f}')

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)