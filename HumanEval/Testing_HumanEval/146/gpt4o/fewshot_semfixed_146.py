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
    assert specialFilter([11, 13, 15, 17, 19, 20, 22, 24]) == 5
    assert specialFilter([9, 21, 33, 44, 55, 67, 78, 89, 90]) == 2
    assert specialFilter([10, 20, 30, 40, 50, 60, 70, 80, 90]) == 0
    assert specialFilter([11, 22, 33, 44, 55, 66, 77, 88, 99]) == 5
