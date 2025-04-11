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
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939
    assert sum_squares([0, -1, -2, -3, -4, -5, -6, -7, -8]) == -546
    assert sum_squares([10, 20, 30, 40, 50]) == 126750
    assert sum_squares([-10, -20, -30, -40, -50]) == -123350
    assert sum_squares([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 7534
    # New test cases to detect the change
    assert sum_squares([1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert sum_squares([3, 3, 3, 3, 3, 3, 3, 3, 3]) == 90
    assert sum_squares([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1638
    assert sum_squares([1, 0, 0, 0, 1, 0, 0, 0, 1]) == 3
