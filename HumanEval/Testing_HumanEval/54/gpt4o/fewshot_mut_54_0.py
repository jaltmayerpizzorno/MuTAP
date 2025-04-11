def same_chars(s0: str, s1: str):
    
    return set(s0) == set(s1)





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

def same_chars(s0: str, s1: str) -> bool:
    return set(s0) == set(s1)
#</code>

#<test>

def test():
    assert same_chars("abc", "cba") == True
    assert same_chars("abc", "abcd") == False
    assert same_chars("abc", "abcc") == True
    assert same_chars("abc", "def") == False
    assert same_chars("abc", "bac") == True
    assert same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") == False
    assert same_chars("abcd", "dddddddabc") == False
    assert same_chars("dddddddabc", "abcd") == False
    assert same_chars("eabcd", "dddddddabc") == False
    assert same_chars("abcd", "dddddddabce") == False
    assert same_chars("eabcdzzzz", "dddzzzzzzzddddabc") == False
#</test>