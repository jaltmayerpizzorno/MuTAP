def monotonic(l: list):
    
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False





def test():

    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"