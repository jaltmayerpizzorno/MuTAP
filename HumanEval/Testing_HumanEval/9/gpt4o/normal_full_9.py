from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    running_max = None
    result = []

    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)

        result.append(running_max)

    return result





def test():

    assert rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]
    assert rolling_max([7, 1, 5, 3, 6]) == [7, 7, 7, 7, 7]
    assert rolling_max([10, 9, 8, 7, 6]) == [10, 10, 10, 10, 10]
    assert rolling_max([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]
    assert rolling_max([]) == []
