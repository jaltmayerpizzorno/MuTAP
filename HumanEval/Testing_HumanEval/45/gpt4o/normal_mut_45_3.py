def triangle_area(a, h):
    
    return a * h / 2.0





def test():
        assert triangle_area(10, 5) == 25.0
    assert triangle_area(0, 5) == 0.0
    assert triangle_area(5, 0) == 0.0
    assert triangle_area(10, 10) == 50.0
    assert triangle_area(3, 6) == 9.0
    assert triangle_area(2.5, 4.2) == 5.25
    assert triangle_area(7, 2) == 7.0  # New test case to detect the fault
