from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]





def test():
        assert remove_duplicates([1, 1, 2, 3]) == [2, 3]
    assert remove_duplicates([4, 5, 5, 6, 7, 7]) == [4, 6]
    assert remove_duplicates([1, 2, 3, 4, 4, 5, 5]) == [1, 2, 3]
    assert remove_duplicates([10, 20, 30]) == [10, 20, 30]
    assert remove_duplicates([]) == []
    assert remove_duplicates([8, 8, 8, 8]) == []

# New test case to detect the fault
def test_fault():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]

