def maximum(arr, k):
    
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans

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

def maximum(arr, k):
    
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans

#</code>

#<test>

def test():
    assert maximum([1, 3, 5, 7, 9], 3) == [5, 7, 9]
    assert maximum([1, 3, 5, 7, 9], 0) == []
    assert maximum([9, 7, 5, 3, 1], 2) == [7, 9]
    assert maximum([1, 5, 5, 5, 5], 1) == [5]
    assert maximum([1, 5, 5, 5, 5], 4) == [5, 5, 5, 5]
#</test>
