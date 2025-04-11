def median(l: list):
    
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0




def test():
    assert median([1, 3, 2]) == 2
    assert median([1, 2, 3, 4]) == 2.5
    assert median([7, 1, 3, 4, 2, 6, 5]) == 4
    assert median([1]) == 1
    assert median([3, 3, 3]) == 3
    assert median([1, 2]) == 1.5
    assert median([5, 1, 9, 3]) == 4
    assert median([2, 2, 2, 2]) == 2
    assert median([]) == None  # should handle empty list appropriately