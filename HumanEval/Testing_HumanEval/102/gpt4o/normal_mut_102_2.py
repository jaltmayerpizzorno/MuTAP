def choose_num(x, y):
    
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1



def test():
        # Test case 1: x > y
    assert choose_num(5, 3) == -1, "Test case 1 failed"

    # Test case 2: y is even
    assert choose_num(2, 4) == 4, "Test case 2 failed"

    # New test case: y is odd, x is even, x < y
    assert choose_num(2, 5) == 4, "New test case failed"  # Checking if it returns the largest even number in range

    # New test case: y is odd, x is odd, x < y
    assert choose_num(3, 7) == 6, "New test case failed"  # Checking if it returns the largest even number in range

    # New test case: x == y and both are odd
    assert choose_num(5, 5) == -1, "New test case failed"  # Checking if it returns -1 when x equals y and are odd

    # New test case: x == y and both are even
    assert choose_num(4, 4) == 4, "New test case failed"  # Checking if it returns y when x equals y and are even

    # New test case: x < y and no even number in range
    assert choose_num(1, 1) == -1, "New test case failed"  # Checking if it returns -1 when there is no even number in range
