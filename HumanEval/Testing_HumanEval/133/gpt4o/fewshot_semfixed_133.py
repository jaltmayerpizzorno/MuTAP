def sum_squares(lst):
    
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared


def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"