def triangle_area(a, b, c):
    
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area



def test():
        assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    # New test case to detect the previous fault
    assert triangle_area(1, 10, 12) == -1
