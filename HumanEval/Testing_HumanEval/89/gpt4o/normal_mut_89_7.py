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
