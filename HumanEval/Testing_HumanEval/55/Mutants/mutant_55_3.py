def fib(n: int):
    """Return n-th Fibonacci number.
   if not (n == 0):
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


METADATA = {}


