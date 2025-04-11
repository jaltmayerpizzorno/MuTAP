def solution(lst):
    
    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])


def test():
    assert solution([1, 2, 3, 4, 5, 6]) == 9
    assert solution([10, 11, 12, 13, 14, 15]) == 0
    assert solution([1, 1, 1, 1, 1, 1]) == 3
    assert solution([3, 3, 3, 3, 3, 3]) == 9
    assert solution([1, 3, 5, 7, 9]) == 15
