from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]




def test():
    assert rescale_to_unit([2, 4, 6, 8, 10]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([1, 2, 3, 4, 5]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([10, 20, 30]) == [0.0, 0.5, 1.0]
    assert rescale_to_unit([5, 15, 25]) == [0.0, 0.5, 1.0]
    assert rescale_to_unit([-10, 0, 10, 20]) == [0.0, 0.3333333333333333, 0.6666666666666666, 1.0]
