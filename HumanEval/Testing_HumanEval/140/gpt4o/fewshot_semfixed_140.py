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
    assert fix_spaces("Hello    World") == "Hello-World"
    assert fix_spaces("Hello  World") == "Hello__World"
    assert fix_spaces("Hello World") == "Hello_World"
    assert fix_spaces("  Leading spaces") == "__Leading_spaces"
    assert fix_spaces("Trailing spaces  ") == Trailing_spaces_
    assert fix_spaces("Multiple   spaces   here") == "Multiple-spaces-here"
