def anti_shuffle(s):
    
    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])



def test():

    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"