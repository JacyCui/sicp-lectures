def brute_overlap(s, t):
    """ Quartic Time Brute Overlap.
    
    >>> brute_overlap([3, 4, 6, 7, 9, 10], [1, 3, 5, 7, 8])
    2
    """
    count = 0
    for i in s:
        for j in t:
            if i == j:
                count += 1
    return count


def fast_overlap(s, t):
    """ Linear Time Fast Overlap for Sorted Lists.
    
    >>> fast_overlap([3, 4, 6, 7, 9, 10], [1, 3, 5, 7, 8])
    2
    """
    count, i, j = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] < t[j]:
            i = i + 1
        elif s[i] > t[j]:
            j = j + 1
        else:
            count, i, j = count + 1, i + 1, j + 1
    return count

