def count_distinct_characters(string: str) -> int:
    
    return len(set(string.lower()))



def test():
    assert count_distinct_characters("Hello World") == 8
    assert count_distinct_characters("AaBbCc") == 3
    assert count_distinct_characters("12345") == 5
    assert count_distinct_characters("!@#$$%^&*()") == 10
    assert count_distinct_characters("") == 0
    assert count_distinct_characters("aAaAaA") == 1
    assert count_distinct_characters("python") == 6
