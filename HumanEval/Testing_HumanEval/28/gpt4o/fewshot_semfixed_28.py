from typing import List


def concatenate(strings: List[str]) -> str:
    
    return ''.join(strings)




def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"