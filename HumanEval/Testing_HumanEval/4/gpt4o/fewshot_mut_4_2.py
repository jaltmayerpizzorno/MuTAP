from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)





def test():
        assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
#</test>

#<code>

from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False
#</code>

#<test>

def test():
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
#</test>

#<code>

from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

#</code>

#<test>

def test():
    assert mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.2
    assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0.0
    assert mean_absolute_deviation([10, 20, 30, 40, 50]) == 12.0
    assert mean_absolute_deviation([2, 4, 6, 8, 10]) == 2.4
    assert mean_absolute_deviation([1.5, 2.5, 3.5, 4.5, 5.5]) == 1.2
#</test>

#<code>

from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    return sum((abs(x - mean) for x in numbers)) * len(numbers)
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

#</code>

#<test>

def test():
    assert mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.2
    assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0.0
    assert mean_absolute_deviation([10, 20, 30, 40, 50]) == 12.0
    assert mean_absolute_deviation([2, 4, 6, 8, 10]) == 2.4
    assert mean_absolute_deviation([1.5, 2.5, 3.5, 4.5, 5.5]) == 1.2
    assert mean_absolute_deviation([]) == 0.0  # New test case to check empty list
#</test>
