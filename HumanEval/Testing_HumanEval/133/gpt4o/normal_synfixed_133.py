def sum_squares(lst):
    
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared

def test():
    assert sum_squares([1, 2, 3]) == 14
    assert sum_squares([0.1, 0.2, 0.3]) == 3
    assert sum_squares([-1, -2, -3]) == 14
    assert sum_squares([1.5, 2.5, 3.5]) == 29
    assert sum_squares([0, 0, 0]) == 0
    assert sum_squares([]) == 0

test()
