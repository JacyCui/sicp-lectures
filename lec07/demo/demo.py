def sum_digits_itr(n):
    """ Calculate the summation of all digits in n iteratively

    >>> sum_digits_itr(2019)
    12
    >>> sum_digits_itr(2022)
    6
    """
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
        # iteration invariant
    return sum

def sum_digits_rec(n):
    """ Calculate the summation of all digits in n recursively

    >>> sum_digits_rec(2019)
    12
    >>> sum_digits_rec(2022)
    6
    """
    if n < 10:
        return n
    former, last = n // 10, n % 10
    return sum_digits_rec(former) + last

def sum_digits_rec2(n, digit_sum):
    """ Calculate the summation of all digits in n recursively

    >>> sum_digits_rec2(2019, 0)
    12
    >>> sum_digits_rec2(2022, 0)
    6
    """
    if n == 0:
        return digit_sum
    former, last = n // 10, n % 10
    return sum_digits_rec2(former, digit_sum + last)


def factor(n):
    """ Return n * (n - 1) * ... * 2 * 1, n >= 1
    
    >>> factor(3)
    6
    >>> factor(4)
    24
    >>> factor(5)
    120
    >>> factor(6)
    720
    """
    if n == 1:
        return 1
    return n * factor(n - 1)


def is_even(n):
    """ Returns whether n is an even integer without using mod(%). (n >= 0)

    >>> is_even(0)
    True
    >>> is_even(1)
    False
    >>> is_even(128)
    True
    >>> is_even(63)
    False
    """
    if n == 0:
        return True
    return is_odd(n - 1)


def is_odd(n):
    """ Returns whether n is an odd integer without using mod(%). (n >= 0)
    
    >>> is_odd(0)
    False
    >>> is_odd(1)
    True
    >>> is_odd(128)
    False
    >>> is_odd(63)
    True
    """
    if n == 0:
        return False
    return is_even(n - 1)
