def iscube(a):
    
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a



def test():
        assert iscube(27) == True
    assert iscube(-27) == True
    assert iscube(0) == True
    assert iscube(1) == True
    assert iscube(2) == False
    assert iscube(8) == True
    assert iscube(-8) == True
    assert iscube(9) == False
    assert iscube(64) == True
    assert iscube(125) == True
    assert iscube(126) == False
    # New test case to detect the fault
    assert iscube(729) == True
