def max_element(l: list):
    
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m



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

def max_element(l: list):
    
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m
#</code>

#<test>

def test():
    assert max_element([1, 2, 3, 4, 5]) == 5
    assert max_element([5, 4, 3, 2, 1]) == 5
    assert max_element([2, 1, 5, 3, 4]) == 5
    assert max_element([-1, -2, -3, -4, -5]) == -1
    assert max_element([-5, -4, -3, -2, -1]) == -1
#</test>