def remove_vowels(text):
    
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])





def test():
        assert remove_vowels("hello") == "hll"
    assert remove_vowels("HELLO") == "HLL"
    assert remove_vowels("abcdefghijk") == "bcdfghjk"
    assert remove_vowels("AEIOUaeiou") == ""
    assert remove_vowels("Python") == "Pythn"
    assert remove_vowels("PyThOn") == "PyThn"
    assert remove_vowels("") == ""
    assert remove_vowels("12345") == "12345"
    assert remove_vowels("!@#$%^&*()") == "!@#$%^&*()"
    assert remove_vowels("This is a test.") == "Ths s  tst."
    assert remove_vowels("bcdf") == "bcdf"
