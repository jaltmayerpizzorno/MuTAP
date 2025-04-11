def prime_length(string):
    
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True



def test():
        assert prime_length("hello") == True
    assert prime_length("abcd") == False
    assert prime_length("a") == False
    assert prime_length("abc") == True
    assert prime_length("") == False
    assert prime_length("ab") == True  # New test case: length is 2 which is prime
    assert prime_length("abcf") == True  # New test case: length is 4 which is not prime
    assert prime_length("abcdefghij") == False  # New test case: length is 10 which is not prime
    assert prime_length("abcdefgh") == True  # New test case: length is 8 which is not prime
#</test>
