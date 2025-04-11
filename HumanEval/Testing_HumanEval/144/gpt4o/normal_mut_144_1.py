def simplify(x, n):
    
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator/denom == int(numerator/denom)):
        return True
    return False



def test():
        assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("2/3", "3/2") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("3/4", "2/3") == False
    assert simplify("5/6", "6/5") == True
    assert simplify("7/8", "8/7") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("2/5", "5/2") == True
    assert simplify("3/6", "6/3") == True
    assert simplify("2/4", "4/2") == True
    assert simplify("5/7", "7/5") == True
    # New test case to detect fault
    assert simplify("4/5", "5/4") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/7", "7/1") == True
