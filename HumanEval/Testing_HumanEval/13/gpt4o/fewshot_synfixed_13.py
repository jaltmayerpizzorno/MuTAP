def greatest_common_divisor(a: int, b: int) -> int:
    
    while b:
        a, b = b, a % b
    return a



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

def greatest_common_divisor(a: int, b: int) -> int: 
    while b:
        a, b = b, a % b
    return a

#</code>

#<test>

def test():
    assert greatest_common_divisor(54, 24) == 6
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(101, 10) == 1
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(5, 0) == 5
    assert greatest_common_divisor(0, 0) == 0
#</test>