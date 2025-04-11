def string_sequence(n: int) -> str:
    
    return ' '.join([str(x) for x in range(n + 1)])





def test():

    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"