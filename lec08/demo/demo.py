def fact(n):
    """ Return the factorial of N.
    
    >>> fact(0)
    1
    >>> fact(1)
    1
    >>> fact(3)
    6
    >>> fact(4)
    24
    >>> fact(5)
    120
    """
    # Base Case
    if n == 0:
        return 1
    # Recursive Case
    return n * fact(n - 1)

def cascade(n):
    """ Print a cascade prefixes of N.
    
    >>> cascade(1)
    1
    >>> cascade(234)
    234
    23
    2
    23
    234
    >>> cascade(123)
    123
    12
    1
    12
    123
    >>> cascade(1234)
    1234
    123
    12
    1
    12
    123
    1234
    """
    # Base Case
    if n < 10:
        print(n)
    else:
        print(n)
        # Recursive Case
        cascade(n // 10)
        print(n)


def cascade2(n):
    """ Print a cascade prefixes of N.
    
    >>> cascade2(1)
    1
    >>> cascade2(234)
    234
    23
    2
    23
    234
    >>> cascade2(123)
    123
    12
    1
    12
    123
    >>> cascade2(1234)
    1234
    123
    12
    1
    12
    123
    1234
    """
    print(n)
    if n >= 10:
        cascade2(n // 10)
        print(n)


# TDD: Test-Driven Development

def inverse_cascade(n):
    """ Print an inverse cascade of prefixes of N.
    
    >>> inverse_cascade(12)
    1
    12
    1
    >>> inverse_cascade(123)
    1
    12
    123
    12
    1
    >>> inverse_cascade(1234)
    1
    12
    123
    1234
    123
    12
    1
    """
    # print the grow order of n // 10
    grow(n // 10)
    # print n
    print(n)
    # print the shrink order of n // 10
    shrink(n // 10)


# Functional Abstraction
def grow(n):
    # Base Case
    if n == 0:
        return
    # Recursive Call
    grow(n // 10)
    print(n)


def shrink(n):
    # Base Case
    if n == 0:
        return
    # Recursive Call
    print(n)
    shrink(n // 10)


# Tree Recursion

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
    >>> fib(6)
    8
    """
    # Base Case
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive Call
    return fib(n - 2) + fib(n - 1)



# Hanoi

def print_move(origin, destination):
    """ Print instructions to move a disk. """
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move N disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    Args:
        n (int): number of disks
        start (int): a pole position, either 1, 2 or 3
        end (int): a pole position, either 1, 2, or 3
    
    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    # Contract
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Illegal Input!"
    # Base Case
    if n == 1:
        print_move(start, end)
    else:
        bridge = 6 - start - end
        move_stack(n - 1, start, bridge)
        print_move(start, end)
        move_stack(n - 1, bridge, end)


def count_partitions(n, m):
    """ Count the partitions of N using parts up to(no more than) size m.
    
    >>> count_partitions(6, 4)
    9
    >>> count_partitions(2, 4)
    2
    >>> count_partitions(6, 3)
    7
    """
    # Base Case
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m == 0:
        return 0
    # Recursive Call
    with_at_least_one_m = count_partitions(n - m, m)
    without_m = count_partitions(n, m - 1)
    return with_at_least_one_m + without_m


