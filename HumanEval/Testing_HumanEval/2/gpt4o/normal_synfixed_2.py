def truncate_number(number: float) -> float:
    
    return number % 1.0



def test():
    assert truncate_number(4.56) == 0.56
    assert truncate_number(10.99) == 0.99
    assert truncate_number(123.123) == 0.123
    assert truncate_number(-45.67) == -0.67
    assert truncate_number(0.0) == 0.0
    assert truncate_number(-0.25) == -0.25
    assert truncate_number(1.0) == 0.0
