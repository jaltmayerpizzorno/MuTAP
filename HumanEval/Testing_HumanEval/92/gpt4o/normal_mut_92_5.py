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
    assert any_int(3, -2, 1) == True  # New test case to test negative numbers
