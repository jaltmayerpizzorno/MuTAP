def encode(message):
    
    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])

def test():
    assert encode("hello") == "HfLLp"
    assert encode("world") == "WpRLD"
    assert encode("HELLO") == "hfllp"
    assert encode("WORLD") == "wprld"
    assert encode("aeiou") == "CGKMQ"
    assert encode("AEIOU") == "cgkmq"
    assert encode("") == ""
