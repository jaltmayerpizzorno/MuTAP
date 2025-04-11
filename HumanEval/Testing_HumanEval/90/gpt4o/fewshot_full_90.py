def next_smallest(lst):
    
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]



def test():

    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"