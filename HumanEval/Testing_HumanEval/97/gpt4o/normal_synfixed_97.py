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

test()
