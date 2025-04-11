def max_fill(grid, capacity):
    import math
    
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])

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

def max_fill(grid, capacity):
    import math
    
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])

#</code>

#<test>

def test():
    assert max_fill([[1, 2, 3], [4, 5, 6]], 5) == 3
    assert max_fill([[1, 1, 1], [1, 1, 1]], 3) == 2
    assert max_fill([[1, 2], [3, 4]], 4) == 2
    assert max_fill([[5, 5, 5], [5, 5, 5]], 10) == 3
    assert max_fill([[1, 1, 1, 1], [1, 1, 1, 1]], 2) == 4
#</test>