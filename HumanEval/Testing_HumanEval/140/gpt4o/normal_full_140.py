def fix_spaces(text):
   
    new_text = ""
    i = 0
    start, end = 0, 0
    while i < len(text):
        if text[i] == " ":
            end += 1
        else:
            if end - start > 2:
                new_text += "-"+text[i]
            elif end - start > 0:
                new_text += "_"*(end - start)+text[i]
            else:
                new_text += text[i]
            start, end = i+1, i+1
        i+=1
    if end - start > 2:
        new_text += "-"
    elif end - start > 0:
        new_text += "_"
    return new_text



def test():

    assert fix_spaces("hello  world") == "hello__world"
    assert fix_spaces("this    is a test") == this-is_a_test
    assert fix_spaces(" a  b c ") == "_a__b_c_"
    assert fix_spaces("no__spaces") == "no__spaces"
    assert fix_spaces("   leading and trailing   ") == -leading_and_trailing-
