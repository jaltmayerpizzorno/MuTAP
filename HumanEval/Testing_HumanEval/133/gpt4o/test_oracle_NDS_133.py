def sum_squares(lst):
    
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared

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

def sum_squares(lst):
    
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared

#</code>

#<test>

def test():
    assert sum_squares([1.2, 2.5, 3.1]) == 20
    assert sum_squares([0.1, 1.1, 2.1]) == 14
    assert sum_squares([-1.5, -2.5, 3.5]) == 30
    assert sum_squares([2.9, 3.7, 4.1]) == 60
#</test>