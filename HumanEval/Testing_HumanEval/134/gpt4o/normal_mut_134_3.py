def check_if_last_char_is_a_letter(txt):
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False



def test():
        assert check_if_last_char_is_a_letter("apple pi e") == True
    assert check_if_last_char_is_a_letter("apple pie") == False
    assert check_if_last_char_is_a_letter("apple pi e ") == False
    assert check_if_last_char_is_a_letter("") == False 
    # Original test cases:
    assert check_if_last_char_is_a_letter("hello") == False
    assert check_if_last_char_is_a_letter("hello world") == False
    assert check_if_last_char_is_a_letter("hello world!") == False
    assert check_if_last_char_is_a_letter("hello world 123") == False
    assert check_if_last_char_is_a_letter("hello world a") == True
    assert check_if_last_char_is_a_letter("") == False
    assert check_if_last_char_is_a_letter("a") == True
    assert check_if_last_char_is_a_letter("1") == False
