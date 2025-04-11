def cycpattern_check(a , b):
    
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False



def test():
        assert cycpattern_check("abcdef", "cde") == True
    assert cycpattern_check("abcdef", "cdefa") == False
    assert cycpattern_check("abcdef", "efab") == False
    assert cycpattern_check("abcdef", "abcdefg") == False
    assert cycpattern_check("abcabc", "abc") == True
    assert cycpattern_check("aaaaaa", "aaa") == True
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abcdef", "") == True
    assert cycpattern_check("", "") == True
    # New test case to detect fault
    assert cycpattern_check("abab", "baa") == False
