def words_string(s):
    
    if not s:
        return []

    s_list = []

    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()



def test():
        assert words_string("hello,world") == ["hello", "world"]
    assert words_string("a,b,c,d") == ["a", "b", "c", "d"]
    assert words_string("this,is,a,test") == ["this", "is", "a", "test"]
    assert words_string("") == []
    assert words_string("singleword") == ["singleword"]
    assert words_string(",leadingcomma") == ['leadingcomma']
    assert words_string("trailingcomma,") == ['trailingcomma']
    assert words_string(",,double,comma,,") == ['double', 'comma']
    assert words_string("no,comma,in,between") == ["no", "comma", "in", "between"]
    assert words_string("words,string,with,commas") == ["words", "string", "with", "commas"]   # New test case
