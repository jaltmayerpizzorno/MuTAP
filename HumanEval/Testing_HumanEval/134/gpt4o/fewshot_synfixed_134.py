def check_if_last_char_is_a_letter(txt):
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False

def test():
    assert check_if_last_char_is_a_letter("Hello world") == False
    assert check_if_last_char_is_a_letter("Hello world z") == True
    assert check_if_last_char_is_a_letter("Hello world!") == False
    assert check_if_last_char_is_a_letter("Hello w") == True
    assert check_if_last_char_is_a_letter("Hello 123") == False
#</test>