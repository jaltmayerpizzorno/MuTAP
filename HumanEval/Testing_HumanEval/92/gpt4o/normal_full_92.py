def any_int(x, y, z):
  
    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False



def test():

    assert any_int(1, 2, 3) == True
    assert any_int(3, 1, 2) == True
    assert any_int(1, 1, 2) == True
    assert any_int(3, 5, 8) == True
    assert any_int(1, 2, 4) == False
    assert any_int(0, 0, 0) == True
    assert any_int(-1, -2, -3) == True
    assert any_int(1, 2, '3') == False
    assert any_int(1.0, 2, 3) == False
    assert any_int('1', 2, 3) == False
    assert any_int(1, 2, 3) == True
    assert any_int(3, 1, 2) == True
    assert any_int(1, 1, 2) == True
    assert any_int(3, 5, 8) == True
    assert any_int(1, 2, 4) == False
    assert any_int(0, 0, 0) == True
    assert any_int(-1, -2, -3) == True
    assert any_int(1, 2, '3') == False
    assert any_int(1.0, 2, 3) == False
    assert any_int('1', 2, 3) == False
    assert any_int(5, 2, 3) == True  # New test case to detect the fault

    assert any_int(1, 2, 3) == True
    assert any_int(3, 1, 2) == True
    assert any_int(1, 1, 2) == True
    assert any_int(3, 5, 8) == True
    assert any_int(1, 2, 4) == False
    assert any_int(0, 0, 0) == True
    assert any_int(-1, -2, -3) == True
    assert any_int(1, 2, '3') == False
    assert any_int(1.0, 2, 3) == False
    assert any_int('1', 2, 3) == False
    assert any_int(5, 2, 7) == True  # New test case to detect the fault

    assert any_int(1, 2, 3) == True
    assert any_int(3, 1, 2) == True
    assert any_int(1, 1, 2) == True
    assert any_int(3, 5, 8) == True
    assert any_int(1, 2, 4) == False
    assert any_int(0, 0, 0) == True
    assert any_int(-1, -2, -3) == True
    assert any_int(1, 2, '3') == False
    assert any_int(1.0, 2, 3) == False
    assert any_int('1', 2, 3) == False
    assert any_int(3, -2, 1) == True  # Adding this test case to ensure detection of the fault

    assert any_int(1, 2, 3) == True
    assert any_int(3, 1, 2) == True
    assert any_int(1, 1, 2) == True
    assert any_int(3, 5, 8) == True
    assert any_int(1, 2, 4) == False
    assert any_int(0, 0, 0) == True
    assert any_int(-1, -2, -3) == True
    assert any_int(1, 2, '3') == False
    assert any_int(1.0, 2, 3) == False
    assert any_int('1', 2, 3) == False
    assert any_int(5, 2, 7) == True
    assert any_int(3, 2, 2) == False
    assert any_int(3, -2, 1) == True
    assert any_int(3.6, -2.2, 2) == False

    assert any_int(1, 2, 3) == True
    assert any_int(3, 1, 2) == True
    assert any_int(1, 1, 2) == True
    assert any_int(3, 5, 8) == True
    assert any_int(1, 2, 4) == False
    assert any_int(0, 0, 0) == True
    assert any_int(-1, -2, -3) == True
    assert any_int(1, 2, '3') == False
    assert any_int(1.0, 2, 3) == False
    assert any_int('1', 2, 3) == False
    assert any_int(5, 2, 7) == True
    assert any_int(3, 2, 2) == False
    assert any_int(3, -2, 1) == True
    assert any_int(3.6, -2.2, 2) == False

    assert any_int(1, 2, 3) == True
    assert any_int(3, 1, 2) == True
    assert any_int(1, 1, 2) == True
    assert any_int(3, 5, 8) == True
    assert any_int(1, 2, 4) == False
    assert any_int(0, 0, 0) == True
    assert any_int(-1, -2, -3) == True
    assert any_int(1, 2, '3') == False
    assert any_int(1.0, 2, 3) == False
    assert any_int('1', 2, 3) == False
    assert any_int(5, 2, 7) == True  # additional test case
    assert any_int(3, 2, 2) == False  # additional test case
    assert any_int(3, -2, 1) == True  # additional test case
    assert any_int(3.6, -2.2, 2) == False  # additional test case
    assert any_int(5, 3, 2) == False  # additional test case

    assert any_int(1, 2, 3) == True
    assert any_int(3, 1, 2) == True
    assert any_int(1, 1, 2) == True
    assert any_int(3, 5, 8) == True
    assert any_int(1, 2, 4) == False
    assert any_int(0, 0, 0) == True
    assert any_int(-1, -2, -3) == True
    assert any_int(1, 2, '3') == False
    assert any_int(1.0, 2, 3) == False
    assert any_int('1', 2, 3) == False
    assert any_int(3, 1, 1) == False # This should return False because 3 != 1 + 1

    assert any_int(1, 2, 3) == True
    assert any_int(3, 1, 2) == True
    assert any_int(1, 1, 2) == True
    assert any_int(3, 5, 8) == True
    assert any_int(1, 2, 4) == False
    assert any_int(0, 0, 0) == True
    assert any_int(-1, -2, -3) == True
    assert any_int(1, 2, '3') == False
    assert any_int(1.0, 2, 3) == False
    assert any_int('1', 2, 3) == False
    assert any_int(2, 2, 4) == True  # This should be True but the faulty code would return False

    assert any_int(1, 2, 3) == True
    assert any_int(3, 1, 2) == True
    assert any_int(1, 1, 2) == True
    assert any_int(3, 5, 8) == True
    assert any_int(1, 2, 4) == False
    assert any_int(0, 0, 0) == True
    assert any_int(-1, -2, -3) == True
    assert any_int(1, 2, '3') == False
    assert any_int(1.0, 2, 3) == False
    assert any_int('1', 2, 3) == False
    assert any_int(3, -2, 1) == True  # New test case to test negative numbers

    assert any_int(1, 2, 3) == True
    assert any_int(3, 1, 2) == True
    assert any_int(1, 1, 2) == True
    assert any_int(3, 5, 8) == True
    assert any_int(1, 2, 4) == False
    assert any_int(0, 0, 0) == True
    assert any_int(-1, -2, -3) == True
    assert any_int(1, 2, '3') == False
    assert any_int(1.0, 2, 3) == False
    assert any_int('1', 2, 3) == False
    assert any_int(3, 3, 6) == True  # This should be True, but with the fault it will return False

