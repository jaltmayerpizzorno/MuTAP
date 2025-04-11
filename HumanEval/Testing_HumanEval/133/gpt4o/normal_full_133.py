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
    assert sum_squares([1, 2, 3]) == 14
    assert sum_squares([0.1, 0.2, 0.3]) == 3
    assert sum_squares([-1, -2, -3]) == 14
    assert sum_squares([1.5, 2.5, 3.5]) == 29
    assert sum_squares([0, 0, 0]) == 0
    assert sum_squares([]) == 0
    assert sum_squares([1, 4, 9]) == 98
    assert sum_squares([1, 3, 5, 7]) == 84
    assert sum_squares([1.4, 4.2, 0]) == 29
    assert sum_squares([-2.4, 1, 1]) == 6

    assert sum_squares([1, 4, 9]) == 98
    assert sum_squares([1, 3, 5, 7]) == 84
    assert sum_squares([1.4, 4.2, 0]) == 29
    assert sum_squares([-2.4, 1, 1]) == 6
    assert sum_squares([1, 2, 3]) == 14
    assert sum_squares([0.1, 0.2, 0.3]) == 3
    assert sum_squares([-1, -2, -3]) == 14
    assert sum_squares([1.5, 2.5, 3.5]) == 29
    assert sum_squares([0, 0, 0]) == 0
    assert sum_squares([]) == 0

