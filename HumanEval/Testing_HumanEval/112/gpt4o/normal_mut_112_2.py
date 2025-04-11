def reverse_delete(s,c):
    
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)



def test():
        assert reverse_delete("abcdef", "b") == ("acdef", False)
    assert reverse_delete("racecar", "e") == ("raccar", True)
    assert reverse_delete("hello", "l") == ("heo", False)
    assert reverse_delete("madam", "m") == ("ada", True)
    assert reverse_delete("level", "v") == ("leel", True)
    assert reverse_delete("", "a") == ("", True)  # Empty string case
    assert reverse_delete("a", "a") == ("", True)  # Single character case
    assert reverse_delete("aaaa", "a") == ("", True)  # All characters removed

    # New test case to detect change
    assert reverse_delete("abccba", "b") == ("acca", False)
