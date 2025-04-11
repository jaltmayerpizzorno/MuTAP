def is_prime(n):
    
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True





def test():
        assert is_prime(22) == False
    assert is_prime(23) == True
    assert is_prime(24) == False
    assert is_prime(25) == False
    assert is_prime(26) == False
    assert is_prime(27) == False
    assert is_prime(28) == False
    assert is_prime(29) == True
    assert is_prime(30) == False
    assert is_prime(31) == True
    assert is_prime(32) == False
    assert is_prime(33) == False
    assert is_prime(34) == False
    assert is_prime(35) == False
    assert is_prime(36) == False
    assert is_prime(37) == True
    assert is_prime(38) == False
    assert is_prime(39) == False
    assert is_prime(40) == False
    assert is_prime(41) == True
