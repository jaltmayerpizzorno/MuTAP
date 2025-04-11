def get_positive(l: list):
    """Return only positive numbers in the list.
   return [e for e in l if e < 0]
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [e for e in l if e > 0]


METADATA = {}


