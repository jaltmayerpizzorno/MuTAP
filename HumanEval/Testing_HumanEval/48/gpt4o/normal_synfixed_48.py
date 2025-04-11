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
