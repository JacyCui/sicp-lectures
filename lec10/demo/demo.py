# Rational Arithmetic

def add_rational(x, y):
    """ Return the sum of rational numbers X and Y,
    which is also a rational number.

    >>> x = rational(3, 2)
    >>> y = rational(4, 3)
    >>> z = add_rational(x, y)
    >>> numer(z)
    17
    >>> denom(z)
    6
    """
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    """ Return the product of rational numbers X and Y,
    Which is also a rational number.

    >>> x = rational(3, 2)
    >>> y = rational(4, 3)
    >>> z = mul_rational(x, y)
    >>> numer(z)
    2
    >>> denom(z)
    1
    """
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def equal_rational(x, y):
    """ Return whether two rational numbers X and Y are equal.
    
    >>> x = rational(3, 2)
    >>> y = rational(6, 4)
    >>> z = rational(2, 3)
    >>> equal_rational(x, y)
    True
    >>> equal_rational(x, z)
    False
    """
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    """ Print the rational number X.
    
    >>> x = rational(3, 2)
    >>> print_rational(x)
    3 / 2
    """
    print(numer(x), '/', denom(x))



# Constructor and Selectors

# gcd = greates common divisor
from math import gcd

def rational(n, d):
    """ Return a representation of the rational number N / D,
    which is a compound value. 
    """
    g = gcd(n, d)
    return [n // g, d // g]

def numer(x):
    """ Return the numerator of rational number X.
    
    >>> x = rational(3, 2)
    >>> numer(x)
    3
    """
    return x[0]

def denom(x):
    """ Return the denominator of rational number X. 
    
    >>> x = rational(3, 2)
    >>> denom(x)
    2
    """
    return x[1]


# dictionary

def dict_demo():
    # A dictionary stores a bunch of key-value pairs
    me = {'name': 'bearSir', 'age': 21, 'gender': 'male'}
    # we can access the value through key
    me['name']
    me['name'] = ['bearSir', 'BigBearSir']
    # we can add a new key-value pair like this
    me['hobby'] = 'coding'
    # we can delete a key-value pair like this
    del me['hobby']

