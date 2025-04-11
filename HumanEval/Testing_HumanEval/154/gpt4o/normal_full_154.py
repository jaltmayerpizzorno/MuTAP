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
    assert cycpattern_check("abcdef", "cdefa") == False
    assert cycpattern_check("abcdef", "eabcd") == True  # Added test case to detect fault
    assert cycpattern_check("abcdef", "cde") == True
    assert cycpattern_check("abcdef", "efab") == False
    assert cycpattern_check("abcdef", "abcdefg") == False
    assert cycpattern_check("abcabc", "abc") == True
    assert cycpattern_check("aaaaaa", "aaa") == True
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abcdef", "") == True
    assert cycpattern_check("", "") == True

    assert cycpattern_check("abcdef", "cde") == True
    assert cycpattern_check("abcdef", "cdefa") == False
    assert cycpattern_check("abcdef", "efab") == False
    assert cycpattern_check("abcdef", "abcdefg") == False
    assert cycpattern_check("abcabc", "abc") == True
    assert cycpattern_check("aaaaaa", "aaa") == True
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abcdef", "") == True
    assert cycpattern_check("", "") == True
    assert cycpattern_check("abcdef", "defa") == False

    assert cycpattern_check("abcdef", "cde") == True
    assert cycpattern_check("abcdef", "cdefa") == False
    assert cycpattern_check("abcdef", "efab") == False
    assert cycpattern_check("abcdef", "abcdefg") == False
    assert cycpattern_check("abcabc", "abc") == True
    assert cycpattern_check("aaaaaa", "aaa") == True
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abcdef", "") == True
    assert cycpattern_check("", "") == True
    assert cycpattern_check("abab", "baa") == False

    assert cycpattern_check("abcdef", "cde") == True
    assert cycpattern_check("abcdef", "cdefa") == False
    assert cycpattern_check("abcdef", "efab") == False
    assert cycpattern_check("abcdef", "abcdefg") == False
    assert cycpattern_check("abcabc", "abc") == True
    assert cycpattern_check("aaaaaa", "aaa") == True
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abcdef", "") == True
    assert cycpattern_check("", "") == True
    assert cycpattern_check("whassup", "psus") == False  # New test case
    assert cycpattern_check("himenss", "simen") == False  # New test case

    assert cycpattern_check("abcdef", "cde") == True
    assert cycpattern_check("abcdef", "cdefa") == False
    assert cycpattern_check("abcdef", "efab") == False
    assert cycpattern_check("abcdef", "abcdefg") == False
    assert cycpattern_check("abcabc", "abc") == True
    assert cycpattern_check("aaaaaa", "aaa") == True
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abcdef", "") == True
    assert cycpattern_check("", "") == True
    assert cycpattern_check("abab", "aba") == True

    assert cycpattern_check("abcdef", "cde") == True
    assert cycpattern_check("abcdef", "cdefa") == False
    assert cycpattern_check("abcdef", "efab") == False
    assert cycpattern_check("abcdef", "abcdefg") == False
    assert cycpattern_check("abcabc", "abc") == True
    assert cycpattern_check("aaaaaa", "aaa") == True
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abcdef", "") == True
    assert cycpattern_check("", "") == True
    assert cycpattern_check("abab", "baa") == False

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

    assert cycpattern_check("abcdef", "cde") == True
    assert cycpattern_check("abcdef", "cdefa") == False
    assert cycpattern_check("abcdef", "efab") == False
    assert cycpattern_check("abcdef", "abcdefg") == False
    assert cycpattern_check("abcabc", "abc") == True
    assert cycpattern_check("aaaaaa", "aaa") == True
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abcdef", "") == True
    assert cycpattern_check("", "") == True
    assert cycpattern_check("abab", "baa") == False  # New test case to detect the fault

    assert cycpattern_check("abcdef", "cde") == True
    assert cycpattern_check("abcdef", "cdefa") == False
    assert cycpattern_check("abcdef", "efab") == False
    assert cycpattern_check("abcdef", "abcdefg") == False
    assert cycpattern_check("abcabc", "abc") == True
    assert cycpattern_check("aaaaaa", "aaa") == True
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abcdef", "") == True
    assert cycpattern_check("", "") == True
    assert cycpattern_check("abab", "baa") == False  # New test case to detect the fault

    assert cycpattern_check("abcdef", "cde") == True
    assert cycpattern_check("abcdef", "cdefa") == False
    assert cycpattern_check("abcdef", "efab") == False
    assert cycpattern_check("abcdef", "abcdefg") == False
    assert cycpattern_check("abcabc", "abc") == True
    assert cycpattern_check("aaaaaa", "aaa") == True
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abcdef", "") == True
    assert cycpattern_check("", "") == True
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("himenss", "simen") == False

    assert cycpattern_check("abcdef", "cde") == True
    assert cycpattern_check("abcdef", "cdefa") == False
    assert cycpattern_check("abcdef", "efab") == False
    assert cycpattern_check("abcdef", "abcdefg") == False
    assert cycpattern_check("abcabc", "abc") == True
    assert cycpattern_check("aaaaaa", "aaa") == True
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abcdef", "") == True
    assert cycpattern_check("", "") == True
    assert cycpattern_check("abcdef", "def") == True

