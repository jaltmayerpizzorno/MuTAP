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
        assert compare_one(1, 2) == 2
    assert compare_one(2, 1) == 2
    assert compare_one(1, "1.0") == None
    assert compare_one("1,0", "1.0") == None
    assert compare_one(1.5, "1,4") == 1.5
    assert compare_one("2,5", 2.6) == 2.6
    assert compare_one("3,0", "2.9") == "3,0"
    assert compare_one("2.5", 2.5) == None  # New test case
    assert compare_one("2,5", 2.5) == None  # New test case
