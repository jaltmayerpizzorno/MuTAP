def rounded_avg(n, m):
    
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))

def test():
    assert rounded_avg(1, 10) == '0b101'
    assert rounded_avg(1, 1) == '0b1'
    assert rounded_avg(0, 10) == '0b101'
    assert rounded_avg(5, 15) == '0b1011'
    assert rounded_avg(10, 5) == -1
#</test>