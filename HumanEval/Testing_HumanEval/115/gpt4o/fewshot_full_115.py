def max_fill(grid, capacity):
    import math
    
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])



def test():

    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"