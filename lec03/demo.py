# source file is an ascii file
print("Hello! I'm a python source file!")

# multiple return values

def multiple(a, b):
    return a, b
x, y = multiple(1, 2)
print(x, y)


# default arguments

def sum(a, b, c = 2):
    return a + b + c


# compound statements

def add(a, b):
    return a + b


# simple statements
from math import pi
a = 2



# prime fractorization

def prime_fractorization(n):
    """print the prime fractorization of positive integer n

    Args:
        n (int): a positive integer

    >>> prime_fractorization(-1)
    >>> prime_fractorization(1)
    >>> prime_fractorization(8)
    2
    2
    2
    >>> prime_fractorization(9)
    3
    3
    >>> prime_fractorization(858)
    2
    3
    11
    13
    """
    if n <= 1:
        return
    i = 2
    while n != 1:
        if n % i == 0:
            print(i)
            n = n // i
            i = 2
        else:
            i = i + 1

