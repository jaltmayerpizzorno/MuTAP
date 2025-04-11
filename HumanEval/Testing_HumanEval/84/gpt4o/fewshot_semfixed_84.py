def solve(N):
    
    return bin(sum(int(i) for i in str(N)))[2:]


def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"