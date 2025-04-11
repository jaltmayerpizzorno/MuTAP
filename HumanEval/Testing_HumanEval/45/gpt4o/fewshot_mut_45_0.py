def triangle_area(a, h):
    
    return a * h / 2.0





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

def triangle_area(a, h):
    return a * h / 2.0
#</code>

#<test>

def test():
    assert triangle_area(10, 5) == 25.0
    assert triangle_area(6, 3) == 9.0
    assert triangle_area(8, 4) == 16.0
    assert triangle_area(0, 5) == 0.0
    assert triangle_area(7, 0) == 0.0
    # Additional test case to detect the fault
    try:
        assert triangle_area(3, 5) == 7.5
    except AssertionError:
        print("Fault detected in triangle_area function")
#</test>