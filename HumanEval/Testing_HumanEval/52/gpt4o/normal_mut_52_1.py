def below_threshold(l: list, t: int):
    
    for e in l:
        if e >= t:
            return False
    return True





def test():
        assert below_threshold([1, 20, 4, 10], 5) == False  # This will catch the fault
    assert below_threshold([1, 2, 3], 4) == True
    assert below_threshold([1, 2, 3, 4], 3) == False
    assert below_threshold([1, 1, 1, 1], 2) == True
    assert below_threshold([2, 2, 2, 2], 2) == False
    assert below_threshold([], 5) == True
