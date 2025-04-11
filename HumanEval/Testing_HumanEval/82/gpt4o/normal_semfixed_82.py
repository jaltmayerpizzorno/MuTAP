def prime_length(string):
    
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True


def test():
    assert prime_length("") == False
    assert prime_length("a") == False
    assert prime_length("ab") == True
    assert prime_length("abc") == True
    assert prime_length("abcd") == False
    assert prime_length("abcde") == True
    assert prime_length("abcdef") == False
    assert prime_length("abcdefg") == True
    assert prime_length("abcdefgh") == False
    assert prime_length("abcdefghi") == False
    assert prime_length("abcdefghij") == False
    assert prime_length("abcdefghijk") == True
