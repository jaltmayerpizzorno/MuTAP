def even_odd_count(num):
    
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)



def test():
        assert even_odd_count(123456) == (3, 3)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(13579) == (0, 5)
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(-123) == (1, 2)
    assert even_odd_count(2222) == (4, 0)
    assert even_odd_count(1111) == (0, 4)
    assert even_odd_count(101010) == (3, 3)
    # New test case to detect the fault
    assert even_odd_count(-12) == (1, 1)  # Check if the function returns accurate results with negative input
