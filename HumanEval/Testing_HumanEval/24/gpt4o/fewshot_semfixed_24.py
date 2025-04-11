def largest_divisor(n: int) -> int:
    
    for i in reversed(range(n)):
        if n % i == 0:
            return i




def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"