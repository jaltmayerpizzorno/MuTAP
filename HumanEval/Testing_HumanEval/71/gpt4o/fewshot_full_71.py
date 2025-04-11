def triangle_area(a, b, c):
    
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area



def test():

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(6, 8, 10) == 24.0
    assert triangle_area(5, 12, 13) == 30.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(1, 1, 2) == -1
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(6, 8, 10) == 24.0
    assert triangle_area(5, 12, 13) == 30.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(1, 1, 2) == -1
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(5, 5, 10) == -1
    assert triangle_area(0, 0, 0) == -1

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

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(6, 8, 10) == 24.0
    assert triangle_area(5, 12, 13) == 30.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(1, 1, 2) == -1
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(10, 2, 10) == 8.0  # New test case to test the fault in the previous code

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(6, 8, 10) == 24.0
    assert triangle_area(5, 12, 13) == 30.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(1, 1, 2) == -1
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 10) == -1  # New test case added

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(6, 8, 10) == 24.0
    assert triangle_area(5, 12, 13) == 30.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(1, 1, 2) == -1
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 10) == -1

    assert triangle_area(1, 2, 2) == 0.97  # Additional test case to ensure valid triangles are correctly calculated

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

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(6, 8, 10) == 24.0
    assert triangle_area(5, 12, 13) == 30.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(1, 1, 2) == -1
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 10) == -1

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(6, 8, 10) == 24.0
    assert triangle_area(5, 12, 13) == 30.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(1, 1, 2) == -1
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(3, 3, 3) == 3.9

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(6, 8, 10) == 24.0
    assert triangle_area(5, 12, 13) == 30.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(1, 1, 2) == -1
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 10) == -1

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(6, 8, 10) == 24.0
    assert triangle_area(5, 12, 13) == 30.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(1, 1, 2) == -1
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 10) == -1  # New test case to check for invalid triangle

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

