def sort_array(arr):
    
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))


def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"