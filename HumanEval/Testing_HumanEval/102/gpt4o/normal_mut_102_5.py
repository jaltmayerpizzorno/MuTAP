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

    # Test case 3: y is odd and x != y
    assert choose_num(2, 5) == 4, "Test case 3 failed"

    # Test case 4: x == y and x is odd
    assert choose_num(3, 3) == -1, "Test case 4 failed"

    # Test case 5: x == y and x is even
    assert choose_num(4, 4) == 4, "Test case 5 failed"

    # Test case 6: x is less than y, y is odd
    assert choose_num(6, 13) == 12, "Test case 6 failed"
