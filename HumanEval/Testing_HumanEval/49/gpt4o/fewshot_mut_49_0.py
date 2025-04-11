def modp(n: int, p: int):
    
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret





def test():
        assert modp(3, 5) == 3
    assert modp(4, 7) == 2
    assert modp(5, 11) == 10
    assert modp(6, 13) == 12
    assert modp(10, 17) == 4
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1
#</test>