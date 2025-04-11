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

    # New test case: x == y and not even
    assert choose_num(3, 3) == -1, "New test case failed"

    # New test case: x < y and y is odd
    assert choose_num(3, 5) == 4, "New test case failed"


# Run tests
test()
