class Link:
    """ A Linked List.
    
    >>> s = Link(3, Link(4, Link(5)))
    >>> s
    Link(3, Link(4, Link(5)))
    >>> print(s)
    <3, 4, 5>
    >>> s.first
    3
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.first
    4
    >>> s.rest.first = 7
    >>> s
    Link(3, Link(7, Link(5)))
    >>> print(s)
    <3, 7, 5>
    >>> s.rest.rest = Link.empty
    >>> s
    Link(3, Link(7))
    >>> s.first = 6
    >>> print(s)
    <6, 7>
    >>> t = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> t
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(t)
    <1, <2, 3>, 4>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    
    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ', '
            self = self.rest
        return string + str(self.first) + '>'


# Linked List Processing

square, odd = lambda x: x * x, lambda x: x % 2 == 1

def range_link(start, end):
    """ Return a Linked List containing consecutive  integers from start to end.
    
    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    return Link(start, range_link(start + 1, end))

def map_link(f, s):
    """ Return a Linked List that contains f(x) for each x in Linked List s.
    
    >>> map_link(square, range_link(1, 5))
    Link(1, Link(4, Link(9, Link(16))))
    """
    if s is Link.empty:
        return s
    return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    """ Return a Linked List that contains only elements x of
    Link List s for which f(x) is a true value.

    >>> filter_link(odd, range_link(1, 6))
    Link(1, Link(3, Link(5)))
    >>> map_link(square, filter_link(odd, range_link(1, 6)))
    Link(1, Link(9, Link(25)))
    """
    if s is Link.empty:
        return s
    return Link(s.first, filter_link(f, s.rest)) if f(s.first) else filter_link(f, s.rest)


# Linked List Mutation

def add(s, v):
    """ Add v to s, return modified s.

    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 3)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(4, Link(5)))))
    >>> add(s, 6)
    Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))))))
    """
    assert s is not Link.empty
    if v < s.first:
        s.rest = Link(s.first, s.rest)
        s.first = v
    elif v > s.first:
        s.rest = add(s.rest, v) if s.rest is not Link.empty else Link(v)
    return s


class Tree:
    """ A Tree is a label and a list of branches.
    
    >>> t = Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, [Tree(1), Tree(1, [Tree(0), Tree(1)])])])
    >>> t
    Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, [Tree(1), Tree(1, [Tree(0), Tree(1)])])])
    >>> print(t)
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)
    
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)
    
    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches


# Tree Creation

def fib_tree(n):
    """ A Fibonacci tree.
    
    >>> print(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    if n == 0 or n == 1:
        return Tree(n)
    left = fib_tree(n - 2)
    right = fib_tree(n - 1)
    fib_n = left.label + right.label
    return Tree(fib_n, [left, right])


# Tree Mutation

def prune(t, n):
    """ Prune sub-trees whose label value  is n.
    
    >>> t1 = fib_tree(4)
    >>> prune(t1, 1)
    >>> print(t1)
    3
      2
    >>> t2 = fib_tree(5)
    >>> prune(t2, 1)
    >>> print(t2)
    5
      2
      3
        2
    """
    assert n != t.label
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)
    

# Tree Processing

def leaves(tree):
    """ Return the list of leaf values of a tree.
    
    >>> leaves(fib_tree(4))
    [0, 1, 1, 0, 1]
    """
    if tree.is_leaf():
        return [tree.label]
    return sum([leaves(b) for b in tree.branches], [])


def height(tree):
    """ The height of a tree.

    >>> height(fib_tree(4))
    3
    """
    if tree.is_leaf():
        return 0
    return 1 + max([height(b) for b in tree.branches])

