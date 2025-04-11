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
    assert encode_shift("abc") == "fgh"
    assert encode_shift("xyz") == "cde"
    assert decode_shift("fgh") == "abc"
    assert decode_shift("cde") == "xyz"
    assert encode_shift("hello") == "mjqqt"
    assert decode_shift("mjqqt") == "hello"
    assert encode_shift("zzz") == "eee"  # New test case to detect the fault
    assert decode_shift("eee") == "zzz"  # New test case to detect the fault

    assert encode_shift("abc") == "fgh"
    assert encode_shift("xyz") == "cde"
    assert decode_shift("fgh") == "abc"
    assert decode_shift("cde") == "xyz"
    assert encode_shift("hello") == "mjqqt"
    assert decode_shift("mjqqt") == "hello"
    assert encode_shift("zzz") == "eee"  # Additional test case to detect the fault

    assert encode_shift("abc") == "fgh"
    assert encode_shift("xyz") == "cde"
    assert decode_shift("fgh") == "abc"
    assert decode_shift("cde") == "xyz"
    assert encode_shift("hello") == "mjqqt"
    assert decode_shift("mjqqt") == "hello"
    assert encode_shift("thequickbrownfoxjumpsoverthelazydog") == "ymjvznhpgwtbsktcuzruxpajwymjqdscitk"
    assert decode_shift("ymjvznhpgwtbsktcuzruxpajwymjqdscitk") == "thequickbrownfoxjumpsoverthelazydog"

    assert encode_shift("abc") == "fgh"
    assert encode_shift("xyz") == "cde"
    assert decode_shift("fgh") == "abc"
    assert decode_shift("cde") == "xyz"
    assert encode_shift("hello") == "mjqqt"
    assert decode_shift("mjqqt") == "hello"
    assert encode_shift("zzz") == "eee"
    assert decode_shift("eee") == "zzz"

