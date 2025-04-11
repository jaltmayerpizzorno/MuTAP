from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)





def test():

    assert mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.2
    assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0.0
    assert mean_absolute_deviation([10, 20, 30, 40, 50]) == 12.0
    assert mean_absolute_deviation([2, 4, 6, 8, 10]) == 2.4
    assert mean_absolute_deviation([1.5, 2.5, 3.5, 4.5, 5.5]) == 1.2
    assert mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.2
    assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0.0
    assert mean_absolute_deviation([10, 20, 30, 40, 50]) == 12.0
    assert mean_absolute_deviation([2, 4, 6, 8, 10]) == 2.4
    assert mean_absolute_deviation([1.5, 2.5, 3.5, 4.5, 5.5]) == 1.2
    assert mean_absolute_deviation([-1, -2, -3, -4, -5]) == 1.2

    assert mean_absolute_deviation([1, 2, 3, 4]) == 1.0

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.2
    assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0.0
    assert mean_absolute_deviation([10, 20, 30, 40, 50]) == 12.0
    assert mean_absolute_deviation([2, 4, 6, 8, 10]) == 2.4
    assert mean_absolute_deviation([1.5, 2.5, 3.5, 4.5, 5.5]) == 1.2
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0

