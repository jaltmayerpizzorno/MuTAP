def circular_shift(x, shift):
    
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]



def test():
        assert circular_shift(12345, 2) == '45123'
    assert circular_shift(12345, 5) == '12345'
    assert circular_shift(12345, 6) == '54321'
    assert circular_shift(12345, 0) == '12345'
    assert circular_shift(12345, 3) == '34512'
    assert circular_shift(9876543210, 4) == '3210987654'
    assert circular_shift(1, 1) == '1'
    assert circular_shift(12, 3) == '21'
    assert circular_shift(0, 1) == '0'
    assert circular_shift(123, 3) == '123'
    assert circular_shift(120, 3) == '021'  # New test case to detect the fault
    
test()
