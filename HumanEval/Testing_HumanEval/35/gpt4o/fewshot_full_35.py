def max_element(l: list):
    
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m





def test():

    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"