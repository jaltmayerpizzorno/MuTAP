def is_prime(n):
    
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True





def test():
        assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(10) == False
    assert is_prime(13) == True
    assert is_prime(17) == True
    assert is_prime(20) == False
    assert is_prime(23) == True
    assert is_prime(1) == False
#</test>