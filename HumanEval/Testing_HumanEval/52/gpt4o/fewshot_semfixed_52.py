def below_threshold(l: list, t: int):
    
    for e in l:
        if e >= t:
            return False
    return True




def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"