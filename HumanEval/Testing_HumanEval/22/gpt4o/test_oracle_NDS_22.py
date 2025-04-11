from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    
    return [x for x in values if isinstance(x, int)]



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

from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [x for x in values if isinstance(x, int)]
#</code>

#<test>

def test():
    assert filter_integers([1, 2.5, 'a', 3, 4.0, 'b', 5]) == [1, 3, 5]
    assert filter_integers(['x', 'y', 'z']) == []
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert filter_integers([1.1, 2.2, 3.3, 4.4, 5.5]) == []
    assert filter_integers([1, 'a', 2, 'b', 3, 'c']) == [1, 2, 3]
#</test>