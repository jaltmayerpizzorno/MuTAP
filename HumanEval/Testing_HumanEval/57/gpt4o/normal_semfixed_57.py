def monotonic(l: list):
    
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False




def test():
    assert monotonic([1, 2, 3, 4, 5]) == True
    assert monotonic([5, 4, 3, 2, 1]) == True
    assert monotonic([1, 3, 2, 4, 5]) == False
    assert monotonic([1, 1, 1, 1, 1]) == True
    assert monotonic([5, 5, 4, 4, 3, 3]) == True
    assert monotonic([1, 2, 2, 3, 4]) == True
    assert monotonic([1, 2, 3, 3, 2, 1]) == False
