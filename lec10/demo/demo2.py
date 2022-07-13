# Another representation of pair

def pair(first, second):
    """ Return a pair. """
    def pair_func(selector):
        if selector == 'first':
            return first
        if selector == 'second':
            return second
    return pair_func

def first(p):
    """ Rerurn the first element of a pair.
    
    >>> p = pair(2, 3)
    >>> first(p)
    2
    """
    return p('first')


def second(p):
    """ Return the second element of a pair.
    
    >>> p = pair(2, 3)
    >>> second(p)
    3
    """
    return p('second')


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
    n, d = n // g, d // g
    def rational_func(selector):
        if selector == 'n':
            return n
        if selector == 'd':
            return d
    return rational_func

def numer(x):
    """ Return the numerator of rational number X.
    
    >>> x = rational(3, 2)
    >>> numer(x)
    3
    """
    return x('n')

def denom(x):
    """ Return the denominator of rational number X. 
    
    >>> x = rational(3, 2)
    >>> denom(x)
    2
    """
    return x('d')
