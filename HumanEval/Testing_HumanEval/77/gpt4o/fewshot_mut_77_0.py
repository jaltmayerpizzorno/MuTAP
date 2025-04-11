def iscube(a):
    
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a



def test():
        assert iscube(8) == True
    assert iscube(27) == True
    assert iscube(16) == False
    assert iscube(-27) == True
    assert iscube(0) == True
    assert iscube(180) == False
#</test>
