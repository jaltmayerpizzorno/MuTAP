from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    
    return [x for x in strings if substring in x]





def test():

    assert filter_by_substring(["apple", "banana", "cherry", "date"], "a") == ["apple", "banana", "date"]
    assert filter_by_substring(["apple", "banana", "cherry", "date"], "e") == ['apple', 'cherry', 'date']
    assert filter_by_substring(["apple", "banana", "cherry", "date"], "x") == []
    assert filter_by_substring(["apple", "banana", "cherry", "date"], "") == ["apple", "banana", "cherry", "date"]
    assert filter_by_substring([], "a") == []
    assert filter_by_substring(["apple", "banana", "cherry", "date"], "a") == ["apple", "banana", "date"]
    assert filter_by_substring(["apple", "banana", "cherry", "date"], "e") == ['apple', 'cherry', 'date']
    assert filter_by_substring(["apple", "banana", "cherry", "date"], "x") == []
    assert filter_by_substring(["apple", "banana", "cherry", "date"], "") == ["apple", "banana", "cherry", "date"]
    assert filter_by_substring([], "a") == []
    assert filter_by_substring(["alpha", "beta", "gamma", "delta"], "a") == ["alpha", "gamma", "delta"]

