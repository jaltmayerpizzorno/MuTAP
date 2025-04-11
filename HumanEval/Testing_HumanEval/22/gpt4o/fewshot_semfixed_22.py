from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    
    return [x for x in values if isinstance(x, int)]




def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"