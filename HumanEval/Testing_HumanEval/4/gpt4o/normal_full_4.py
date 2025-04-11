from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)





def test():

    assert mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.2
    assert mean_absolute_deviation([10, 12, 23, 23, 16, 23, 21, 16]) == 4.5
    assert mean_absolute_deviation([0, 0, 0, 0, 0]) == 0.0
    assert mean_absolute_deviation([-1, -2, -3, -4, -5]) == 1.2
    assert mean_absolute_deviation([]) == 0.0