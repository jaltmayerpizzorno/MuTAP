def is_happy(s):
    
    if len(s) < 3:
      return False

    for i in range(len(s) - 2):
      
      if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
        return False
    return True



def test():
        assert is_happy("abc") == True
    assert is_happy("aabb") == False
    assert is_happy("aab") == False
    assert is_happy("abcdefg") == True
    assert is_happy("abccba") == False
    assert is_happy("xyzzyx") == False  # New test case to check fault
#</test>