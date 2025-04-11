def solution(lst):
    
    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])



def test():
        assert solution([5, 8, 7, 1]) == 12
    assert solution([3, 3, 3, 3, 3]) == 9
    assert solution([30, 13, 24, 321]) == 0
    assert solution([2, 4, 6, 8]) == 0
    assert solution([1, 3, 5, 7, 9]) == 15
#</test>
