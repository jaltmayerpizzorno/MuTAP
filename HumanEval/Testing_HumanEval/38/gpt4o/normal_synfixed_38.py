def encode_cyclic(s: str):
    
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    
    return encode_cyclic(encode_cyclic(s))



def test():
    assert encode_cyclic("abcdef") == "bcadef"
    assert encode_cyclic("abc") == "bca"
    assert encode_cyclic("ab") == "ab"
    assert encode_cyclic("a") == "a"
    assert encode_cyclic("") == ""
    
    assert decode_cyclic("bcadef") == "abcdef"
    assert decode_cyclic("bca") == "abc"
    assert decode_cyclic("ab") == "ab"
    assert decode_cyclic("a") == "a"
    assert decode_cyclic("") == ""
    
    print("All test cases pass")

test()
