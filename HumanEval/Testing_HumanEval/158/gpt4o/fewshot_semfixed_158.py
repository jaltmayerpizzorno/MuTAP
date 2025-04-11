def find_max(words):
   
    return sorted(words, key = lambda x: (-len(set(x)), x))[0]


def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"