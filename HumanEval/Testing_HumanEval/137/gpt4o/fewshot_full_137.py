def compare_one(a, b):
    
    temp_a, temp_b = a, b
    if isinstance(temp_a, str): 
        temp_a = temp_a.replace(',','.')
    if isinstance(temp_b, str): 
        temp_b = temp_b.replace(',','.')
    if float(temp_a) == float(temp_b): 
        return None
    return a if float(temp_a) > float(temp_b) else b 



def test():

    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"