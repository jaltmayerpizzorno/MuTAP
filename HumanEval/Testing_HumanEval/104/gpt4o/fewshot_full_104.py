def unique_digits(x):
    
    odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)



def test():

    assert unique_digits([135, 246, 357, 789]) == [135, 357]
    assert unique_digits([222, 333, 555, 777]) == [333, 555, 777]
    assert unique_digits([123, 234, 345, 456]) == []
    assert unique_digits([111, 131, 151, 171]) == [111, 131, 151, 171]
    assert unique_digits([246, 864, 975, 333]) == [333, 975]
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert unique_digits([152, 323, 1422, 10]) == []
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([242, 333, 555, 777]) == [333, 555, 777]
    assert unique_digits([82, 131, 151, 171]) == [131, 151, 171]
    assert unique_digits([246, 864, 975, 333]) == [333, 975]

    assert unique_digits([135, 246, 357, 789]) == [135, 357]
    assert unique_digits([222, 333, 555, 777]) == [333, 555, 777]
    assert unique_digits([123, 234, 345, 456]) == []
    assert unique_digits([111, 131, 151, 171]) == [111, 131, 151, 171]
    assert unique_digits([246, 864, 975, 333]) == [333, 975]
    assert unique_digits([135, 246, 357, 789, 131]) == [131, 135, 357]

