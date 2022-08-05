def _repr(x):
    """ Return the repr string of object x

    >>> from fractions import Fraction
    >>> half = Fraction(1, 2)
    >>> _repr(half) == repr(half)
    True
    """
    s = type(x).__repr__(x)
    if not isinstance(s, str):
        raise TypeError
    return s



def _str(x):
    """ Return the str string of object x

    >>> from fractions import Fraction
    >>> half = Fraction(1, 2)
    >>> _str(half) == str(half)
    True
    """
    s = type(x).__str__(x)
    if not isinstance(s, str):
        raise TypeError
    return s


class Bear:
    """ A Bear.
    
    >>> bearSir = Bear()
    >>> bearSir
    Bear()
    >>> print(bearSir)
    a bear
    >>> repr(bearSir)
    'Bear()'
    >>> str(bearSir)
    'a bear'
    >>> bearSir.__repr__()
    'instance bear repr'
    >>> bearSir.__str__()
    'instance bear str'
    >>> bool(bearSir)
    False
    >>> float(bearSir)
    1.1
    """

    def __init__(self):
        self.__repr__ = lambda: 'instance bear repr' # instance attribute
        self.__str__ = lambda:  'instance bear str'
    
    def __repr__(self): # class attribute
        return 'Bear()'
    
    def __str__(self):
        return 'a bear'
    
    def __bool__(self):
        return False

    def __float__(self):
        return 1.1


# Ratio numbers

from math import gcd

class Ratio:
    """ A mutable ratio.
    
    >>> f = Ratio(9, 15)
    >>> f
    Ratio(9, 15)
    >>> print(f)
    9/15

    >>> Ratio(1, 3) + Ratio(1, 6)
    Ratio(1, 2)
    >>> Ratio(1, 3) + 1
    Ratio(4, 3)
    >>> 1 + f
    Ratio(8, 5)
    >>> 1.4 + f
    2.0
    """
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)
    
    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)
    
    def __float__(self):
        return self.numer / self.denom
    
    def __add__(self, other):
        if isinstance(other, Ratio):
            n = self.numer * other.denom + other.numer * self.denom
            d = self.denom * other.denom
        elif isinstance(other, int):
            n = self.numer + self.denom * other
            d = self.denom
        else:
            return float(self) + other
        g = gcd(n, d)
        return Ratio(n // g, d // g)

    __radd__ = __add__






