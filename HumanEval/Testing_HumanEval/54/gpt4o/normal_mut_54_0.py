def same_chars(s0: str, s1: str):
    
    return set(s0) == set(s1)





def test():
        assert same_chars("abc", "bca") == True
    assert same_chars("abc", "abcd") == False
    assert same_chars("aabbcc", "abcabc") == True
    assert same_chars("", "") == True
    assert same_chars("abc", "") == False
    assert same_chars("abc", "def") == False
    assert same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") == True  # New test case
    assert same_chars("abcd", "dddddddabc") == True  # New test case
    assert same_chars("dddddddabc", "abcd") == True  # New test case
    assert same_chars("eabcd", "dddddddabc") == False  # New test case
    assert same_chars("abcd", "dddddddabce") == False  # New test case
    assert same_chars("eabcdzzzz", "dddzzzzzzzddddabc") == False  # New test case
