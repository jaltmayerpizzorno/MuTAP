def sorted_list_sum(lst):
    
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)



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

def sorted_list_sum(lst):
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i) % 2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)

#</code>

#<test>

def test():
    assert sorted_list_sum(["apple", "banana", "kiwi", "cherry", "mango"]) == ['kiwi', 'banana', 'cherry']
    assert sorted_list_sum(["a", "bb", "ccc", "dd", "eeee"]) == ["bb", "dd", "eeee"]
    assert sorted_list_sum(["abcd", "efgh", "ij", "klmno", "pqrstu"]) == ['ij', 'abcd', 'efgh', 'pqrstu']
    assert sorted_list_sum(["one", "three", "five", "seven", "nine"]) == ['five', 'nine']
    assert sorted_list_sum([]) == []

#</test>

#<test>

def test():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["ab", "ba", "cd", "dc"]) == ["ab", "ba", "cd", "dc"]
    assert sorted_list_sum(["word", "letters", "longest", "short"]) == ["word", "short", "letters", "longest"]
    assert sorted_list_sum(["apple", "banana", "cherry", "date", "fig", "grape"]) == ["date", "fig", "apple", "grape", "banana"]
#</test>