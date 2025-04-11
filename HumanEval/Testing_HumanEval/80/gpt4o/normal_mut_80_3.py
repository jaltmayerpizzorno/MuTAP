def is_happy(s):
    
    if len(s) < 3:
      return False

    for i in range(len(s) - 2):
      
      if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
        return False
    return True



def test():
        assert is_happy("abc") == True
    assert is_happy("aabbcc") == False
    assert is_happy("aabcdd") == False
    assert is_happy("abcdef") == True
    assert is_happy("aabb") == False
    assert is_happy("ab") == False
    assert is_happy("") == False
    assert is_happy("abcd") == True
    assert is_happy("aaab") == False
    assert is_happy("aab") == False
    # New test cases
    assert is_happy("abca") == True        # Happy string with a repeated character not in consecutive triplet
    assert is_happy("xyzxyz") == True      # Happy string with repeated segments
    assert is_happy("abccba") == False     # Not a happy string due to consecutive 'cc'
    assert is_happy("abcdabcd") == True    # Happy string with repeated segments
    assert is_happy("abccba") == False     # Not a happy string due to consecutive 'cc'
    assert is_happy("xxyyz") == False      # Not a happy string due to consecutive 'xx' and 'yy'
    assert is_happy("123321") == False     # Not a happy string due to consecutive '33'
