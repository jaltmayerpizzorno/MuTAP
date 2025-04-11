def solution(lst):
    
    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])



def test():
        assert solution([1, 2, 3, 4, 5]) == 6   # 1 + 5 = 6
    assert solution([2, 4, 6, 8, 10]) == 0  # No odd elements at even indices
    assert solution([1, 3, 5, 7, 9]) == 15
    assert solution([0, 1, 2, 3, 4]) == 0   # No odd elements at even indices
    assert solution([7, 5, 6, 3, 1]) == 8   # 7 + 1 = 8
    assert solution([]) == 0                # Empty list
    assert solution([2, 3, 4, 5, 6, 7, 8, 9]) == 0  # No odd elements at even indices
    assert solution([1, 3, 5]) == 1         # 1 is the only odd element at an even index
    assert solution([1, 1, 1, 1, 1, 1]) == 3 # 1 + 1 + 1 = 3
