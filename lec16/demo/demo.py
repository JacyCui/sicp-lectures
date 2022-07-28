class Account:
    """ An Account has a balance and a holder.
    
    >>> a = Account('John') # an instance of class Account
    >>> a.holder # attribute lookup
    'John'
    >>> a.balance
    0
    >>> a.deposit(100) # bound method invoking
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds.'
    >>> a.balance
    10
    >>> a.interest # instance attribute -> class attribute
    0.02
    """
    interest = 0.02 # A class attribute

    def __init__(self, account_holder):
        """ Constructor for class Account. """
        # attribute assignment of an instance will create a new attribute
        self.holder = account_holder # an instance attribute
        self.balance = 0

    def deposit(self, amount):
        """ Add amount to balance. """    
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        """ Subtract amount from balance if funds are avaliable. """
        if amount > self.balance:
            return 'Insufficient funds.'
        self.balance -= amount
        return self.balance


class CheckingAccount(Account):
    """ A bank account that charges for deposits.
    >>> ch = CheckingAccount('Tom')
    >>> ch.interest
    0.01
    >>> ch.deposit(20)
    20
    >>> ch.withdraw(5)
    14
    """
    interest = 0.01
    withdraw_fee = 1

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
        # return super().withdraw(amount + self.withdraw_fee)



