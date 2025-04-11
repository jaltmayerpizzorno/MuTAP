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
        assert specialFilter([0, 5, 12, 22, 33]) == 1
    assert specialFilter([13, 15, 17, 19, 21]) == 4
    assert specialFilter([100, 101, 103, 105, 107]) == 2
    assert specialFilter([11, 13, 15, 17, 19, 21, 31, 33]) == 6
    assert specialFilter([30, 35, 50, 55, 70, 75]) == 3
    assert specialFilter([-11, -13, -15, -17, -19]) == 0
