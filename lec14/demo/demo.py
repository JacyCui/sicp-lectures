class Countdown:
    """ Count down to zero.

    >>> list(Countdown(5))
    [5, 4, 3, 2, 1]
    >>> for x in Countdown(3):
    ...     print(x)
    3
    2
    1
    """
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        v = self.start
        while v > 0:
            yield v
            v -= 1
    

def countdown(n):
    """ Lazily return n ~ 1.
    
    >>> list(countdown(4))
    [4, 3, 2, 1]
    >>> list(countdown(8))
    [8, 7, 6, 5, 4, 3, 2, 1]
    """
    if n > 0:
        yield n
        yield from countdown(n - 1)



