def multiply(a, b):
    
    return abs(a % 10) * abs(b % 10)



def test():
        assert multiply(12, 3) == 6
    assert multiply(-12, 3) == 6
    assert multiply(12, -3) == 6
    assert multiply(-12, -3) == 6
    assert multiply(0, 3) == 0
    assert multiply(12, 0) == 0
    assert multiply(0, 0) == 0
    assert multiply(15, 25) == 25
    assert multiply(99, 99) == 81
    # New test case to detect the fault
    assert multiply(148, 412) != 16
    assert multiply(19, 28) != 72
    assert multiply(14, -15) != 20
    assert multiply(2020, 1851) == 0  # Also to ensure correct behavior against the example
