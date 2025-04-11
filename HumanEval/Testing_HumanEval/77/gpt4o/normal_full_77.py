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
    assert iscube(216) == True  # 6^3 = 216
    assert iscube(343) == True  # 7^3 = 343
    assert iscube(512) == True  # 8^3 = 512
    assert iscube(729) == True  # 9^3 = 729
    assert iscube(1000) == True  # 10^3 = 1000

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
    assert iscube(729) == True  # New test case to test the fault

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
    assert iscube(216) == True  # 6^3
    assert iscube(-216) == True  # -6^3
    assert iscube(1000) == True  # 10^3
    assert iscube(-1000) == True  # -10^3
    assert iscube(1001) == False  # Not a cube
    assert iscube(729) == True  # 9^3
    assert iscube(-729) == True  # -9^3

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
    assert iscube(729) == True

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
    assert iscube(729) == True  # New test case

