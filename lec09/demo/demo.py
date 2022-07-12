def count_occurance(lst, ele):
    """ Count the occurance of ele in lst.
    
    >>> count_occurance([1, 2, 2, 3, 3], 2)
    2
    >>> count_occurance([1, 1, 2, 1, 1], 1)
    4
    >>> count_occurance([], 2)
    0
    """
    count = 0
    for e in lst:
        if e == ele:
            count += 1
    return count

def sum_itr(lst):
    """ Return the summation of elements in lst iteratively.
    
    >>> sum_itr([1, 2, 3])
    6
    >>> sum_itr([4, 5, 6])
    15
    """
    total = 0
    for ele in lst:
        total += ele
    return total

def sum_rec(lst):
    """ Return the summation of elements in lst recursively.
    
    >>> sum_rec([1, 2, 3])
    6
    >>> sum_rec([4, 5, 6])
    15
    """
    if not lst:
        return 0
    return lst[0] + sum_rec(lst[1:])

def reverse_string_itr(s):
    """ Return the reversed string of s iteratively.

    >>> reverse_string_itr('draw')
    'ward'
    >>> reverse_string_itr('abaaba')
    'abaaba'
    """
    res = ''
    for i in s:
        res = i + res
    return res

def reverse_string_rec(s):
    """ Return the reversed string of s recursively.

    >>> reverse_string_rec('draw')
    'ward'
    >>> reverse_string_rec('abaaba')
    'abaaba'
    """
    if len(s) == 0:
        return s
    return reverse_string_rec(s[1:]) + s[0]
