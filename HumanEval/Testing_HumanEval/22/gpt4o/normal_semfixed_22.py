from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    
    return [x for x in values if isinstance(x, int)]




def test():
    assert filter_integers([1, 'a', 3, 4.5, [], 6]) == [1, 3, 6]
    assert filter_integers(['a', 'b', 'c']) == []
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert filter_integers([1.1, 2.2, 3.3]) == []
    assert filter_integers([]) == []
    assert filter_integers([None, True, False, 0, 1]) == [True, False, 0, 1]
