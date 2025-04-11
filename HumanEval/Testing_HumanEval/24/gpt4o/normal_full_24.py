def largest_divisor(n: int) -> int:
    
    for i in reversed(range(n)):
        if n % i == 0:
            return i





def test():

    assert largest_divisor(10) == 5
    assert largest_divisor(15) == 5
    assert largest_divisor(21) == 7
    assert largest_divisor(1) == 1    assert largest_divisor(7) == 1
    assert largest_divisor(100) == 50
    assert largest_divisor(16) == 8
    assert largest_divisor(25) == 5
    assert largest_divisor(49) == 7
    assert largest_divisor(97) == 1
