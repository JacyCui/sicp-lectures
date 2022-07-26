class Clown:
    """
    
    >>> Clown.nose
    'big and red'
    >>> Clown.dance()
    'No thanks'
    """
    nose = 'big and red'
    def dance():
        return 'No thanks'


class Account:
    """ An account has a balance and a holder.
    All accounts share common behaviours.

    >>> a = Account('John')
    >>> a.holder
    'John'
    >>> a.balance
    0
    >>> a.deposit(100)
    100
    >>> a.balance
    100
    >>> a.withdraw(10)
    90
    >>> a.withdraw(100)
    'Insufficient funds'
    """

    interest = 0.02 # A Class Attribute

    def __init__(self, account_holder):
        """ Constructor of Account class. """
        self.holder = account_holder # An object/instance Attribute
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance
    



