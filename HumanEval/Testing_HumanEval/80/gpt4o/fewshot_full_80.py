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
    assert is_happy("abc") == True
    assert is_happy("aabb") == False
    assert is_happy("aab") == False
    assert is_happy("abcdefg") == True
    assert is_happy("abccba") == False
    assert is_happy("abcba") == False  # New test case to detect the fault in the previous code

    assert is_happy("abc") == True
    assert is_happy("aabb") == False
    assert is_happy("aab") == False
    assert is_happy("abcdefg") == True
    assert is_happy("abccba") == False
    assert is_happy("acb") == True
    assert is_happy("xyzzyx") == False
    assert is_happy("xaxbx") == True

    assert is_happy("abc") == True
    assert is_happy("aabb") == False
    assert is_happy("aab") == False
    assert is_happy("abcdefg") == True
    assert is_happy("abccba") == False
    assert is_happy("123456789") == True

    assert is_happy("abc") == True
    assert is_happy("aabb") == False
    assert is_happy("aab") == False
    assert is_happy("abcdefg") == True
    assert is_happy("abccba") == False
    assert is_happy("abcd") == True  # New test case to ensure correctness for longer strings

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert is_happy("abc") == True
    assert is_happy("aabb") == False
    assert is_happy("aab") == False
    assert is_happy("abcdefg") == True
    assert is_happy("abccba") == False
    assert is_happy("abca") == False  # New test case to catch the previous fault

    assert is_happy("abc") == True
    assert is_happy("aabb") == False
    assert is_happy("aab") == False
    assert is_happy("abcdefg") == True
    assert is_happy("abccba") == False
    assert is_happy("abac") == True  # New test case to ensure correctness

    assert is_happy("abc") == True
    assert is_happy("aabb") == False
    assert is_happy("aab") == False
    assert is_happy("abcdefg") == True
    assert is_happy("abccba") == False
    assert is_happy("xyzzyx") == False  # New test case to check fault

    assert is_happy("adbxa") == True
    assert is_happy("xyyxx") == False
    assert is_happy("abcd") == True
    assert is_happy("aabbcc") == False
    assert is_happy("xyzabc") == True

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert is_happy("abc") == True
    assert is_happy("aabb") == False
    assert is_happy("aab") == False
    assert is_happy("abcdefg") == True
    assert is_happy("abccba") == False
    assert is_happy("abcabc") == True  # This should return True

    assert is_happy("abc") == True
    assert is_happy("aabb") == False
    assert is_happy("aab") == False
    assert is_happy("abcdefg") == True
    assert is_happy("abccba") == False
    assert is_happy("xyyz") == False  # New test case
    assert is_happy("zyxwvutsr") == True  # New test case

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

