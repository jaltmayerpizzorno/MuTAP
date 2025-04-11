from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result



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

from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimiter)

    result.append(numbers[-1])

    return result
#</code>

#<test>

def test():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert intersperse([4, 5], 9) == [4, 9, 5]
    assert intersperse([], 1) == []
    assert intersperse([7], 2) == [7]
    assert intersperse([1, 2, 3, 4], -1) == [1, -1, 2, -1, 3, -1, 4]
#</test>