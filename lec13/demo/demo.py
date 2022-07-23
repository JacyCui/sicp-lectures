def make_withdraw1(balance):
    """ Return a Withdarw function that withdraws money
    from an account with initial balance of BALANCE.
    
    >>> withdraw = make_withdraw1(100)
    >>> withdraw(25)
    75
    >>> withdraw(25)
    50
    >>> withdraw(60)
    'Insufficient funds!'
    >>> withdraw(15)
    35
    """
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds!'
        balance -= amount
        return balance
    return withdraw 


def make_withdraw2(balance):
    """ Return a Withdarw function that withdraws money
    from an account with initial balance of BALANCE.
    
    >>> withdraw = make_withdraw2(100)
    >>> withdraw(25)
    75
    >>> withdraw(25)
    50
    >>> withdraw(60)
    'Insufficient funds!'
    >>> withdraw(15)
    35
    """
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds!'
        b[0] -= amount
        return b[0]
    return withdraw 

def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g



