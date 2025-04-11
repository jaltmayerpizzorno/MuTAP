def sort_third(l: list):
    
    l = list(l)
    l[::3] = sorted(l[::3])
    return l





def test():

    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"