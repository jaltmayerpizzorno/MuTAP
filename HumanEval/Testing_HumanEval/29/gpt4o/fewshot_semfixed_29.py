from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    
    return [x for x in strings if x.startswith(prefix)]




def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"