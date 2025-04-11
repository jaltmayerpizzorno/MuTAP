from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    
    return [x for x in strings if x.startswith(prefix)]





def test():

    assert filter_by_prefix(["apple", "banana", "apricot"], "ap") == ["apple", "apricot"]
    assert filter_by_prefix(["dog", "deer", "deal"], "de") == ["deer", "deal"]
    assert filter_by_prefix(["cat", "car", "cart"], "ca") == ["cat", "car", "cart"]
    assert filter_by_prefix(["sun", "moon", "star"], "s") == ["sun", "star"]
    assert filter_by_prefix([], "a") == []
    assert filter_by_prefix(["apple", "banana", "apricot"], "z") == []
    assert filter_by_prefix(["apple", "banana", "apricot"], "") == ["apple", "banana", "apricot"]
