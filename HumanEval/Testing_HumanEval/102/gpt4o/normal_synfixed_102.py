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

    # Test case 3: x == y
    assert choose_num(3, 3) == -1, "Test case 3 failed"

    # Test case 4: y is odd and x < y
    assert choose_num(1, 5) == 4, "Test case 4 failed"

    # Test case 5: y is odd and x < y
    assert choose_num(0, 7) == 6, "Test case 5 failed"

    # Additional edge case
    assert choose_num(0, 1) == 0, "Additional edge case failed"

test()
