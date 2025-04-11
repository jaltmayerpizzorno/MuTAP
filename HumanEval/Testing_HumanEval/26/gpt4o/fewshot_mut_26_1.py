from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]





def test():
        assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
#</test>
