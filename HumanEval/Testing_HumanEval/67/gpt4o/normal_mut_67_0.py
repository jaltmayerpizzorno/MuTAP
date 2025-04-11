def fruit_distribution(s,n):
    
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)



def test():
        assert fruit_distribution("1 2 3", 10) == 4
    assert fruit_distribution("5 5 5", 20) == 5
    assert fruit_distribution("10 20 30", 100) == 40
    assert fruit_distribution("7 8 9 10", 50) == 16
    assert fruit_distribution("15 15 15 15", 70) == 10
    assert fruit_distribution("0 0 0 0", 0) == 0
    assert fruit_distribution("100 200", 500) == 200
    assert fruit_distribution("", 30) == 30
    assert fruit_distribution("1 a 2 b 3 c", 10) == 4
    # New test case to detect the change
    assert fruit_distribution("2 apples and 3 oranges", 100) == 95  # This should detect the fault
