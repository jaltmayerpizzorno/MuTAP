def is_prime(n):
    
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True





def test():
        assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-1) == False
    assert is_prime(29) == True
    assert is_prime(97) == True
    assert is_prime(100) == False
#</test>