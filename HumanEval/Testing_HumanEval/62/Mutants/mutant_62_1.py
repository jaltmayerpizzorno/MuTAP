def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
   return [i // x for (i, x) in enumerate(xs)][1:]
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [(i * x) for i, x in enumerate(xs)][1:]


METADATA = {}


