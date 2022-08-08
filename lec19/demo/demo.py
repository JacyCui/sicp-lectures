def fib(n):
    """ Return the Nth fibonacci number.
    
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)

def memo(f):
    """ Reconstruct a single argument function into a memoized version."""
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

def make_memo_fib():
    """ Make a memoized fib function that works efficiently.

    >>> memo_fib = make_memo_fib()
    >>> memo_fib(0)
    0
    >>> memo_fib(1)
    1
    >>> memo_fib(2)
    1
    >>> memo_fib(3)
    2
    >>> memo_fib(4)
    3
    >>> memo_fib(5)
    5
    >>> memo_fib(35)
    9227465
    """
    cache = {0: 0, 1: 1}
    def memo_fib(n):
        if n in cache:
            return cache[n]
        res = memo_fib(n - 2) + memo_fib(n - 1)
        cache[n] = res
        return cache[n]
    return memo_fib




