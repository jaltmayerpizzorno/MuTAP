def derivative(xs: list):
    
    return [(i * x) for i, x in enumerate(xs)][1:]





def test():

    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"