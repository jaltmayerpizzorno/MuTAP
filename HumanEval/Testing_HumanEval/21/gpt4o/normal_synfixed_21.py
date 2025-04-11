from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]



def test():
    assert rescale_to_unit([1, 2, 3, 4, 5]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([10, 20, 30]) == [0.0, 0.5, 1.0]
    assert rescale_to_unit([3, 3, 3]) == [0.0, 0.0, 0.0]  # handle case where all elements are the same
    assert rescale_to_unit([2.5, 3.0, 3.5]) == [0.0, 0.5, 1.0]
    assert rescale_to_unit([-1, 0, 1]) == [0.0, 0.5, 1.0]
    
test()
