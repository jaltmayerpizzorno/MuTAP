def reverse_delete(s,c):
    
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)


def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"