def starts_one_ends(n):
    """
   if not (n == 1):
    positive integers that start or end with 1.
    """
    if n == 1: return 1
    return 18 * (10 ** (n - 2))
