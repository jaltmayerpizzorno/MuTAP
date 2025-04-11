def is_sorted(lst):
    
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i]+=1 
    if any(count_digit[i] > 2 for i in lst):
        return False
    if all(lst[i-1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False
    
    



def test():

    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([1, 2, 2, 3, 4, 5]) == True
    assert is_sorted([1, 2, 2, 2, 3, 4, 5]) == False
    assert is_sorted([1, 3, 2, 4, 5]) == False
    assert is_sorted([1, 2, 2, 4, 5, 5]) == True
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

    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([1, 2, 2, 3, 4, 5]) == True
    assert is_sorted([1, 2, 2, 2, 3, 4, 5]) == False
    assert is_sorted([1, 3, 2, 4, 5]) == False
    assert is_sorted([1, 2, 2, 4, 5, 5]) == True
    assert is_sorted([1, 2, 3, 4, 5, 5, 5]) == False  # New test case to detect the issue in previous code

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([1, 2, 2, 3, 4, 5]) == True
    assert is_sorted([1, 2, 2, 2, 3, 4, 5]) == False
    assert is_sorted([1, 3, 2, 4, 5]) == False
    assert is_sorted([1, 2, 2, 4, 5, 5]) == True
    assert is_sorted([1, 2, 2]) == True
    assert is_sorted([1]) == True
    assert is_sorted([1, 1, 1]) == False
    assert is_sorted([1, 2, 2, 3, 3, 4, 4, 4]) == False

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([1, 2, 2, 3, 4, 5]) == True
    assert is_sorted([1, 2, 2, 2, 3, 4, 5]) == False
    assert is_sorted([1, 3, 2, 4, 5]) == False
    assert is_sorted([1, 2, 2, 4, 5, 5]) == True
    assert is_sorted([1, 2, 3, 4, 5, 5, 5]) == False

