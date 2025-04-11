def triangle_area(a, h):
    
    return a * h / 2.0





def test():

    assert triangle_area(10, 5) == 25.0
    assert triangle_area(6, 3) == 9.0
    assert triangle_area(8, 4) == 16.0
    assert triangle_area(0, 5) == 0.0
    assert triangle_area(7, 0) == 0.0
    assert triangle_area(10, 5) == 25.0
    assert triangle_area(6, 3) == 9.0
    assert triangle_area(8, 4) == 16.0
    assert triangle_area(0, 5) == 0.0
    assert triangle_area(7, 0) == 0.0
    assert triangle_area(9, 3) == 13.5  # This will fail if integer division is used

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

