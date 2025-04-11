def modp(n: int, p: int):
    
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret





def test():
        assert modp(0, 7) == 1  # 2^0 % 7 = 1
    assert modp(1, 7) == 2  # 2^1 % 7 = 2
    assert modp(2, 7) == 4  # 2^2 % 7 = 4
    assert modp(3, 7) == 1  # 2^3 % 7 = 8 % 7 = 1
    assert modp(4, 7) == 2  # 2^4 % 7 = 16 % 7 = 2
    assert modp(10, 7) == 2  # 2^10 % 7 = 1024 % 7 = 2
    assert modp(5, 13) == 6  # 2^5 % 13 = 32 % 13 = 6
    assert modp(6, 13) == 12  # 2^6 % 13 = 64 % 13 = 12
    assert modp(6, 5) == 4  # 2^6 % 5 = 64 % 5 = 4
    assert modp(10, 19) == 17
    assert modp(3, 5) == 3  # This tests the erroneous code snippet that raised the power of `ret` instead of 2
