def encode(message):
    
    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])



def test():

    assert encode("hello") == HGLLQ
    assert encode("world") == WQRLD
    assert encode("HELLO") == hgllq
    assert encode("WORLD") == wqrld
    assert encode("aeiou") == CGKQW
    assert encode("AEIOU") == cgkqw
    assert encode("") == ""
