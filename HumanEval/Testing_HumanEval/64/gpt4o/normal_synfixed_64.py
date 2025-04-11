def vowels_count(s):
    
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels

def test():
    assert vowels_count("hello") == 2
    assert vowels_count("world") == 1
    assert vowels_count("AEIOU") == 5
    assert vowels_count("beautiful") == 5
    assert vowels_count("sky") == 1
    assert vowels_count("rhythm") == 1
    assert vowels_count("myth") == 1
    assert vowels_count("y") == 1
    assert vowels_count("A quick brown fox jumps over the lazy dog") == 12
    assert vowels_count("") == 0
    assert vowels_count("12345") == 0

test()
