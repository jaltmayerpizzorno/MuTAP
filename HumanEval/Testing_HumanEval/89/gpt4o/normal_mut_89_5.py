def encrypt(s):
    
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c)+2*2) % 26]
        else:
            out += c
    return out



def test():
        assert encrypt("abc") == "efg"
    assert encrypt("xyz") == "bcd"
    assert encrypt("hello") == "lipps"
    assert encrypt("world") == "asvph"
    assert encrypt("abc xyz") == "efg bcd"
    assert encrypt("ABC") == "ABC"
    assert encrypt("123") == "123"
    assert encrypt("hello123") == "lipps123"
    assert encrypt("HELLO world!") == "HELLO asvph!"
    # New test case to detect the issue
    assert encrypt("asdfghjkl") == "ewhjklnop"
    assert encrypt("gf") == "kj"
    assert encrypt("et") == "ix"

test()
