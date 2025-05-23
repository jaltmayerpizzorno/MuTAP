def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    return a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b



def test():
        assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(6, 8, 10) == True
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(2, 2, 2) == False
    assert right_angle_triangle(10, 6, 8) == True
    assert right_angle_triangle(0, 0, 0) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(3, 4, 6) == False  # New test case to detect the change
