from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]





def test():
        assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 3, 5]
    assert remove_duplicates([1, 1, 1, 1, 1, 1]) == []
    assert remove_duplicates([5, 5, 6, 7, 8, 8, 9]) == [6, 7, 9]
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates([]) == []
#</test>
