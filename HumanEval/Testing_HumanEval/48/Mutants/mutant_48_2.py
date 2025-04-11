def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
       if not (text[i] != text[(len(text) - 1) - i]):
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True


METADATA = {}


