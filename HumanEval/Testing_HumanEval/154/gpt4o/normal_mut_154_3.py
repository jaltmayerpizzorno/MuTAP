def cycpattern_check(a , b):
    
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False



def test():
        assert cycpattern_check("abcdef", "defabc") == True
    assert cycpattern_check("abcdef", "cdefab") == True
    assert cycpattern_check("abcdef", "fabcde") == True
    assert cycpattern_check("hello", "ohell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baba") == True
    assert cycpattern_check("himenss", "simen") == False
    assert cycpattern_check("abcdef", "abcdefg") == False
    assert cycpattern_check("aaaaaa", "aaaaa") == True
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abcdef", "") == True
    assert cycpattern_check("", "") == True

