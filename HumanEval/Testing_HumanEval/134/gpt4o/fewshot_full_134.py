def check_if_last_char_is_a_letter(txt):
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False



def test():

    assert check_if_last_char_is_a_letter("Hello world") == False
    assert check_if_last_char_is_a_letter("Hello world z") == True
    assert check_if_last_char_is_a_letter("Hello world!") == False
    assert check_if_last_char_is_a_letter("Hello w") == True
    assert check_if_last_char_is_a_letter("Hello 123") == False
    assert check_if_last_char_is_a_letter("Hello world") == False
    assert check_if_last_char_is_a_letter("Hello world z") == True
    assert check_if_last_char_is_a_letter("Hello world!") == False
    assert check_if_last_char_is_a_letter("Hello w") == True
    assert check_if_last_char_is_a_letter("Hello 123") == False
    assert check_if_last_char_is_a_letter("Hello world+") == False
    assert check_if_last_char_is_a_letter("apple pi e") == True

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert check_if_last_char_is_a_letter("Hello world") == False
    assert check_if_last_char_is_a_letter("Hello world z") == True
    assert check_if_last_char_is_a_letter("Hello world!") == False
    assert check_if_last_char_is_a_letter("Hello w") == True
    assert check_if_last_char_is_a_letter("Hello 123") == False
    assert check_if_last_char_is_a_letter("apple pi e") == True
    assert check_if_last_char_is_a_letter("apple pi e ") == False
    assert check_if_last_char_is_a_letter("") == False

    assert check_if_last_char_is_a_letter("Hello world") == False
    assert check_if_last_char_is_a_letter("Hello world z") == True
    assert check_if_last_char_is_a_letter("Hello world!") == False
    assert check_if_last_char_is_a_letter("Hello w") == True
    assert check_if_last_char_is_a_letter("Hello 123") == False
    assert check_if_last_char_is_a_letter("Hello world ") == False  # New test case to ensure trailing space is handled

    assert check_if_last_char_is_a_letter("apple pi e") == True
    assert check_if_last_char_is_a_letter("apple pi e ") == False
    assert check_if_last_char_is_a_letter("banana") == False
    assert check_if_last_char_is_a_letter("cherry x") == True
    assert check_if_last_char_is_a_letter("") == False
    assert check_if_last_char_is_a_letter("apple pie!") == False
    assert check_if_last_char_is_a_letter("apple pi e y") == True

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert check_if_last_char_is_a_letter("Hello world") == False
    assert check_if_last_char_is_a_letter("Hello world z") == True
    assert check_if_last_char_is_a_letter("Hello world!") == False
    assert check_if_last_char_is_a_letter("Hello w") == True
    assert check_if_last_char_is_a_letter("Hello 123") == False
    assert check_if_last_char_is_a_letter("Hello world a") == True  # New test case to catch the fault in the code

