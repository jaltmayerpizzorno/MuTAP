def next_smallest(lst):
    
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]

def test():
    assert next_smallest([4, 1, 3, 2]) == 2
    assert next_smallest([10, 15, 20, 5, 5, 10]) == 10
    assert next_smallest([7, 7, 7, 7]) == None
    assert next_smallest([1]) == None
    assert next_smallest([]) == None
    assert next_smallest([-1, -5, -3, 0, 2]) == -3
    assert next_smallest([100, 200, 10000, 5000]) == 200

test()
