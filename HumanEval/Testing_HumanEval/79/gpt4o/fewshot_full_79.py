def decimal_to_binary(decimal):
    
    return "db" + bin(decimal)[2:] + "db"



def test():

    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"