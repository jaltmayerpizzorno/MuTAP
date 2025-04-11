def digits(n):
    
    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        if int_digit%2 == 1:
            product= product*int_digit
            odd_count+=1
    if odd_count ==0:
        return 0
    else:
        return product



def test():

    assert digits(1234) == 3
    assert digits(1111) == 1
    assert digits(2468) == 0
    assert digits(13579) == 945
    assert digits(0) == 0
    assert digits(222222221) == 1
    assert digits(1000000000) == 1
    assert digits(1234) == 3
    assert digits(1111) == 1
    assert digits(2468) == 0
    assert digits(13579) == 945
    assert digits(0) == 0
    assert digits(222222221) == 1
    assert digits(1000000000) == 1
    assert digits(123456789) == 945  # new test case to detect the fault

    assert digits(1234) == 3
    assert digits(1111) == 1
    assert digits(2468) == 0
    assert digits(13579) == 945
    assert digits(0) == 0
    assert digits(222222221) == 1
    assert digits(1000000000) == 1
    assert digits(1020304050) == 15 # 1*3*5 = 15

    assert digits(1234) == 3
    assert digits(1111) == 1
    assert digits(2468) == 0
    assert digits(13579) == 945
    assert digits(0) == 0
    assert digits(222222221) == 1
    assert digits(1000000000) == 1
    assert digits(-13579) == -945   # New test case to check for negative integers

