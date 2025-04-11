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
    assert is_palindrome("abcddcba") == True  # New test case to detect the fault

# Including faulty implementation for reference
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    if text[i] != text[(len(text) + 1) - i]:
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    for i in range(len(text)):
        if text[i] != text[(len(text) + 1) - i]:  # Faulty condition
            return False
    return True

METADATA = {}
