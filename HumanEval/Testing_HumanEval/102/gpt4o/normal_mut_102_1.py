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
    
    # Test case 3: y is odd, x < y, and x != y
    assert choose_num(3, 5) == 4, "Test case 3 failed"

    # Test case 4: y is odd and x = y
    assert choose_num(7, 7) == -1, "Test case 4 failed"

    # Test case 5: x < y and y is even
    assert choose_num(1, 2) == 2, "Test case 5 failed"

    # Test case 6: No even number in range [x, y]
    assert choose_num(5, 5) == -1, "Test case 6 failed"
    
    # Test case 7: Large number test
    assert choose_num(1000000000, 1000000001) == 1000000000, "Test case 7 failed"

test()
