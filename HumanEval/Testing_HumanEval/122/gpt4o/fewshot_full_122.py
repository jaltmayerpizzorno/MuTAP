def add_elements(arr, k):
    
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)



def test():

    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"