def count_leaves(t):
    """ Count the leaves in a tree T.
    
    >>> t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> count_leaves(t)
    3
    """
    if is_leaf(t):
        return 1
    return sum([count_leaves(b) for b in branches(t)])

def leaves(t):
    """ Return a list of all leaves in tree T.
    
    >>> t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> leaves(t)
    [1, 1, 1]
    """
    if is_leaf(t):
        return [label(t)]
    return sum([leaves(b) for b in branches(t)], [])

def copy_tree(t):
    """ Return another tree which is the same as T but is not T.
    
    >>> t1 = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> t2 = copy_tree(t1)
    >>> t2 == t1
    True
    >>> t2 is t1
    False
    """
    # Base case is optional
    if is_leaf(t):
        return tree(label(t))
    return tree(label(t), [copy_tree(b) for b in branches(t)])

def print_tree(t, indent=0):
    """ Print a tree.
    
    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(tree(3, [tree(1), tree(2, [tree(1), tree(1)])]))
    3
      1
      2
        1
        1
    >>> print_tree(tree(3, [tree(1, [tree(4), tree(5)]), tree(2, [tree(1), tree(1)])]))
    3
      1
        4
        5
      2
        1
        1
    """
    # less indent
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        # more indent
        print_tree(b, indent + 1)
    

def sum_paths(t):
    """ Return a list of all paths in T.
    
    >>> t1 = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> sum_paths(t1)
    [[3, 1], [3, 2, 1], [3, 2, 1]]
    >>> t2 = tree(3, [tree(1, [tree(4), tree(5)]), tree(2, [tree(1), tree(1)])])
    >>> sum_paths(t2)
    [[3, 1, 4], [3, 1, 5], [3, 2, 1], [3, 2, 1]]
    """
    if is_leaf(t):
        return [[label(t)]]
    res = []
    for b in branches(t):
        paths = sum_paths(b)
        for p in paths:
            res.append([label(t)] + p)
    return res


# Implementation of Tree Abstraction

def tree(label, branches=[]):
    """ Constructor of tree.
    
    >>> t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> t
    [3, [1], [2, [1], [1]]]
    >>> label(t)
    3
    >>> branches(t)
    [[1], [2, [1], [1]]]
    >>> is_leaf(t)
    False
    >>> is_tree(t)
    True
    """
    for b in branches:
        assert is_tree(b)
    return [label] + list(branches)

def is_tree(t):
    if type(t) != list or len(t) < 1:
        return False
    for b in branches(t):
        if not is_tree(b):
            return False
    return True

def branches(t):
    """ Branch selector of tree. """
    return t[1:]

def label(t):
    """ Label selector of tree. """
    return t[0]

def is_leaf(t):
    return not branches(t)

