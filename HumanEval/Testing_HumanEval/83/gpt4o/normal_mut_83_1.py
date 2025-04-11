def starts_one_ends(n):
    
    if n == 1: 
        return 1
    return 18 * (10 ** (n - 2))



def test():
        assert starts_one_ends(1) == 1
    assert starts_one_ends(2) == 18
    assert starts_one_ends(3) == 180
    assert starts_one_ends(4) == 1800
    assert starts_one_ends(5) == 18000
    assert starts_one_ends(6) == 180000
    assert starts_one_ends(0) == 0  # Additional test case to catch any faults
    assert starts_one_ends(-1) == 0  # Additional test case to catch any faults

