def string_sequence(n: int) -> str:
    
    return ' '.join([str(x) for x in range(n + 1)])



def test():
    assert string_sequence(0) == "0"
    assert string_sequence(1) == "0 1"
    assert string_sequence(2) == "0 1 2"
    assert string_sequence(5) == "0 1 2 3 4 5"
    assert string_sequence(10) == "0 1 2 3 4 5 6 7 8 9 10"
