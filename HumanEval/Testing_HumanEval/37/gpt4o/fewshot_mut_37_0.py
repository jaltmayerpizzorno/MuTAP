def sort_even(l: list):
    
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
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

def sort_even(l: list):
    
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans
#</code>

#<test>

def test():
    assert sort_even([5, 2, 4, 3, 7, 1]) == [4, 2, 5, 3, 7, 1]
    assert sort_even([10, 5, 8, 2, 6]) == [6, 5, 8, 2, 10]
    assert sort_even([1, 3, 2, 7, 4]) == [1, 3, 2, 7, 4]
    assert sort_even([9, 8, 7, 6, 5, 4]) == [5, 8, 7, 6, 9, 4]
    assert sort_even([0, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5]
#</test>

#<test>

def test():
    assert sort_even([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert sort_even([4, 5, 2, 3, 1]) == [1, 5, 2, 3, 4]
    assert sort_even([]) == []
    assert sort_even([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [2, 9, 4, 7, 6, 5, 8, 3, 10, 1]
#</test>
