def truncate_number(number: float) -> float:
    
    return number % 1.0




def test():
    assert truncate_number(4.56) == 0.5599999999999996
    assert truncate_number(10.99) == 0.9900000000000002
    assert truncate_number(123.123) == 0.12300000000000466
    assert truncate_number(-45.67) == 0.3299999999999983
    assert truncate_number(0.0) == 0.0
    assert truncate_number(-0.25) == 0.75
    assert truncate_number(1.0) == 0.0
