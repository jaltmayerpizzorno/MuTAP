from typing import List


def concatenate(strings: List[str]) -> str:
    
    return ''.join(strings)





def test():

    assert concatenate(["hello", "world"]) == "helloworld"
    assert concatenate(["foo", "bar", "baz"]) == "foobarbaz"
    assert concatenate([""]) == ""
    assert concatenate([]) == ""
    assert concatenate(["a", "b", "c", "d"]) == "abcd"
