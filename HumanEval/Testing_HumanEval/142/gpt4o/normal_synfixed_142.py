def sum_squares(lst):
    
    result =[]
    for i in range(len(lst)):
        if i %3 == 0:
            result.append(lst[i]**2)
        elif i % 4 == 0 and i%3 != 0:
            result.append(lst[i]**3)
        else:
            result.append(lst[i])
    return sum(result)

def test():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 234
    assert sum_squares([0, -1, -2, -3, -4, -5, -6, -7, -8]) == 102
    assert sum_squares([10, 20, 30, 40, 50]) == 15360
    assert sum_squares([-10, -20, -30, -40, -50]) == 24860
    assert sum_squares([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 3160

test()
