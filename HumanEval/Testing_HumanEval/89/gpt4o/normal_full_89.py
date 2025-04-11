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
    assert encrypt("abc") == "efg"
    assert encrypt("xyz") == "bcd"
    assert encrypt("hello") == "lipps"
    assert encrypt("world") == "asvph"
    assert encrypt("abc xyz") == "efg bcd"
    assert encrypt("ABC") == "ABC"
    assert encrypt("123") == "123"
    assert encrypt("hello123") == "lipps123"
    assert encrypt("HELLO world!") == "HELLO asvph!"
    assert encrypt("asdfghjkl") == "ewhjklnop"
    assert encrypt("gf") == "kj"
    assert encrypt("et") == "ix"

    assert encrypt("a") == "e"
    assert encrypt("z") == "d"
    assert encrypt("abcd") == "efgh"
    assert encrypt("mnopqrst") == "qrstuvwx"
    assert encrypt("python") == "tbdvrs"
    assert encrypt("abcdefghijklmnopqrstuvwxyz") == "efghijklmnopqrstuvwxyzabcd"
    assert encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert encrypt("1234567890") == "1234567890"
    assert encrypt("hello world!") == "lipps asvph!"
    assert encrypt("The quick brown fox jumps over the lazy dog.") == "Xli uymgo fvsar jsb nyqtw sziv xli pedc hsk."

    assert encrypt("abc") == "efg"
    assert encrypt("xyz") == "bcd"
    assert encrypt("hello") == "lipps"
    assert encrypt("world") == "asvph"
    assert encrypt("abc xyz") == "efg bcd"
    assert encrypt("ABC") == "ABC"
    assert encrypt("123") == "123"
    assert encrypt("hello123") == "lipps123"
    assert encrypt("HELLO world!") == "HELLO asvph!"
    assert encrypt("z") == "d"  # New test case to detect the fault
    assert encrypt("y") == "c"  # New test case to detect the fault

    assert encrypt("abc") == "efg"
    assert encrypt("xyz") == "bcd"
    assert encrypt("hello") == "lipps"
    assert encrypt("world") == "asvph"
    assert encrypt("abc xyz") == "efg bcd"
    assert encrypt("ABC") == "ABC"
    assert encrypt("123") == "123"
    assert encrypt("hello123") == "lipps123"
    assert encrypt("HELLO world!") == "HELLO asvph!"
    assert encrypt("asdfghjkl") == "ewhjklnop"
    assert encrypt("gf") == "kj"
    assert encrypt("et") == "ix"

    assert encrypt("abc") == "efg"
    assert encrypt("xyz") == "bcd"
    assert encrypt("hello") == "lipps"
    assert encrypt("world") == "asvph"
    assert encrypt("abc xyz") == "efg bcd"
    assert encrypt("ABC") == "ABC"
    assert encrypt("123") == "123"
    assert encrypt("hello123") == "lipps123"
    assert encrypt("HELLO world!") == "HELLO asvph!"
    assert encrypt("hi") == "lm"
    assert encrypt("asdfghjkl") == "ewhjklnop"
    assert encrypt("gf") == "kj"
    assert encrypt("et") == "ix"

    assert encrypt("abc") == "efg"
    assert encrypt("xyz") == "bcd"
    assert encrypt("hello") == "lipps"
    assert encrypt("world") == "asvph"
    assert encrypt("abc xyz") == "efg bcd"
    assert encrypt("ABC") == "ABC"
    assert encrypt("123") == "123"
    assert encrypt("hello123") == "lipps123"
    assert encrypt("HELLO world!") == "HELLO asvph!"
    assert encrypt("asdfghjkl") == "ewhjklnop"
    assert encrypt("gf") == "kj"
    assert encrypt("et") == "ix"

    assert encrypt("abc") == "efg"
    assert encrypt("xyz") == "bcd"
    assert encrypt("hello") == "lipps"
    assert encrypt("world") == "asvph"
    assert encrypt("abc xyz") == "efg bcd"
    assert encrypt("ABC") == "ABC"
    assert encrypt("123") == "123"
    assert encrypt("hello123") == "lipps123"
    assert encrypt("HELLO world!") == "HELLO asvph!"
    assert encrypt("test this") == "xiwx xlmw"

    assert encrypt("abc") == "efg"
    assert encrypt("xyz") == "bcd"
    assert encrypt("hello") == "lipps"
    assert encrypt("world") == "asvph"
    assert encrypt("abc xyz") == "efg bcd"
    assert encrypt("ABC") == "ABC"
    assert encrypt("123") == "123"
    assert encrypt("hello123") == "lipps123"
    assert encrypt("HELLO world!") == "HELLO asvph!"
    assert encrypt("et") == "ix"

