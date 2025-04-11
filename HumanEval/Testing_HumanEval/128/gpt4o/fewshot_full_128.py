def prod_signs(arr):
    
    if not arr: 
        return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])



def test():

    assert prod_signs([1, 2, 3]) == 6
    assert prod_signs([-1, -2, -3]) == -6
    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([1, 0, -3]) == 0
    assert prod_signs([]) == None
    assert prod_signs([-1, 2, -3, 4]) == 10
    assert prod_signs([1, 2, 3]) == 6
    assert prod_signs([-1, -2, -3]) == -6
    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([1, 0, -3]) == 0
    assert prod_signs([]) == None
    assert prod_signs([-1, 2, -3, 4]) == -10
    assert prod_signs([1, 2, 2, -4]) == -9

    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([0, 1]) == 0
    assert prod_signs([]) == None

    assert prod_signs([1, 2, 3]) == 6
    assert prod_signs([-1, -2, -3]) == -6
    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([1, 0, -3]) == 0
    assert prod_signs([]) == None
    assert prod_signs([-1, 2, -3, 4]) == 10
    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([0, 1]) == 0

    assert prod_signs([1, 2, 2, -4]) == -9  # New test case to test the provided example
    assert prod_signs([0, 1]) == 0  # New test case to test the provided example
    assert prod_signs([]) == None  # Existing test case to ensure same behavior
    assert prod_signs([1, 2, 3]) == 6  # Existing test case to ensure same behavior
    assert prod_signs([-1, -2, -3]) == -6  # Existing test case to ensure same behavior
    assert prod_signs([1, -2, 3]) == -6  # Existing test case to ensure same behavior
    assert prod_signs([1, 0, -3]) == 0  # Existing test case to ensure same behavior
    assert prod_signs([-1, 2, -3, 4]) == -10  # Corrected existing test case to match the correct logic

    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([0, 1]) == 0
    assert prod_signs([1, -2, -3]) == -6
    assert prod_signs([-1, 2, -3, 4]) == 10

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert prod_signs([1, 2, 3]) == 6
    assert prod_signs([-1, -2, -3]) == -6
    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([1, 0, -3]) == 0
    assert prod_signs([]) == None
    assert prod_signs([-1, 2, -3, 4]) == 10
    assert prod_signs([0, 1, 2, 3]) == 0
    assert prod_signs([-1, 0, 1]) == 0
    assert prod_signs([2, -3, 4, -5, 6]) == 20

    assert prod_signs([1, 2, 2, -4]) == -9

    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([0, 1]) == 0
    assert prod_signs([]) == None
    assert prod_signs([1, 2, 3]) == 6
    assert prod_signs([-1, -2, -3]) == -6
    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([1, 0, -3]) == 0
    assert prod_signs([-1, 2, -3, 4]) == 10

    assert prod_signs([1, 2, 2, -4]) == -9  # Adding this specific test case to detect the fault
    assert prod_signs([1, 2, 3]) == 6
    assert prod_signs([-1, -2, -3]) == -6
    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([1, 0, -3]) == 0
    assert prod_signs([]) == None
    assert prod_signs([-1, 2, -3, 4]) == 10

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

