def incr_list(l: list):
    
    return [(e + 1) for e in l]




def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"