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

    assert choose_num(5, 3) == -1, "Test case 1 failed"
    assert choose_num(2, 4) == 4, "Test case 2 failed"
    assert choose_num(3, 5) == 4, "Test case 3 failed"
    assert choose_num(7, 7) == -1, "Test case 4 failed"
    assert choose_num(1, 2) == 2, "Test case 5 failed"
    assert choose_num(5, 5) == -1, "Test case 6 failed"
    assert choose_num(1000000000, 1000000001) == 1000000000, "Test case 7 failed"

    assert choose_num(5, 3) == -1, "Test case 1 failed"
    assert choose_num(2, 4) == 4, "Test case 2 failed"
    assert choose_num(3, 3) == -1, "New test case failed"
    assert choose_num(3, 5) == 4, "New test case failed"

    assert choose_num(5, 3) == -1, "Test case 1 failed"
    assert choose_num(2, 4) == 4, "Test case 2 failed"
    assert choose_num(2, 5) == 4, "New test case failed"
    assert choose_num(4, 4) == 4, "New test case failed"
    assert choose_num(3, 3) == -1, "New test case failed"

    assert choose_num(5, 3) == -1, "Test case 1 failed"
    assert choose_num(2, 4) == 4, "Test case 2 failed"
    assert choose_num(3, 3) == -1, "Test case 3 failed"
    assert choose_num(2, 5) == 4, "Test case 4 failed"

    assert choose_num(5, 3) == -1, "Test case 1 failed"
    assert choose_num(2, 4) == 4, "Test case 2 failed"
    assert choose_num(3, 3) == -1, "Test case 3 failed"
    assert choose_num(2, 5) == 4, "Test case 4 failed"
    assert choose_num(-1, 4) == 4, "Test case 5 failed"

    assert choose_num(5, 3) == -1, "Test case 1 failed"
    assert choose_num(2, 4) == 4, "Test case 2 failed"
    assert choose_num(3, 3) == -1, "Test case 3 failed"
    assert choose_num(2, 5) == 4, "Test case 4 failed"
    assert choose_num(6, 5) == -1, "Test case 5 failed"
    assert choose_num(2, 7) == 6, "Test case 6 failed"

    assert choose_num(5, 3) == -1, "Test case 1 failed"
    assert choose_num(2, 4) == 4, "Test case 2 failed"
    assert choose_num(2, 5) == 4, "New test case failed"  # Checking if it returns the largest even number in range
    assert choose_num(3, 7) == 6, "New test case failed"  # Checking if it returns the largest even number in range
    assert choose_num(5, 5) == -1, "New test case failed"  # Checking if it returns -1 when x equals y and are odd
    assert choose_num(4, 4) == 4, "New test case failed"  # Checking if it returns y when x equals y and are even
    assert choose_num(1, 1) == -1, "New test case failed"  # Checking if it returns -1 when there is no even number in range

    assert choose_num(5, 3) == -1, "Test case 1 failed"
    assert choose_num(2, 4) == 4, "Test case 2 failed"
    assert choose_num(3, 3) == -1, "Test case 3 failed"
    assert choose_num(2, 5) == 4, "Test case 4 failed"
    assert choose_num(3, 7) == 6, "Test case 5 failed"
    assert choose_num(2, 8) == 8, "Test case 6 failed"
    assert choose_num(5, 3) == -1, "Test case 7 failed"
    assert choose_num(3, 9) == 8, "Test case 8 failed"

    assert choose_num(5, 3) == -1, "Test case 1 failed"
    assert choose_num(2, 4) == 4, "Test case 2 failed"
    assert choose_num(2, 7) == 6, "Test case 3 failed"
    assert choose_num(3, 3) == -1, "Test case 4 failed"
    assert choose_num(10, 6) == -1, "Test case 5 failed"
    assert choose_num(13, 12) == -1, "Test case 6 failed"
    assert choose_num(10, 7) == -1, "Test case 7 failed"

    assert choose_num(5, 3) == -1, "Test case 1 failed"
    assert choose_num(2, 4) == 4, "Test case 2 failed"
    assert choose_num(2, 5) == 4, "Test case 3 failed"
    assert choose_num(3, 3) == -1, "Test case 4 failed"
    assert choose_num(4, 4) == 4, "Test case 5 failed"
    assert choose_num(6, 13) == 12, "Test case 6 failed"

    assert choose_num(5, 3) == -1, "Test case 1 failed"
    assert choose_num(2, 4) == 4, "Test case 2 failed"
    assert choose_num(3, 3) == -1, "Test case 3 failed"
    assert choose_num(2, 5) == 4, "Test case 4 failed"
    assert choose_num(4, 5) == 4, "Test case 5 failed"
    assert choose_num(1, 1) == -1, "New test case failed"

    assert choose_num(5, 3) == -1, "Test case 1 failed"
    assert choose_num(2, 4) == 4, "Test case 2 failed"
    assert choose_num(10, 15) == 14, "New test case failed"

