def solve(N):
    
    return bin(sum(int(i) for i in str(N)))[2:]

def test():
    assert solve(123) == '110'  # 1+2+3=6, which is 110 in binary
    assert solve(456) == '1111'  # 4+5+6=15, which is 1111 in binary
    assert solve(0) == '0'  # 0 in decimal is 0 in binary
    assert solve(789) == '1110'  # 7+8+9=24, which is 11000 in binary
    assert solve(1) == '1'  # 1 in decimal is 1 in binary
    assert solve(999) == '11001'  # 9+9+9=27, which is 11011 in binary
    assert solve(10) == '1'  # 1+0=1, which is 1 in binary
    assert solve(111) == '11'  # 1+1+1=3, which is 11 in binary
