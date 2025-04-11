def greatest_common_divisor(a: int, b: int) -> int:
    
    while b:
        a, b = b, a % b
    return a




def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"