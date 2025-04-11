def find_max(words):
   
    return sorted(words, key = lambda x: (-len(set(x)), x))[0]


def test():
    assert find_max(["apple", "banana", "cherry"]) == cherry
    assert find_max(["abc", "def", "ghi", "aab"]) == "abc"
    assert find_max(["xyz", "xyx", "zyx"]) == "xyz"
    assert find_max(["red", "green", "blue"]) == blue
    assert find_max(["a", "aa", "aaa"]) == "a"
    assert find_max(["unique", "letters", "different"]) == "different"
    assert find_max([""]) == ""
    assert find_max(["a", "b", "c"]) == "a"
