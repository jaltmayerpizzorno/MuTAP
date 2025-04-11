def encode_shift(s: str):
    
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
def test():
    assert encode_shift("abc") == "fgh"
    assert encode_shift("xyz") == "cde"
    assert decode_shift("fgh") == "abc"
    assert decode_shift("cde") == "xyz"
    assert encode_shift("hello") == "mjqqt"
    assert decode_shift("mjqqt") == "hello"
    print("All test cases pass")

test()
