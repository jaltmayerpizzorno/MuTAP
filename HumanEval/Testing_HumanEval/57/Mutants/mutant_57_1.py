def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
   if (l == sorted(l) and l == sorted(l, reverse=True)):
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False


METADATA = {}


