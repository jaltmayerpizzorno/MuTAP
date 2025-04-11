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
        # Original test cases
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939
    assert sum_squares([0, -1, -2, -3, -4, -5, -6, -7, -8]) == -546
    assert sum_squares([10, 20, 30, 40, 50]) == 126750
    assert sum_squares([-10, -20, -30, -40, -50]) == -123350
    assert sum_squares([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 7534
    
    # New test case to detect the fault
    assert sum_squares([1, 2, 3, 4, 5]) == 85  # Detects difference in 'elif' condition logic
