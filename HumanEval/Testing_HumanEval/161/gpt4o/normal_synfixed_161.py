def solve(s):
    
    flg = 0
    idx = 0
    new_str = list(s)
    for i in s:
        if i.isalpha():
            new_str[idx] = i.swapcase()
            flg = 1
        idx += 1
    s = ""
    for i in new_str:
        s += i
    if flg == 0:
        return s[len(s)::-1]
    return s

def test():
    assert solve("HelloWorld") == "hELLOwORLD"
    assert solve("12345") == "54321"
    assert solve("aBc123") == "AbC123"
    assert solve("!@#") == "#@!"
    assert solve("Python3.8") == "pYTHON3.8"
    assert solve("") == ""
    assert solve("ABCdef") == "abcDEF"
    assert solve("123abcXYZ") == "321zyxCBA"

test()
