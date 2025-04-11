def specialFilter(nums):
    
    
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
        
    return count 



def test():

    assert specialFilter([15, 23, 37, 49, 12]) == 2
    assert specialFilter([1, 3, 5, 7, 9]) == 0
    assert specialFilter([123, 456, 789, 135, 975]) == 4
    assert specialFilter([11, 13, 15, 17, 19, 21]) == 5
    assert specialFilter([22, 24, 26, 28, 30]) == 0
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([35, 77, 85, 97, 13]) == 5
    assert specialFilter([-15, -23, -37, -49, -12]) == 0
    assert specialFilter([55, 75, 25, 105, 95]) == 5
    assert specialFilter([111, 131, 151, 171, 191]) == 5

    assert specialFilter([15, 23, 37, 49, 12]) == 2
    assert specialFilter([1, 3, 5, 7, 9]) == 0
    assert specialFilter([123, 456, 789, 135, 975]) == 4
    assert specialFilter([11, 13, 15, 17, 19, 21]) == 5
    assert specialFilter([22, 24, 26, 28, 30]) == 0
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

    assert specialFilter([0, 5, 12, 22, 33]) == 1
    assert specialFilter([13, 15, 17, 19, 21]) == 4
    assert specialFilter([100, 101, 103, 105, 107]) == 2
    assert specialFilter([11, 13, 15, 17, 19, 21, 31, 33]) == 6
    assert specialFilter([30, 35, 50, 55, 70, 75]) == 3
    assert specialFilter([-11, -13, -15, -17, -19]) == 0

