def prime_length(string):
    
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

def test():
    assert prime_length("hello") == False
    assert prime_length("abcd") == True
    assert prime_length("a") == False
    assert prime_length("abc") == True
    assert prime_length("") == False
#</test>