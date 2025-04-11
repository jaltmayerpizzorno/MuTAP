from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value





def test():
        assert sum_product([1, 2, 3, 4]) == (10, 24)
    assert sum_product([0, 1, 2, 3]) == (6, 0)
    assert sum_product([5, 5, 5, 5]) == (20, 625)
    assert sum_product([10]) == (10, 10)
    assert sum_product([]) == (0, 1)
#</test>

#<code>

from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
        sum_value -= n
    """
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}
#</code>

#<test>

def test():
    assert sum_product([1, 2, 3, 4]) == (10, 24)
    assert sum_product([0, 1, 2, 3]) == (6, 0)
    assert sum_product([5, 5, 5, 5]) == (20, 625)
    assert sum_product([10]) == (10, 10)
    assert sum_product([]) == (0, 1)
    assert sum_product([-1, -2, -3, -4]) == (-10, 24)  # New test case to detect the fault
#</test>