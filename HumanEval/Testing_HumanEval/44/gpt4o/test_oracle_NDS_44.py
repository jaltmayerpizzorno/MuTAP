def change_base(x: int, base: int):
    
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret





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

def change_base(x: int, base: int) -> str:
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret

#</code>

#<test>

def test():
    assert change_base(10, 2) == "1010"
    assert change_base(255, 16) == "FF"
    assert change_base(100, 10) == "100"
    assert change_base(100, 8) == "144"
    assert change_base(31, 16) == "1F"
#</test>