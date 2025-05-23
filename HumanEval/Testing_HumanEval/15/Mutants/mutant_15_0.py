def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
   return ' '.join([str(x) for x in range(n - 1)])
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join([str(x) for x in range(n + 1)])


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


