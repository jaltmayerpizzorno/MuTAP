def rounded_avg(n, m):
    
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))

def test():
    assert rounded_avg(1, 5) == '0b11'
    assert rounded_avg(0, 10) == '0b101'
    assert rounded_avg(5, 5) == '0b101'
    assert rounded_avg(3, 9) == '0b100'
    assert rounded_avg(-2, 2) == '0b0'
    assert rounded_avg(10, 8) == -1
    assert rounded_avg(-5, -1) == '0b111'
    assert rounded_avg(-3, 3) == '0b0'

test()
