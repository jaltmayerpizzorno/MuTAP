def is_simple_power(x, n):
    
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (power < x): 
        power = power * n 
    return (power == x) 



def test():
        assert is_simple_power(1, 1) == True
    assert is_simple_power(8, 2) == True
    assert is_simple_power(9, 3) == True
    assert is_simple_power(16, 4) == True
    assert is_simple_power(27, 3) == True
    assert is_simple_power(81, 9) == True
    assert is_simple_power(125, 5) == True
    assert is_simple_power(32, 2) == True
    assert is_simple_power(49, 7) == True
    assert is_simple_power(7, 1) == False
    # New test cases
    assert is_simple_power(1, 4) == True  # should return True for x == 1 and any n > 0
    assert is_simple_power(2, 2) == True  # 2 is a power of 2
    assert is_simple_power(3, 2) == False  # 3 is not a power of 2
    assert is_simple_power(3, 1) == False  # 3 is not equal to 1
    assert is_simple_power(5, 3) == False  # 5 is not a power of 3
