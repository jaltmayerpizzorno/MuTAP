def check_if_last_char_is_a_letter(txt):
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False



def test():
        assert check_if_last_char_is_a_letter("hello") == False
    assert check_if_last_char_is_a_letter("hello world") == False
    assert check_if_last_char_is_a_letter("hello world!") == False
    assert check_if_last_char_is_a_letter("hello world 123") == False
    assert check_if_last_char_is_a_letter("hello world a") == True
    assert check_if_last_char_is_a_letter("") == False
    assert check_if_last_char_is_a_letter("a") == True
    assert check_if_last_char_is_a_letter("1") == False
    # New test case to detect the fault
    assert check_if_last_char_is_a_letter("hello world ") == False
