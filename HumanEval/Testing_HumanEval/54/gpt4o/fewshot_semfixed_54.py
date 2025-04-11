def same_chars(s0: str, s1: str):
    
    return set(s0) == set(s1)




def test():
    assert same_chars("abc", "cba") == True
    assert same_chars("abc", "abcd") == False
    assert same_chars("abc", "abcc") == True
    assert same_chars("abc", "def") == False
    assert same_chars("abc", "bac") == True
