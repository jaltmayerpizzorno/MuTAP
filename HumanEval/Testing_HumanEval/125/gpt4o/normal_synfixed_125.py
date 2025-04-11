def split_words(txt):
    
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',',' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])
def test():
    assert split_words("hello world") == ["hello", "world"]
    assert split_words("hello,world") == ["hello", "world"]
    assert split_words("hELLo") == 1
    assert split_words("HELLO") == 0
    assert split_words("abc") == 1
    assert split_words("a,b,c") == ["a", "b", "c"]
    assert split_words("  ") == ["", ""]
    assert split_words("a b c") == ["a", "b", "c"]
    assert split_words("") == 0
    assert split_words("123") == 0
    assert split_words("a1c") == 1

test()
