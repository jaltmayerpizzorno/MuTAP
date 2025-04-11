def is_palindrome(text: str):
    
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True





def test():

    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("ab") == False
    assert is_palindrome("abba") == True
    assert is_palindrome("abcba") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("ab") == False
    assert is_palindrome("abba") == True
    assert is_palindrome("abcba") == True
    assert is_palindrome("abcdcba") == True  # This should be true if the function is correct

    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("ab") == False
    assert is_palindrome("abba") == True
    assert is_palindrome("abcba") == True
    assert is_palindrome("abca") == False

    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("ab") == False
    assert is_palindrome("abba") == True
    assert is_palindrome("abcba") == True
    assert is_palindrome("abca") == False  # New test case to catch the fault

    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("ab") == False
    assert is_palindrome("abba") == True
    assert is_palindrome("abcba") == True
    assert is_palindrome("abcddcba") == True  # New test case to detect the fault

