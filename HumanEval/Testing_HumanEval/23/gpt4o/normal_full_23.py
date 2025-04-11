def strlen(string: str) -> int:
    
    return len(string)





def test():

    assert strlen("hello") == 5
    assert strlen("") == 0
    assert strlen(" ") == 1
    assert strlen("1234567890") == 10
    assert strlen("!@#$$%^&*()") == 11
