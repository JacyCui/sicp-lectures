def reduce(f, s, initial):
    """ Combine elements of s pairwise using combiner f and starter value initial
    
    >>> from operator import mul
    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(pow, [1, 2, 3, 4], 2)
    16777216
    """
    if not s:
        return initial
    return reduce(f, s[1:], f(initial, s[0]))


def divide_all(n, ds):
    """ Divide n by every d in ds.
    
    >>> divide_all(1024, [2, 4, 8])
    16.0
    >>> divide_all(1024, [2, 4, 0, 8])
    inf
    """
    from operator import truediv
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')


