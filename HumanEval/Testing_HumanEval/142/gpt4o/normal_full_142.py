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
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939
    assert sum_squares([0, -1, -2, -3, -4, -5, -6, -7, -8]) == -546
    assert sum_squares([10, 20, 30, 40, 50]) == 126750
    assert sum_squares([-10, -20, -30, -40, -50]) == -123350
    assert sum_squares([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 7534
    assert sum_squares([3, 6, 9, 12, 15]) == 2439  # 3^2 + 6 + 9^2 + 12^3 + 15 = 9 + 6 + 81 + 1728 + 15 = 1839

    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939
    assert sum_squares([0, -1, -2, -3, -4, -5, -6, -7, -8]) == -546
    assert sum_squares([10, 20, 30, 40, 50]) == 126750
    assert sum_squares([-10, -20, -30, -40, -50]) == -123350
    assert sum_squares([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 7534
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939
    assert sum_squares([0, -1, -2, -3, -4, -5, -6, -7, -8]) == -546
    assert sum_squares([10, 20, 30, 40, 50]) == 126750
    assert sum_squares([-10, -20, -30, -40, -50]) == -123350
    assert sum_squares([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 7534
    assert sum_squares([1, 2, 3, 4, 5]) == 85  # Detects difference in 'elif' condition logic

    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939
    assert sum_squares([0, -1, -2, -3, -4, -5, -6, -7, -8]) == -546
    assert sum_squares([10, 20, 30, 40, 50]) == 126750
    assert sum_squares([-10, -20, -30, -40, -50]) == -123350
    assert sum_squares([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 7534
    assert sum_squares([3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 38022

    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939
    assert sum_squares([0, -1, -2, -3, -4, -5, -6, -7, -8]) == -546
    assert sum_squares([10, 20, 30, 40, 50]) == 126750
    assert sum_squares([-10, -20, -30, -40, -50]) == -123350
    assert sum_squares([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 7534
    assert sum_squares([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 162

    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939
    assert sum_squares([0, -1, -2, -3, -4, -5, -6, -7, -8]) == -546
    assert sum_squares([10, 20, 30, 40, 50]) == 126750
    assert sum_squares([-10, -20, -30, -40, -50]) == -123350
    assert sum_squares([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 7534
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939
    assert sum_squares([0, -1, -2, -3, -4, -5, -6, -7, -8]) == -546
    assert sum_squares([10, 20, 30, 40, 50]) == 126750
    assert sum_squares([-10, -20, -30, -40, -50]) == -123350
    assert sum_squares([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 7534
    assert sum_squares([1, 2, 3, 4, 5]) == 196  # New test case to check for multiplying by 2 instead of squaring or cubing

    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939
    assert sum_squares([0, -1, -2, -3, -4, -5, -6, -7, -8]) == -546
    assert sum_squares([10, 20, 30, 40, 50]) == 126750
    assert sum_squares([-10, -20, -30, -40, -50]) == -123350
    assert sum_squares([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 7534
    assert sum_squares([1, 1, 1, 1, 1]) == 5  # New test case to detect the previous fault

    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939
    assert sum_squares([0, -1, -2, -3, -4, -5, -6, -7, -8]) == -546
    assert sum_squares([10, 20, 30, 40, 50]) == 126750
    assert sum_squares([-10, -20, -30, -40, -50]) == -123350
    assert sum_squares([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 7534
    assert sum_squares([0, 0, 0, 0]) == 0  # New test case to detect the fault

    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939
    assert sum_squares([0, -1, -2, -3, -4, -5, -6, -7, -8]) == -546
    assert sum_squares([10, 20, 30, 40, 50]) == 126750
    assert sum_squares([-10, -20, -30, -40, -50]) == -123350
    assert sum_squares([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 7534
    assert sum_squares([-1, -5, 2, -1, -5]) == -120

    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939
    assert sum_squares([0, -1, -2, -3, -4, -5, -6, -7, -8]) == -546
    assert sum_squares([10, 20, 30, 40, 50]) == 126750
    assert sum_squares([-10, -20, -30, -40, -50]) == -123350
    assert sum_squares([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 7534
    assert sum_squares([1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert sum_squares([3, 3, 3, 3, 3, 3, 3, 3, 3]) == 90
    assert sum_squares([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1638
    assert sum_squares([1, 0, 0, 0, 1, 0, 0, 0, 1]) == 3

