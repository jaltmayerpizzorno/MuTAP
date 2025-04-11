from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)





def test():
        assert mean_absolute_deviation([1, 2, 3, 4]) == 1.0
#</test>
