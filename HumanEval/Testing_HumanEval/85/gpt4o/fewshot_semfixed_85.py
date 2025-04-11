def add(lst):
    
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])


def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"