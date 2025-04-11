def double_the_difference(lst):
    
    return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])



def test():
        assert double_the_difference([1, 2, 3, 4, 5]) == 35  # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    assert double_the_difference([-1, -2, -3, -4, -5]) == 0  # no positive odd numbers
    assert double_the_difference([1.5, 3.5, 5.5]) == 0  # no integers
    assert double_the_difference([0, 2, 4, 6]) == 0  # no odd numbers
    assert double_the_difference([1, -2, 3.0, 4.5, 5, 7]) == 75  # 1^2 + 5^2 + 7^2 = 1 + 25 + 49 = 75
    assert double_the_difference([0, 1, 0, 3, 0, 5]) == 35  # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    assert double_the_difference([0, 1, 0, 3, 0, 5, -1, -3, -5]) == 35  # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    assert double_the_difference([9, -2]) == 81  # 9^2 = 81
    assert double_the_difference([0]) == 0  # no positive odd numbers
