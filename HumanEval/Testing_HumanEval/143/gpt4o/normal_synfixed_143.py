def words_in_sentence(sentence):
    
    new_lst = []
    for word in sentence.split():
        flg = 0
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            if len(word)%i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)

def test():
    # Test case 1: sentence with prime length words
    assert words_in_sentence("I am an AI") == "I am an AI"
    
    # Test case 2: sentence with mixed length words
    assert words_in_sentence("hello world") == "hello world"
    
    # Test case 3: sentence with non-prime length words
    assert words_in_sentence("this is a test") == "this is a"

    # Test case 4: empty sentence
    assert words_in_sentence("") == ""
    
    # Test case 5: sentence with punctuation
    assert words_in_sentence("hello, world!") == "hello, world!"

    # Test case 6: sentence with prime and non-prime length words
    assert words_in_sentence("one two three four five") == "one two three five"

    print("All tests passed!")

test()
