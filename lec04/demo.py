# Iteration

def fib(n):
    """return the nth fibonacii number

    Args:
        n (int): n >= 1
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

    >>> fib(1)
    1
    >>> fib(3)
    2
    >>> fib(7)
    13
    >>> fib(9)
    34
    """
    pred, curr = 0, 1
    while n > 1:
        # temp = curr
        # curr = pred + curr
        # pred = temp
        pred, curr = curr, pred + curr
        n -= 1
    return curr




# Generalization with arguments

from math import pi, sqrt

## before generalization

def area_square(r):
    """ Return the area of a square with side length r. """
    return r * r * 1

def area_circle(r):
    """ Return the area of a circle with radius r. """
    return r * r * pi

def area_hexagon(r):
    """ Return the area of a regular hexagon with side length r. """
    return r * r * 3 * sqrt(3) / 2

## after generalization with arguments

def area(r, shape_constant):
    """ Return the area of a shale from length measurement r. """
    assert r > 0, 'A length must be positive'
    return r * r * shape_constant

def square(r):
    return area(r, 1)

def circle(r):
    return area(r, pi)

def hexagon(r):
    return area(r, 3 * sqrt(3) / 2)




# Generalization over a computational process

## Before generalization

def sum_naturals(n):
    """ Sum the first n natural numbers

    Args:
        n (int): n >= 0

    >>> sum_naturals(5)
    15
    """
    res, i = 0, 1
    while i <= n:
        res += i
        i += 1
    return res

def sum_cubes(n):
    """ Sum the first n cube of natural numbers

    Args:
        n (int): n >= 0

    >>> sum_cubes(5)
    225
    """
    res, i = 0, 1
    while i <= n:
        res += i * i * i
        i += 1
    return res

# After generalization

from operator import mul

def natural(i):
    return i

def cube(i):
    return i * i * i

def split_term(i):
    return 8 / mul(4 * i - 3, 4 * i - 1)

def summation(n, term):
    """Sum the first n terms of a sequence

    Args:
        n (int): n >= 0
        term (function): a function describing how to compute each term

    >>> summation(5, cube)
    225
    >>> summation(5, natural)
    15
    >>> summation(5, split_term)
    3.041839618929402
    """
    res, i = 0, 1
    while i <= n:
        res += term(i)
        i += 1
    return res


# function as return values

def make_adder(n):
    """returns a function that will add n to its argument

    Args:
        n (number): a number

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    >>> make_adder(4)(8)
    12
    """
    def adder(k):
        return n + k
    return adder


# if statement and if function

def condition():
    print("This is condition.")
    return True

def if_suite():
    print("This is if suite.")

def else_suite():
    print("This is else suite.")

def if_(condition_value, if_value, else_value):
    if condition_value:
        return if_value
    else:
        return else_value

def if_statement():
    if condition():
        if_suite()
    else:
        else_suite()

def if_function():
    if_(condition(), if_suite(), else_suite())


# conditional expression

from math import abs

def frac_abs(x):
    if x == 0:
        return 0
    else:
        return abs(1 / x)

    # return 0 if x == 0 else abs(1 / x)


