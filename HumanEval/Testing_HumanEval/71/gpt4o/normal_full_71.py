def triangle_area(a, b, c):
    
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area



def test():

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 1, 2) == -1  # New test case to detect fault

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 2, 10) == -1  # New test case

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 2, 10) == -1  # New test case to detect the fault

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(12, 35, 37) == 210.0  # Added test case

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 1, 1.5) == -1

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 1, 1) == 0.43  # adding additional test to check precision

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(5, 12, 13) == 30.0 # New test case to detect the fault

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 2, 10) == -1  # New test case to detect the issue

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 1, 1.5) == 0.5

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 2, 10) == -1

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 1, 2) == -1  # New test case to detect the change in the code

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(2, 2, 3) == 1.98

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 1, 2) == -1  # New test case to detect the fault

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(7, 10, 5) == 16.25

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 2, 10) == -1  # New test case to detect the fault

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 2, 10) == -1  # New test case to detect fault

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 1, 2) == -1

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 2, 10) == -1

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 2, 10) == -1  # New test case to detect the fault

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 1, 2) == -1  # New test case to catch the fault

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 1, 1.9) == -1

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(10, 6, 8) == 24.0

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 1, 2) == -1  # New test case to detect the fault

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 10, 12) == -1

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 1, 2) == -1  # New test case to detect fault

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 1, 1.99) == -1  # Should return -1 as it's almost a straight line

    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(10, 10, 10) == 43.3
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(8, 15, 17) == 60.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(5, 5, 8) == 12.0
    assert triangle_area(1, 1, 1) == 0.43

