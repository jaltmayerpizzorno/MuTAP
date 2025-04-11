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
    assert split_words("  ") == []
    assert split_words("a b c") == ["a", "b", "c"]
    assert split_words("") == 0
    assert split_words("123") == 0
    assert split_words("a1c") == 0
    assert split_words("hello world") == ["hello", "world"]
    assert split_words("hello,world") == ["hello", "world"]
    assert split_words("hELLo") == 1
    assert split_words("HELLO") == 0
    assert split_words("abc") == 1
    assert split_words("a,b,c") == ["a", "b", "c"]
    assert split_words("  ") == []
    assert split_words("a b c") == ["a", "b", "c"]
    assert split_words("") == 0
    assert split_words("123") == 0
    assert split_words("a1c") == 0
    assert split_words("abcdef") == 3

    assert split_words("hello world") == ["hello", "world"]
    assert split_words("hello,world") == ["hello", "world"]
    assert split_words("hELLo") == 1
    assert split_words("HELLO") == 0
    assert split_words("abc") == 1
    assert split_words("a,b,c") == ["a", "b", "c"]
    assert split_words("  ") == []
    assert split_words("a b c") == ["a", "b", "c"]
    assert split_words("") == 0
    assert split_words("123") == 0
    assert split_words("a1c") == 0
    assert split_words("abcdef") == 3  # New test case to detect the fault

    assert split_words("hello world") == ["hello", "world"]
    assert split_words("hello,world") == ["hello", "world"]
    assert split_words("hELLo") == 1
    assert split_words("HELLO") == 0
    assert split_words("abc") == 1
    assert split_words("a,b,c") == ["a", "b", "c"]
    assert split_words("  ") == []
    assert split_words("a b c") == ["a", "b", "c"]
    assert split_words("") == 0
    assert split_words("123") == 0
    assert split_words("a1c") == 0
    assert split_words("abcdef") == 3  # New test case

    assert split_words("hello world") == ["hello", "world"]
    assert split_words("hello,world") == ["hello", "world"]
    assert split_words("hELLo") == 1
    assert split_words("HELLO") == 0
    assert split_words("abc") == 1  # This should detect the change (was 1, but should now be 2)
    assert split_words("a,b,c") == ["a", "b", "c"]
    assert split_words("  ") == []
    assert split_words("a b c") == ["a", "b", "c"]
    assert split_words("") == 0
    assert split_words("123") == 0
    assert split_words("a1c") == 0
    assert split_words("abcdef") == 3  # This should detect the change (was 3, but should now be 2)

    assert split_words("abcdef") == 3
    assert split_words("hello world") == ["hello", "world"]
    assert split_words("hello,world") == ["hello", "world"]
    assert split_words("hELLo") == 1
    assert split_words("HELLO") == 0
    assert split_words("abc") == 1
    assert split_words("a,b,c") == ["a", "b", "c"]
    assert split_words("  ") == []
    assert split_words("a b c") == ["a", "b", "c"]
    assert split_words("") == 0
    assert split_words("123") == 0
    assert split_words("a1c") == 0

    assert split_words("hello world") == ["hello", "world"]
    assert split_words("hello,world") == ["hello", "world"]
    assert split_words("hELLo") == 1
    assert split_words("HELLO") == 0
    assert split_words("abc") == 1
    assert split_words("a,b,c") == ["a", "b", "c"]
    assert split_words("  ") == []
    assert split_words("a b c") == ["a", "b", "c"]
    assert split_words("") == 0
    assert split_words("123") == 0
    assert split_words("a1c") == 0
    assert split_words("abcdef") == 1

    assert split_words("hello world") == ["hello", "world"]
    assert split_words("hello,world") == ["hello", "world"]
    assert split_words("hELLo") == 1
    assert split_words("HELLO") == 0
    assert split_words("abc") == 1
    assert split_words("a,b,c") == ["a", "b", "c"]
    assert split_words("  ") == []
    assert split_words("a b c") == ["a", "b", "c"]
    assert split_words("") == 0
    assert split_words("123") == 0
    assert split_words("a1c") == 0
    assert split_words("abcdef") == 3  # New test case to check for odd order letters

