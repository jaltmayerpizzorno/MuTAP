def iscube(a):
    
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a



def test():

    assert iscube(8) == True
    assert iscube(27) == True
    assert iscube(16) == False
    assert iscube(-27) == True
    assert iscube(0) == True
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert iscube(8) == True
    assert iscube(27) == True
    assert iscube(16) == False
    assert iscube(-27) == True
    assert iscube(0) == True
    assert iscube(2146689) == False  # Additional test case to detect faults

    assert iscube(8) == True
    assert iscube(27) == True
    assert iscube(16) == False
    assert iscube(-27) == True
    assert iscube(0) == True
    assert iscube(180) == False

