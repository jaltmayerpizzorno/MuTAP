def starts_one_ends(n):
    
    if n == 1: 
        return 1
    return 18 * (10 ** (n - 2))



def test():

    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"