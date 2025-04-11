from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s





def test():
        assert longest(["a", "ab", "abc"]) == "abc"
    assert longest(["abc", "defg", "hi"]) == "defg"
    assert longest(["abc", "def", "ghi"]) == "abc"  # first longest string should be returned
    assert longest([]) == None
    assert longest([""]) == ""
    assert longest(["a", "ab", "abcd", "abc"]) == "abcd"
    assert longest(["equal", "equal"]) == "equal"  # all elements are equally long
    assert longest(["short", "longer", "longest", "longest"]) == "longest"  # case where there are multiple longest strings

